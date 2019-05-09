
import datetime
import psycopg2
import operator
# ------------------------------------------------
# Connection to SQL
# ------------------------------------------------
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

# ------------------------------------------------
# 
# ------------------------------------------------
selectstring = "Select Distinct i.date from innstreymi i " # call to SQL data base
cursor.execute(selectstring)
arr = cursor.fetchall()

select_data = []
count = 0
for i in arr:
	print(i)
	select_data.append([int(i[0][0:2]),int(i[0][3:5]),int(i[0][6:])])
	count = count +1 

select_data = sorted(select_data, key=operator.itemgetter(0))
select_data = sorted(select_data, key=operator.itemgetter(1))
select_data = sorted(select_data, key=operator.itemgetter(2))

for i in range(0,len(select_data)):
		if len(str(select_data[i][1])) == 1:
			select_data[i] = '{}/0{}/{}'.format(select_data[i][0],select_data[i][1],select_data[i][2])
		else:
			select_data[i] = '{}/{}/{}'.format(select_data[i][0],select_data[i][1],select_data[i][2])

strengurinn_minn = ''
for i in range(3,3+5):
	if i == 3:
		strengurinn_minn = "'"+select_data[i]+"'"
	else:
		strengurinn_minn = strengurinn_minn + ','+ "'"+select_data[i]+"'"



print(select_data)
print('---')
print(count)
print(strengurinn_minn)


