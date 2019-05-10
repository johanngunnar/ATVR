
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

selectstring = "Select inn.ItemNo,i.Tegund,i.Description, inn.Qty_perUnit, inn.Quantity, inn.Total_Qty, inn.Date, i.MilliL, i.Timevalue,round(i.Timevalue*inn.Quantity) Alag from Innstreymi inn, Item i where inn.ItemNo = i.id and inn.Date in('12/02/2018')"
cursor.execute(selectstring)
arr = cursor.fetchall()

conn.commit()
cursor.close()
conn.close()


for i in arr:
	print(i)
