import psycopg2

from datetime import datetime
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

vika = 1


#----------------------------------------------------------------------------
# Write the select Q
#----------------------------------------------------------------------------

selectstring = Select_string(vika)

cursor.execute(selectstring)
arr = cursor.fetchall()

fjoldiSendinga = 0
for x in arr:
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
'''
vendor = 'O'
Write_vendor_data(1,vendor,Timeslots,f)

vendor = 'C'
Write_vendor_data(2,vendor,Timeslots,f)

vendor = 'G'
Write_vendor_data(3,vendor,Timeslots,f)

vendor = 'V'
Write_vendor_data(3,vendor,Timeslots,f)

vendor = 'BR'
Write_vendor_data(4,vendor,Timeslots,f)

vendor = 'DI'
Write_vendor_data(4,vendor,Timeslots,f)

vendor = 'BA'
Write_vendor_data(5,vendor,Timeslots,f)

vendor = 'M'
Write_vendor_data(6,vendor,Timeslots,f)

#EIMSKIP OG SAMSKIP
vendor = 'EIM'
Write_vendor_data(7,vendor,Timeslots,f)

vendor = 'SAM'
Write_vendor_data(8,vendor,Timeslots,f)
'''
#----------------------------------------------------------------------
# ALAG & TARGET
#----------------------------------------------------------------------

#Write the ALAG & CREATE the sequence i
f.write("param A := \r\n")
for i in range(1,Sendingar+1):
	f.write("{} {}\r\n".format(i,round(arr[i][4]*arr[i][3])))   #timevalue * Qty
f.write(";\r\n")
f.write("\r\n")

#Write the TARGET
f.write("param Ttarget := \r\n")

for i in range(1,Days+1):
	for x in range(1,Timeslots+1):
		if x in (1,2,3,4):
			f.write("{} {} {}\r\n".format(x,i,1000))
		if x in (5,6,7,8):
			f.write("{} {} {}\r\n".format(x,i,500))
f.write(";\r\n")
f.write("\r\n")

#----------------------------------------------------------------------
#CREATE OF SENDINGAR FOR EACH VENDOR
#----------------------------------------------------------------------
'''
all_sendingar = []
rest_sendingar = []

Ol_kennitolur = ['420369-7789']
vendorname = 'Olgerdin'
Write_sendingar_data(arr,Ol_kennitolur,vendorname,Sendingar,f,all_sendingar)

Cola_kennitolur = ['470169-1419']
vendorname = 'Cola'
Write_sendingar_data(arr,Cola_kennitolur,vendorname,Sendingar,f,all_sendingar)

G_kennitolur = ['570169-0339']
vendorname = 'Globus'
Write_sendingar_data(arr,G_kennitolur,vendorname,Sendingar,f,all_sendingar)

V_kennitolur = ['700103-3660']
vendorname = 'Vintrio'
Write_sendingar_data(arr,V_kennitolur,vendorname,Sendingar,f,all_sendingar)

BR_kennitolur = ['541205-1520']
vendorname = 'Brugghusstedja'
Write_sendingar_data(arr,BR_kennitolur,vendorname,Sendingar,f,all_sendingar)

DI_kennitolur = ['410999-2859']
vendorname = 'Dista'
Write_sendingar_data(arr,DI_kennitolur,vendorname,Sendingar,f,all_sendingar)

BA_kennitolur = ['530303-2410']
vendorname = 'Bakkus'
Write_sendingar_data(arr,BA_kennitolur,vendorname,Sendingar,f,all_sendingar)

M_kennitolur = ['550595-2579']
vendorname = 'Mekka'
Write_sendingar_data(arr,M_kennitolur,vendorname,Sendingar,f,all_sendingar)

#EIMSKIP OG SAMSKIP
EIM_kennitolur = ["601083-0789","470105-2240","490104-2160","450310-0500"
,"491007-1680","511105-1290","601289-1489","470302-4290",
"640485-0949","420178-0349","531212-0530","451205-0560",
"470706-1040","451295-2929","530206-0330","620509-0190","470205-0400"]

vendorname = 'Eimskip'
Write_sendingar_data(arr,EIM_kennitolur,vendorname,Sendingar,f,all_sendingar)


#Ekki endilega réttar kennitölur...
SAM_kennitolur = ['550394-2359','470415-1260','660509-0970','470710-0390','670616-1690',
'460999-2519','501117-0210','520914-2180','500316-0470','490211-0630','681215-1740','430913-0690'
,'660169-1729','600112-1390','590515-3290','550609-1420','471289-2569','650387-1399','560113-0480','560793-2199',
'550405-0400','571214-0240','451115-1460','510515-1020','440417-0510']

vendorname = 'Samskip'
Write_sendingar_data(arr,SAM_kennitolur,vendorname,Sendingar,f,all_sendingar)


#test
print(all_sendingar)

for i in range(1,Sendingar):
	if i not in all_sendingar:
		rest_sendingar.append(i)

print(rest_sendingar)
'''
#----------------------------------------------------------------------
#Bannlisti & Fixlisti
#----------------------------------------------------------------------
f.write("set Bannlisti := \r\n")

f.write(";\r\n")

#s,t,d
Start_day = int(arr[0][2][:2])
f.write("set Fixlisti := \r\n")


for i in range(1,Sendingar+1):
	day = int(arr[i][2][:2].strip())-Start_day+1
	slot_vendor_data = []
	if arr[i][6].strip() == '420369-7789':
		slot = 1
	elif arr[i][6].strip() == '470169-1419':
		slot = 2
	elif arr[i][6].strip() == '570169-0339':
		slot = 3
	elif arr[i][6].strip() == '700103-3660':
		slot = 3
	elif arr[i][6].strip() == '541205-1520':
		slot = 4
	elif arr[i][6].strip() == '410999-2859':
		slot = 4
	elif arr[i][6].strip() == '530303-2410':
		slot = 5
	elif arr[i][6].strip() == '550595-2579':
		slot = 6
	elif arr[i][6].strip() in ["601083-0789","470105-2240","490104-2160","450310-0500","491007-1680","511105-1290","601289-1489","470302-4290","640485-0949","420178-0349","531212-0530","451205-0560","470706-1040","451295-2929","530206-0330","620509-0190","470205-0400"]:
		slot = 7
	else:
		slot = 8

	f.write("{} {} {} \r\n".format(i,slot,day))

f.write(";\r\n")

f.write("end;\r\n")

#counter = 0
#newArr = [2]
#dags = []
#arr = list(dict.fromkeys(arr))
#for i in range(1, len(arr)):

	
	#print('Printing each date only the first number: ', int(arr[counter][2][0:2]))

	#if(arr[counter][2][3:4] == '02'):
		#if((int(arr[counter+1][2][0:2]) !> int(arr[coun))

	#elif(arr[counter][2][3:4] == '04' or arr[counter][2][3:4] == '06' or arr[counter][2][3:4] == '09' or arr[counter][2][3:4] == '11'):

	#else


	#if(int(arr[counter+1][2][0:2]) !> int(arr[counter][2][0:2])+1):
		#newArr.append(arr[counter][2][0:2])



	#dags.append(arr[counter][2])
	#counter = counter + 1
	#print(arr)		


#dags2 = (set(dags))

#dags3 = sorted(dags2, key=lambda x: datetime.strptime(x, "%d/%m/%Y").strftime("%Y-%m-%d"))
print(arr)
print(selectstring)

		








