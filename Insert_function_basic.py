def insert_function_basic(data):

	insertstring = "insert into item_category (name, tegund) values ('{}','{}');\n"

	#Create the file
	f = open('insert_commands.ItemCAT.sql', 'w')
	for x in data:
		#Correct string
	    f.write(insertstring.format(x, data[x]))
	f.close()