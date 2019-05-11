
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

selectstring = "select i.id,i.Timevalue,i.Timevalue_LITER from item i order by i.id"
cursor.execute(selectstring)
arr = cursor.fetchall()

conn.commit()
cursor.close()
conn.close()





#----------------------------------------------------------------------------
# 
#----------------------------------------------------------------------------

f = open("fileforinnkaup.txt", "w+")
for i in arr:
	f.write('{} {} {} \n'.format(i[0],i[1],i[2]))

f.close()



