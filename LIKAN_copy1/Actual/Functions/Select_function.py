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
	for i in range(3 +((vikunumer-1)*5),3+5*vikunumer):
		if i == 3+((vikunumer-1)*5):
			strengurinn_minn = "'"+select_data[i]+"'"
		else:
			strengurinn_minn = strengurinn_minn + ','+ "'"+select_data[i]+"'"

	#'12/02/2018','13/02/2018','14/02/2018','15/02/2018','16/02/2018'

	selectstring = "select s.id,s.SourceNo, s.date, vi.Quantity, c.Timevalue, c.tegund,i.Vendor,i.Vendor_name,i.description from sending s, Item_Category c,item i,vinnsla vi where c.name = i.Tegund and s.ItemNo = i.id and vi.itemno = i.id and s.RE_number = vi.Document_ID1 and s.date in({}) order by s.id".format(strengurinn_minn)

	return selectstring