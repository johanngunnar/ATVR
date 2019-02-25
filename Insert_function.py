def insert_function(data):

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


	# Write the lines 
	insertstring = "insert into item_category (name, tegund, Timevalue) values ('{}','{}',{});\n"

	for d in data:
	    cursor.execute(insertstring.format(d,data[d][0],data[d][1]))

	conn.commit()

	cursor.close()
	conn.close()