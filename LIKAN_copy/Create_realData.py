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

selectstring = Select_string()

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
EIM_kennitolur = []
vendorname = 'Eimskip'
Write_sendingar_data(arr,EIM_kennitolur,vendorname,Sendingar,f,rest_sendingar)

SAM_kennitolur = []
vendorname = 'Samskip'
Write_sendingar_data(arr,SAM_kennitolur,vendorname,Sendingar,f,rest_sendingar)

print(all_sendingar)
print(rest_sendingar)

#----------------------------------------------------------------------
#Bannlisti & Fixlisti
#----------------------------------------------------------------------
f.write("set Bannlisti := \r\n")

f.write(";\r\n")

f.write("set Fixlisti := \r\n")

f.write(";\r\n")

f.write("end;\r\n")
