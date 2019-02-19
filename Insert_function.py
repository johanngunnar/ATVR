def insert_function(data):

	import psycopg2

	#Connection to SQL
	host = 'localhost'
	dbname = 'atvr'
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
	insertstring = "insert into item_category (name, tegund) values ('{}','{}');\n"

	for d in data:
	    cursor.execute(insertstring.format(d,data[d]))

	conn.commit()

	cursor.close()
	conn.close()