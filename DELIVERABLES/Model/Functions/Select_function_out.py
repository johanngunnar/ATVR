import datetime
import psycopg2
import operator
def Select_string_OUT():

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


	selectstring = "Select u.Ship_Code,u.Destination, sum(u.Quantity*c.Timevalue), u.date, count(u.Total_Qty) from Utstreymi u, Item_Category c, Item i where u.ItemNo = i.id and i.tegund = c.name and u.date in('12/02/2018','13/02/2018','14/02/2018','15/02/2018','16/02/2018') group by u.Ship_Code , u.date, u.Destination order by u.Ship_Code "

	return selectstring