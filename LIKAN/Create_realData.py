import psycopg2

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

selectstring = " select s.id,s.SourceNo, s.date, vi.Quantity, c.Timevalue, c.tegund,i.Vendor from sending s, Item_Category c,item i,vinnsla vi where c.name = i.Tegund and s.ItemNo = i.id and vi.itemno = i.id and s.RE_number = vi.Document_ID1 and s.date in('09/02/2018','10/02/2018','11/02/2018','12/02/2018') order by s.id"

cursor.execute(selectstring)
arr = cursor.fetchall()

print ('\nShow me the databases:\n')
count = 0
for x in arr:
	print(x)
	count = count + 1
    

print(count)

#----------------------------------------------------------------------------
# Create data file
#----------------------------------------------------------------------------

f= open("demo_data_real.txt","w+")

Days = 5
Timeslots = 4
Sendingar = 60

f.write("param S := {};\r\n".format(Sendingar))
f.write("param T := {};\r\n".format(Timeslots))
f.write("param D := {};\r\n".format(Days))
f.write("param windowsize := {};\r\n".format(0))
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

#Write the ALAG
f.write("param A := \r\n")
for i in range(0,Sendingar):
	f.write("{} {}\r\n".format(i+1,round(arr[i][4]*arr[i][3])))   #timevalue * Qty
f.write(";\r\n")
f.write("\r\n")

#Write the TARGET
f.write("param Ttarget := \r\n")

for i in range(1,Days+1):
	for x in range(1,Timeslots+1):
		if x in (1,2):
			f.write("{} {} {}\r\n".format(x,i,150))
		if x in (3,4):
			f.write("{} {} {}\r\n".format(x,i,50))
f.write(";\r\n")
f.write("\r\n")


f.write("set Bannlisti := \r\n")

f.write(";\r\n")


f.write("set Fixlisti := \r\n")

f.write(";\r\n")

f.write("end;\r\n")
