
import psycopg2
import math
# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

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

selectstring = " select s.SourceNo,c.tegund, vi.Document_ID1, vi.UserID, vi.Quantity, vi.Qty_perUnit, vi.picked, vi.Picked_Unit,s.date,s.RE_number, s.Shelf, i.Vendor, i.Description, i.id from vinnsla vi, sending s, item i, Item_Category c where vi.itemno = i.id and s.ItemNo = i.id and s.RE_number = vi.Document_ID1 and c.name = i.Tegund and s.date in('09/02/2018','12/02/2018','13/02/2018','14/02/2018','15/02/2018','16/02/2018') order by vi.Picked"

cursor.execute(selectstring)
arr = cursor.fetchall()

selectstring2 = "select inn.sending, c.tegund, vi.Document_ID1, vi.UserID, vi.Quantity, vi.Qty_perUnit, vi.picked, vi.Picked_Unit,inn.date, i.Vendor, i.Description, i.id from vinnsla vi, Innstreymi inn, item i, Item_Category c where vi.itemno = i.id and inn.ItemNo = i.id and inn.put = vi.Document_ID1 and c.name = i.Tegund and inn.date in('12/02/2018','13/02/2018','14/02/2018','15/02/2018','16/02/2018') order by vi.Picked"
cursor.execute(selectstring2)
record = cursor.fetchall()

#1 Ölgerðin (edi) ,2 Coca-Cola (edi),3  Globus (edi), Vín tríó, 4 Brugghús Steðja, Dista , 5 Bakkus (edi), 6 Mekka (edi)
#slot_dict = {'420369-7789':0,'550595-2579':0,'580483-0709':1,'470169-1419':1,'700103-3660':2,'570169-0339':2,'410999-2859':3,'530303-2410':4,'550595-2579':5}

print ('\nShow me the databases:\n')
for x in arr:
    print(x)

#----------------------------------------------------------------------------
# Dictornary lykill kennitala, value index
#----------------------------------------------------------------------------

Lagerbjor_arr = []
Lagerbjor_record = []
Lagerbjor_dict = {}

for x in arr[:10]:
	for i in record:

		if x[0] == i[0] and i[11] == x[13] and i[4] == x[4]:
			if x[1] == 'Lagerbjór':
				Lagerbjor_arr.append(x[6])
				Lagerbjor_dict[x[0]] = [x[1],'Sending:',x[6],x[8],'Innstreymi:',i[6],i[8], 'Description:', i[10],x[12]]


print('line ------------------------------------------------------------------------')
for i in record:
	if i[1] == 'Lagerbjór':
		Lagerbjor_record.append(i[6])



print(Lagerbjor_arr)
print(Lagerbjor_record)
print('line ------------------------------------------------------------------------')
print(Lagerbjor_dict)


conn.commit()
cursor.close()
conn.close()

