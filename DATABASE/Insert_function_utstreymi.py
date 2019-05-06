import psycopg2
def insert_function_utstreymi(data):
	

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
	insertstring = "insert into utstreymi (id, Ship_Code, destination, itemno, qty_perunit, quantity, total_qty, millL_PUnit, liter, date) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');\n"

	for d in data:
	    cursor.execute(insertstring.format(d,data[d][0],data[d][1],data[d][2],data[d][3],data[d][4],data[d][5],data[d][6],data[d][7],data[d][8]))

	conn.commit()

	cursor.close()
	conn.close()
	'''
	
	#THE BASIC METHOD -----------------------------------------
	insertstring = "insert into utstreymi (id, destination, itemno, qty_perunit, quantity, total_qty, millL_PUnit, liter) values ('{}','{}','{}','{}','{}','{}','{}','{}');\n"
	#Create the file
	f = open('insert_commands.utstreymi.sql', 'w')
	for d in data:
		#Correct string
	    f.write(insertstring.format(d,data[d][0],data[d][1],data[d][2],data[d][3],data[d][4],data[d][5],data[d][6]))
	f.close()
	'''