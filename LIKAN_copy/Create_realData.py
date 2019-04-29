import psycopg2

from Select_function import Select_string

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

print ('\nShow me the databases:\n')
fjoldiSendinga = 0
for x in arr:
	print('-----------',x)
	fjoldiSendinga = fjoldiSendinga + 1
    

print(fjoldiSendinga)

#----------------------------------------------------------------------------
# Create data file
#----------------------------------------------------------------------------

f= open("demo_data_real.txt","w+")

Days = 5
Timeslots = 8
Sendingar = fjoldiSendinga
windowsize = 0

f.write("param S := {};\r\n".format(Sendingar))
f.write("param T := {};\r\n".format(Timeslots))
f.write("param D := {};\r\n".format(Days))
f.write("param windowsize := {};\r\n".format(windowsize))
f.write("\r\n")

#Create S numbers
'''
f.write("set S :=\r\n")
for i in range(0,Sendingar):
	f.write("{}\r\n".format(arr[i][0]))
f.write(";\r\n")
f.write("\r\n")
'''
print('timevalue', arr[1][4])
print('Qty', arr[1][3])

#Write the ALAG & CREATE the sequence i
f.write("param A := \r\n")
for i in range(0,Sendingar):
	f.write("{} {}\r\n".format(i+1,round(arr[i][4]*arr[i][3])))   #timevalue * Qty
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


f.write("set Bannlisti := \r\n")

f.write(";\r\n")


f.write("set Fixlisti := \r\n")

f.write(";\r\n")

#CREATE list of Ölgerðin kenntölur
Ol_kennitolur = ['420369-7789']

f.write("set Olgerdin := \r\n")

for i in range(0,Sendingar):
	for x in range(0,len(Ol_kennitolur)):
		if arr[i][6] == Ol_kennitolur[x]:
			f.write("{} \n".format(i))


f.write(";\r\n")


f.write("end;\r\n")
