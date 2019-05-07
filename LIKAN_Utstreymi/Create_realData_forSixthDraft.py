import psycopg2

from Functions.Select_function import Select_string
from Functions.Write_Vendor_data import Write_vendor_data
from Functions.Write_sendingarVendorar_data import Write_sendingar_data

#Connection to SQL
host = 'localhost'
dbname = 'atvr2'
username = 'postgres'
pw = 'postgres'

conn_string = "host='{}' dbname='{}' user='{}' password='{}'"

try:
    conn = psycopg2.connect(conn_string.format(host, dbname, username, pw))
except psycopg2.OperationalError as e:
    print('Connection failed')
    print('Error: ', e)
    exit()
cursor = conn.cursor()


#----------------------------------------------------------------------------
# Write the select Q
#----------------------------------------------------------------------------

selectstring = Select_string(1)
cursor.execute(selectstring)
arr = cursor.fetchall()


#SELECT fyrir utstreymi
selectstring_uts = "Select u.Ship_Code,u.Destination, sum(u.Quantity*c.Timevalue), u.date, count(u.Total_Qty) from Utstreymi u, Item_Category c, Item i where u.ItemNo = i.id and i.tegund = c.name and u.date in('12/02/2018','13/02/2018','14/02/2018','15/02/2018','16/02/2018') group by u.Ship_Code , u.date, u.Destination order by u.Ship_Code "
cursor.execute(selectstring_uts)
arr_uts = cursor.fetchall()


fjoldiSendinga = 0
fjoldiSendinga_innstreymi = 0
for x in arr:
	fjoldiSendinga = fjoldiSendinga + 1
	fjoldiSendinga_innstreymi = fjoldiSendinga_innstreymi + 1

for x in arr_uts:
	fjoldiSendinga = fjoldiSendinga + 1

#----------------------------------------------------------------------------
# Create data file
#----------------------------------------------------------------------------

#DETERMINE VALUES
Days = 5
Timeslots = 8
Sendingar = fjoldiSendinga -1
windowsize = 0

#START WRITING THE FILE
f= open("demo_data_real.txt","w+")
f.write("param S := {};\r\n".format(Sendingar))
f.write("param T := {};\r\n".format(Timeslots))
f.write("param D := {};\r\n".format(Days))
f.write("param windowsize := {};\r\n".format(windowsize))
f.write("\r\n")


#----------------------------------------------------------------------
# VENDORAR & TIMESLOTT
#----------------------------------------------------------------------

vendor = 'O'
Write_vendor_data(1,vendor,Timeslots,f)


#EIMSKIP OG SAMSKIP
vendor = 'EIM'
Write_vendor_data(7,vendor,Timeslots,f)

vendor = 'SAM'
Write_vendor_data(8,vendor,Timeslots,f)

#----------------------------------------------------------------------
# ALAG & TARGET
#----------------------------------------------------------------------

#Write the ALAG & CREATE the sequence i
f.write("param A := \r\n")
for i in range(1,fjoldiSendinga_innstreymi):
	f.write("{} {}\r\n".format(i,round(arr[i][4]*arr[i][3])))   #timevalue * Qty

counter = 0
for i in range(fjoldiSendinga_innstreymi,Sendingar+1):
	f.write("{} {}\r\n".format(i,round(arr_uts[counter][2])))
	counter = counter + 1
f.write(";\r\n")
f.write("\r\n")

#Write the TARGET
f.write("param Ttarget := \r\n")

for i in range(1,Days+1):
	for x in range(1,Timeslots+1):
		if x in (1,2,3,4):
			f.write("{} {} {}\r\n".format(x,i,2000))
		if x in (5,6):
			f.write("{} {} {}\r\n".format(x,i,2000))
		if x in (7,8):
			f.write("{} {} {}\r\n".format(x,i,1500))
		if x in (9,10,11,12):
			f.write("{} {} {}\r\n".format(x,i,2000))
f.write(";\r\n")
f.write("\r\n")


#----------------------------------------------------------------------
#CREATE OF SENDINGAR FOR EACH VENDOR
#----------------------------------------------------------------------

all_sendingar = []
rest_sendingar = []

Ol_kennitolur = ['420369-7789']
vendorname = 'Olgerdin'
Write_sendingar_data(arr,Ol_kennitolur,vendorname,fjoldiSendinga_innstreymi-1,f,all_sendingar)

Cola_kennitolur = ['470169-1419']
vendorname = 'Cola'
Write_sendingar_data(arr,Cola_kennitolur,vendorname,fjoldiSendinga_innstreymi-1,f,all_sendingar)

G_kennitolur = ['570169-0339']
vendorname = 'Globus'
Write_sendingar_data(arr,G_kennitolur,vendorname,fjoldiSendinga_innstreymi-1,f,all_sendingar)

V_kennitolur = ['700103-3660']
vendorname = 'Vintrio'
Write_sendingar_data(arr,V_kennitolur,vendorname,fjoldiSendinga_innstreymi-1,f,all_sendingar)

BR_kennitolur = ['541205-1520']
vendorname = 'Brugghusstedja'
Write_sendingar_data(arr,BR_kennitolur,vendorname,fjoldiSendinga_innstreymi-1,f,all_sendingar)

DI_kennitolur = ['410999-2859']
vendorname = 'Dista'
Write_sendingar_data(arr,DI_kennitolur,vendorname,fjoldiSendinga_innstreymi-1,f,all_sendingar)

BA_kennitolur = ['530303-2410']
vendorname = 'Bakkus'
Write_sendingar_data(arr,BA_kennitolur,vendorname,fjoldiSendinga_innstreymi-1,f,all_sendingar)

M_kennitolur = ['550595-2579']
vendorname = 'Mekka'
Write_sendingar_data(arr,M_kennitolur,vendorname,fjoldiSendinga_innstreymi-1,f,all_sendingar)

#EIMSKIP OG SAMSKIP
EIM_kennitolur = ["601083-0789","470105-2240","490104-2160","450310-0500"
,"491007-1680","511105-1290","601289-1489","470302-4290",
"640485-0949","420178-0349","531212-0530","451205-0560",
"470706-1040","451295-2929","530206-0330","620509-0190","470205-0400"]

vendorname = 'Eimskip'
Write_sendingar_data(arr,EIM_kennitolur,vendorname,fjoldiSendinga_innstreymi-1,f,all_sendingar)


#Ekki endilega réttar kennitölur...
SAM_kennitolur = ['550394-2359','470415-1260','660509-0970','470710-0390','670616-1690',
'460999-2519','501117-0210','520914-2180','500316-0470','490211-0630','681215-1740','430913-0690'
,'660169-1729','600112-1390','590515-3290','550609-1420','471289-2569','650387-1399','560113-0480','560793-2199',
'550405-0400','571214-0240','451115-1460','510515-1020','440417-0510']

vendorname = 'Samskip'
Write_sendingar_data(arr,SAM_kennitolur,vendorname,fjoldiSendinga_innstreymi-1,f,all_sendingar)


#test
print(all_sendingar)

for i in range(1,Sendingar):
	if i not in all_sendingar:
		rest_sendingar.append(i)

print(rest_sendingar)
#----------------------------------------------------------------------
#Bannlisti & Fixlisti
#----------------------------------------------------------------------
f.write("set Bannlisti := \r\n")

for i  in range(fjoldiSendinga_innstreymi,Sendingar):
	for x in range(1,Days+1):
		for y in range(1,4):
			f.write("{} {} {}\r\n".format(i,y,x))


f.write(";\r\n")
print()


#s,t,d
f.write("set Fixlisti := \r\n")

f.write(";\r\n")

f.write("end;\r\n")
