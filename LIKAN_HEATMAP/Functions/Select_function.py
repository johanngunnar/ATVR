import datetime
import psycopg2
import operator
def Select_string(vikunumer):

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


	arr.append(['17/02/2018'])
	arr.append(['18/02/2018'])
	
	arr.append(['24/02/2018'])
	arr.append(['25/02/2018'])
	
	arr.append(['04/03/2018'])	
	
	arr.append(['10/03/2018'])
	
	arr.append(['17/03/2018'])
	arr.append(['18/03/2018'])

	arr.append(['24/03/2018'])
	arr.append(['25/03/2018'])

	arr.append(['30/03/2018'])
	arr.append(['31/03/2018'])
	arr.append(['01/04/2018'])

	arr.append(['07/04/2018'])
	arr.append(['08/04/2018'])

	arr.append(['14/04/2018'])
	arr.append(['15/04/2018'])

	arr.append(['21/04/2018'])
	arr.append(['22/04/2018'])

	arr.append(['28/04/2018'])
	arr.append(['29/04/2018'])
	
	arr.append(['05/05/2018'])
	
	arr.append(['12/05/2018'])

	arr.append(['19/05/2018'])
	arr.append(['20/05/2018'])

	arr.append(['26/05/2018'])
	arr.append(['27/05/2018'])

	arr.append(['02/06/2018'])
	arr.append(['03/06/2018'])
	
	arr.append(['16/06/2018'])
	arr.append(['17/06/2018'])

	arr.append(['23/06/2018'])
	arr.append(['24/06/2018'])

	arr.append(['30/06/2018'])
	arr.append(['01/07/2018'])

	arr.append(['08/07/2018'])

	arr.append(['14/07/2018'])

	arr.append(['21/07/2018'])
	arr.append(['22/07/2018'])

	arr.append(['04/08/2018'])
	arr.append(['05/08/2018'])

	arr.append(['11/08/2018'])
	arr.append(['12/08/2018'])

	arr.append(['18/08/2018'])
	arr.append(['19/08/2018'])

	arr.append(['25/08/2018'])
	arr.append(['26/08/2018'])

	arr.append(['01/09/2018'])
	arr.append(['02/09/2018'])

	arr.append(['08/09/2018'])

	arr.append(['15/09/2018'])
	arr.append(['16/09/2018'])

	arr.append(['22/09/2018'])
	arr.append(['23/09/2018'])

	arr.append(['29/09/2018'])
	arr.append(['30/09/2018'])

	arr.append(['07/10/2018'])

	arr.append(['13/10/2018'])
	arr.append(['14/10/2018'])

	arr.append(['20/10/2018'])
	arr.append(['21/10/2018'])


	arr.append(['27/10/2018'])

	arr.append(['03/11/2018'])
	arr.append(['04/11/2018'])

	arr.append(['17/11/2018'])
	arr.append(['18/11/2018'])

	arr.append(['24/11/2018'])
	arr.append(['25/11/2018'])

	arr.append(['02/12/2018'])


	arr.append(['08/12/2018'])
	arr.append(['09/12/2018'])

	arr.append(['16/12/2018'])


	arr.append(['23/12/2018'])


	arr.append(['25/12/2018'])
	arr.append(['29/12/2018'])
	arr.append(['30/12/2018'])


	arr.append(['05/01/2019'])
	arr.append(['06/01/2019'])


	arr.append(['12/01/2019'])
	arr.append(['13/01/2019'])


	arr.append(['19/01/2019'])
	
	select_data = []
	count = 0
	for i in arr:
		select_data.append([int(i[0][0:2]),int(i[0][3:5]),int(i[0][6:])])
		count = count +1 

	select_data = sorted(select_data, key=operator.itemgetter(0))
	select_data = sorted(select_data, key=operator.itemgetter(1))
	select_data = sorted(select_data, key=operator.itemgetter(2))

	for i in range(0,len(select_data)):
		if len(str(select_data[i][1])) == 1 and len(str(select_data[i][0])) == 2:
			select_data[i] = '{}/0{}/{}'.format(select_data[i][0],select_data[i][1],select_data[i][2])
		elif len(str(select_data[i][1])) == 2 and len(str(select_data[i][0])) == 1:
			select_data[i] = '0{}/{}/{}'.format(select_data[i][0],select_data[i][1],select_data[i][2])
		elif len(str(select_data[i][1])) == 1 and len(str(select_data[i][0])) == 1:
			select_data[i] = '0{}/0{}/{}'.format(select_data[i][0],select_data[i][1],select_data[i][2])
		else:
			select_data[i] = '{}/{}/{}'.format(select_data[i][0],select_data[i][1],select_data[i][2])

	# ------------------------------------------------
	# Create the perfect String
	# ------------------------------------------------

	strengurinn_minn = ''
	nedrimork = 3 +((vikunumer-1)*5)+(vikunumer-1)*2
	efrimork = 3+5*vikunumer+(vikunumer-1)*2
	for j in range(nedrimork,efrimork):
		if j == nedrimork:
			strengurinn_minn = "'"+select_data[j]+"'"
		else:
			strengurinn_minn = strengurinn_minn + ','+ "'"+select_data[j]+"'"


	#'12/02/2018','13/02/2018','14/02/2018','15/02/2018','16/02/2018'


	selectstring = "select s.id,s.SourceNo, s.date, vi.Quantity, c.Timevalue, c.tegund,i.Vendor,i.Vendor_name,i.description from sending s, Item_Category c,item i,vinnsla vi where c.name = i.Tegund and s.ItemNo = i.id and vi.itemno = i.id and s.RE_number = vi.Document_ID1 and s.date in({}) order by s.id".format(strengurinn_minn)

	return selectstring