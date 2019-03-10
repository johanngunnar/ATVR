import psycopg2
def insert_function_innstreymi(data):

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


	# Write the lines 
	insertstring = "insert into innstreymi (id,vinnslu_No,itemno,sending ,qty_perunit, quantity, total_qty,Date,Put) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}');\n"

	for d in data:
	    cursor.execute(insertstring.format(d,data[d][0],data[d][1],data[d][2],data[d][3],data[d][4],data[d][5],data[d][6],data[d][7]))

	conn.commit()

	cursor.close()
	conn.close()
	'''

	#THE BASIC METHOD -----------------------------------------
	insertstring = "insert into innstreymi (id, itemno, qty_perunit, quantity, total_qty) values ('{}','{}','{}','{}','{}');\n"

	#Create the file
	f = open('insert_commands.innstreymi.sql', 'w')
	for d in data:
		#Correct string
	    f.write(insertstring.format(d,data[d][0],data[d][1],data[d][2],data[d][3]))
	f.close()
	'''