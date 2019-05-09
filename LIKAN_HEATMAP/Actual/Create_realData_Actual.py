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


#----------------------------------------------------------------------------
# Write the select Q
#----------------------------------------------------------------------------
for i in range(1,20):
	day_count = 1

	selectstring = Select_string(i)

	cursor.execute(selectstring)
	arr = cursor.fetchall()
	'''
	if(i == 1):
		arr.append([0, '', '17/02/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '18/02/2018', 0, 0, '', '', '', ''])
	if(i == 2):
		arr.append([0, '', '24/02/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '25/02/2018', 0, 0, '', '', '', ''])
	if(i == 3):
		arr.append([0, '', '04/03/2018', 0, 0, '', '', '', ''])
	if(i == 4):
		arr.append([0, '', '10/03/2018', 0, 0, '', '', '', ''])
	if(i == 5):
		arr.append([0, '', '17/03/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '18/03/2018', 0, 0, '', '', '', ''])
	if(i == 6):
		arr.append([0, '', '24/03/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '25/03/2018', 0, 0, '', '', '', ''])
	if(i == 7):
		arr.append([0, '', '30/03/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '31/03/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '01/04/2018', 0, 0, '', '', '', ''])
	if(i == 8):
		arr.append([0, '', '07/04/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '08/04/2018', 0, 0, '', '', '', ''])
	if(i == 9):
		arr.append([0, '', '14/04/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '15/04/2018', 0, 0, '', '', '', ''])
	if(i == 10):
		arr.append([0, '', '21/04/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '22/04/2018', 0, 0, '', '', '', ''])
	if(i == 11):
		arr.append([0, '', '28/04/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '29/04/2018', 0, 0, '', '', '', ''])
	if(i == 12):
		arr.append([0, '', '05/05/2018', 0, 0, '', '', '', ''])
	if(i == 13):
		arr.append([0, '', '12/05/2018', 0, 0, '', '', '', ''])
	if(i == 14):
		arr.append([0, '', '19/05/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '20/05/2018', 0, 0, '', '', '', ''])
	if(i == 15):
		arr.append([0, '', '26/05/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '27/05/2018', 0, 0, '', '', '', ''])
	if(i == 16):
		arr.append([0, '', '02/06/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '03/06/2018', 0, 0, '', '', '', ''])
	if(i == 18):
		arr.append([0, '', '16/06/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '17/06/2018', 0, 0, '', '', '', ''])
	if(i == 19):
		arr.append([0, '', '23/06/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '24/06/2018', 0, 0, '', '', '', ''])
	if(i == 20):
		arr.append([0, '', '30/06/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '01/07/2018', 0, 0, '', '', '', ''])
	if(i == 21):
		arr.append([0, '', '08/07/2018', 0, 0, '', '', '', ''])
	if(i == 22):
		arr.append([0, '', '14/07/2018', 0, 0, '', '', '', ''])
	if(i == 23):
		arr.append([0, '', '21/07/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '22/07/2018', 0, 0, '', '', '', ''])
	if(i == 25):
		arr.append([0, '', '04/08/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '05/08/2018', 0, 0, '', '', '', ''])
	if(i == 26):
		arr.append([0, '', '11/08/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '12/08/2018', 0, 0, '', '', '', ''])
	if(i == 27):
		arr.append([0, '', '18/08/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '19/08/2018', 0, 0, '', '', '', ''])
	if(i == 28):
		arr.append([0, '', '25/08/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '26/08/2018', 0, 0, '', '', '', ''])
	if(i == 29):
		arr.append([0, '', '01/09/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '02/09/2018', 0, 0, '', '', '', ''])
	if(i == 30):
		arr.append([0, '', '08/09/2018', 0, 0, '', '', '', ''])
	if(i == 31):
		arr.append([0, '', '15/09/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '16/09/2018', 0, 0, '', '', '', ''])
	if (i == 32):
		arr.append([0, '', '22/09/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '23/09/2018', 0, 0, '', '', '', ''])
	if(i == 33):
		arr.append([0, '', '29/09/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '30/09/2018', 0, 0, '', '', '', ''])
	if(i == 34):
		arr.append([0, '', '07/10/2018', 0, 0, '', '', '', ''])
	if(i == 35):
		arr.append([0, '', '13/10/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '14/10/2018', 0, 0, '', '', '', ''])
	if(i == 36):
		arr.append([0, '', '20/10/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '21/10/2018', 0, 0, '', '', '', ''])
	if(i == 37):
		arr.append([0, '', '27/10/2018', 0, 0, '', '', '', ''])
	if(i == 38):
		arr.append([0, '', '03/11/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '04/11/2018', 0, 0, '', '', '', ''])
	if(i == 39):
		arr.append([0, '', '17/11/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '18/11/2018', 0, 0, '', '', '', ''])
	if(i == 40):
		arr.append([0, '', '24/11/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '25/11/2018', 0, 0, '', '', '', ''])
	if(i == 41):
		arr.append([0, '', '02/12/2018', 0, 0, '', '', '', ''])
	if(i == 42):
		arr.append([0, '', '08/12/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '09/12/2018', 0, 0, '', '', '', ''])
	if(i == 43):
		arr.append([0, '', '16/12/2018', 0, 0, '', '', '', ''])
	if(i == 44):
		arr.append([0, '', '23/12/2018', 0, 0, '', '', '', ''])
	if(i == 45):
		arr.append([0, '', '25/12/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '29/12/2018', 0, 0, '', '', '', ''])
		arr.append([0, '', '30/12/2018', 0, 0, '', '', '', ''])
	if(i == 46):
		arr.append([0, '', '05/01/2019', 0, 0, '', '', '', ''])
		arr.append([0, '', '06/01/2019', 0, 0, '', '', '', ''])
	if(i == 47):
		arr.append([0, '', '12/01/2019', 0, 0, '', '', '', ''])
		arr.append([0, '', '13/01/2019', 0, 0, '', '', '', ''])
	if(i == 49):
		arr.append([0, '', '19/01/2019', 0, 0, '', '', '', ''])

	'''
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
	demo_data_real = "demo_data_real" + str(i) + ".txt"

	#START WRITING THE FILE
	f= open(demo_data_real,"w+")
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
	#----------------- JULLA CODE -------------	
	#----------------------------------------------------------------------



	#print(arr[:][2][2])
	#arr.sort(key=lambda arr: arr[2][6:9])
	#arr.sort(key=lambda arr: int(arr[2][4:5]))
	#arr.sort(key=lambda arr: arr[2][:2])
	#sorted(arr, lambda x: (degree(arr[2][3:4]), x[:2]))
	#arr.sort(key=lambda x: x[2][5:6])
	#arr.sort(key=lambda x: x[2][3:4])
	#arr.sort(key=lambda x: x[2][:2])
	#if(i == 1):
	#print("fixed listinn er BOOM ", arr)


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
	#print(arr)
	Start_day = int(arr[0][2][:2])
	f.write("set Fixlisti := \r\n")

	haesta_tala = arr[0][2][:2]
	heasta_man = arr[0][2][3:5]

	for i in range(1,Sendingar+1):
		#print("I am failing at the indexes: ", i,arr[i][2][:2], "and", )
		#print(i,arr[i][2][:2])
		#day = int(arr[i][2][:2].strip())-Start_day+1
		if int(haesta_tala.strip()) < int(arr[i][2][:2].strip()) and int(heasta_man.strip()) == int(arr[i][2][3:5].strip()):
			haesta_tala = arr[i][2][:2]
			heasta_man = arr[i][2][3:5]
			day_count = day_count + 1
		elif int(heasta_man.strip()) < int(arr[i][2][3:5].strip()):
			haesta_tala = arr[i][2][:2]
			heasta_man = arr[i][2][3:5]
			day_count = day_count + 1
		#print(arr[i-1][0:3])
		#print(arr[i][0:3])
		#print(day_count)
		#print(haesta_tala)
		#print(heasta_man)
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

		f.write("{} {} {} \r\n".format(i,slot,day_count))

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

		








