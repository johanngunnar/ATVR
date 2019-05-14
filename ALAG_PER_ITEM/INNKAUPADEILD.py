
import psycopg2
#----------------------------------------------------------------------------
#Connection to SQL
#----------------------------------------------------------------------------
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
# Write the select Q & OPEN
#----------------------------------------------------------------------------
date = '28/02/2018'
selectstring = "Select inn.ItemNo,i.Tegund,i.Description, inn.Qty_perUnit, inn.Quantity, inn.Total_Qty, inn.Date, i.MilliL, i.Timevalue,(i.Timevalue*inn.Quantity) Alag,i.Timevalue_Liter ,(i.Timevalue_Liter*i.MilliL*inn.Total_Qty)/1000 ALAG_liter from Innstreymi inn, Item i where inn.ItemNo = i.id and inn.Date in('{}')".format(date)
cursor.execute(selectstring)
arr = cursor.fetchall()

conn.commit()
cursor.close()
conn.close()

#selectstring = "Select inn.ItemNo,i.Tegund,i.Description, inn.Qty_perUnit, inn.Quantity, inn.Total_Qty, inn.Date, i.MilliL, i.Timevalue,(i.Timevalue*inn.Quantity) Alag,i.Timevalue_Liter ,(i.Timevalue_Liter*i.MilliL) ALAG_liter
counter = 0
Litrar = 0
LitraAlag = 0
LitraAlag_test = 0
Kassar = 0
KassaAlag = 0
sendingar = []
for i in arr:
	
	KassaAlag = KassaAlag + i[9]
	Kassar = Kassar + i[4]

	curr_litrar = ((i[5]*i[7])/1000)
	Litrar = Litrar + curr_litrar
	LitraAlag = LitraAlag + curr_litrar*i[10]
	LitraAlag_test = LitraAlag_test + i[11]
	counter = counter +1
	sendingar.append(i)
	print(i)

max_liter_alag = 20965
max_kassa_alag = 20789

print('Sending fyrir {} -----------'.format(date))
print('Fjöldi sendingar: {} Litrar: {} LitraALag: {}  Kassar: {}  KassaAlag:  {}'.format(counter,round(Litrar),round(LitraAlag),Kassar,round(KassaAlag)))
print('Literprosenta: ({}/{})  Kassaprosenta: ({}/{}) '.format(round(LitraAlag/max_liter_alag*100,2),100,round(KassaAlag/max_kassa_alag*100,2),100))




