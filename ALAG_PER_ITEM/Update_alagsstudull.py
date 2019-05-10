import psycopg2
def update_function_alagsstudull(data):

	#------------------------------------------------------------------------------------------------------
	#This file creates "Update_alagsstudull.sql" ,
	#When you create that file go to your database and paste the data into the database
	#------------------------------------------------------------------------------------------------------
	'''
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
	update_string = "update Item SET timevalue = '{}' where id = {} \n"
	#update_string = "insert into sending (id,vinnslu_No,itemno,sending ,qty_perunit, quantity, total_qty,Date,Put) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}');\n"

	for d in data:
	    cursor.execute(update_string.format(data[d][0],d))

	conn.commit()

	cursor.close()
	conn.close()
	'''

	#THE BASIC METHOD -----------------------------------------
	update_string = "update Item SET timevalue = {} where id = {} \n"

	#Create the file
	f = open('Update_alagsstudull.sql', 'w')
	for d in data:
		#Correct string
	    f.write(update_string.format(data[d][0],d))

	f.close()
	
	