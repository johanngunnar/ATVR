
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

selectstring = "Select inn.ItemNo,i.Tegund,i.Description, inn.Qty_perUnit, inn.Quantity, inn.Total_Qty, inn.Date, i.MilliL, i.Timevalue,round(i.Timevalue*inn.Quantity) Alag,i.Timevalue_Liter  from Innstreymi inn, Item i where inn.ItemNo = i.id and inn.Date in('16/02/2018')"
cursor.execute(selectstring)
arr = cursor.fetchall()

conn.commit()
cursor.close()
conn.close()

#inn.ItemNo,i.Tegund,i.Description, inn.Qty_perUnit, inn.Quantity, inn.Total_Qty, inn.Date, i.MilliL, i.Timevalue,round(i.Timevalue*inn.Quantity) Alag ,.Timevalue_Liter
counter = 0
Litrar = 0
LitraAlag = 0
Kassar = 0
KassaAlag = 0
for i in arr:
	
	KassaAlag = KassaAlag + i[9]
	Kassar = Kassar + i[4]

	curr_litrar = ((i[5]*i[7])/1000)
	Litrar = Litrar + curr_litrar
	LitraAlag = LitraAlag + curr_litrar*i[10]
	counter = counter +1

print('Sending fyrir {} -----------'.format(arr[2][6]))
print('Fjöldi sendingar: {} Litrar: {} LitraALag: {} Kassar: {}  KassaAlag:  {}'.format(counter,round(Litrar),round(LitraAlag),Kassar,round(KassaAlag)))




