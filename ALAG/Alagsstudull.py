
import psycopg2
import math
import matplotlib.pyplot as plt
import numpy as np

def Create_alag(tegund_nafn):

	#----------------------------------------------------------------------------
	#Connection to SQL
	#----------------------------------------------------------------------------
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


	#----------------------------------------------------------------------------
	# Write the select Q & OPEN
	#----------------------------------------------------------------------------

	selectstring = " select s.SourceNo,c.tegund, vi.Document_ID1, vi.UserID, vi.Quantity, vi.Qty_perUnit, vi.picked, vi.Picked_Unit, vi.Date_Scanned,s.RE_number, s.Shelf, i.Vendor, i.Description, i.id from vinnsla vi, sending s, item i, Item_Category c where vi.itemno = i.id and s.ItemNo = i.id and s.RE_number = vi.Document_ID1 and c.name = i.Tegund and vi.Date_Scanned like ('%03/2018%') order by (vi.Date_Scanned, vi.Picked)"

	cursor.execute(selectstring)
	arr = cursor.fetchall()

	selectstring2 = "select inn.sending, c.tegund, vi.Document_ID1, vi.UserID, vi.Quantity, vi.Qty_perUnit, vi.picked, vi.Picked_Unit, vi.Date_Scanned, i.Vendor, i.Description, i.id from vinnsla vi, Innstreymi inn, item i, Item_Category c where vi.itemno = i.id and inn.ItemNo = i.id and inn.put = vi.Document_ID1 and c.name = i.Tegund and vi.Date_Scanned like ('%03/2018%') order by (vi.Date_Scanned, vi.Picked)"
	cursor.execute(selectstring2)
	record = cursor.fetchall()

	#----------------------------------------------------------------------------
	# Dictornary lykill count, frá 2 select skipunum
	#----------------------------------------------------------------------------

	Lagerbjor_arr = []
	Lagerbjor_record = []
	Lagerbjor_dict = {}
	alag_per_sendingu_min = 0

	inn_i_kerfi = 0
	upp_i_hillu = 0

	counter = 0
	currcount= 0

	for x in arr:
		if x[1] == tegund_nafn:
			print(x[1],x[13],x[12],x[6],x[8],x[4],x[0])
			print(counter)
			counter = counter + 1
			print(x[0])

		for i in record:
			#SendingarID & Item_no (tegund) & Quantity
			if x[0] == i[0] and i[11] == x[13] and i[4] == x[4]:
				if x[1] == tegund_nafn:
					inn_i_kerfi = (int(x[6][0:2])*60 + int(x[6][3:5]))
					upp_i_hillu = (int(i[6][0:2])*60 + int(i[6][3:5]))
					#inn_i_kerfi_date = 
					alag_per_sendingu_min = (upp_i_hillu - inn_i_kerfi)
					Lagerbjor_dict[currcount] = [x[0],x[1],'Sending:',x[6],x[8],'Innstreymi:',i[6],i[8], 'Description:',i[11] ,i[10],x[12],'Álag i min :', alag_per_sendingu_min, 'Quantity of packs',x[4], 'Liters']
					currcount = currcount + 1

	for i in Lagerbjor_dict:
		print('{}, {}'.format(i, Lagerbjor_dict[i]))


	#----------------------------------------------------------------------------
	# Look at alag by finding a average
	#----------------------------------------------------------------------------

	lagerbjor_alag_total = 0
	lagerbjor_count = 0
	lagerbjor_packs_total = 0
	for i in range(0,len(Lagerbjor_dict)):
		lagerbjor_alag_total = (lagerbjor_alag_total + Lagerbjor_dict[i][13])
		lagerbjor_count = lagerbjor_count + 1
		lagerbjor_packs_total = (lagerbjor_packs_total + Lagerbjor_dict[i][15])


	#-----------------------
	# Closing the select Q
	#-----------------------
	conn.commit()
	cursor.close(
		)
	conn.close()

	#----------------------------------------------------------------------------
	# Check to see what is happening in the RUN
	#----------------------------------------------------------------------------

	if lagerbjor_alag_total == 0:
		return 1
	else:
		medal_alag_a_kassa = lagerbjor_alag_total/lagerbjor_packs_total
		print('Svo álagið er: {:.2f} per hreyfingu af {} '.format(lagerbjor_alag_total/lagerbjor_count,tegund_nafn))
		print('Heildarfjöldi pakka: {} .. Meðfjöldi kassa á Put RE línu: {:.2f} .. Meðal álag á kassa: {:.4f} '.format(lagerbjor_packs_total,(lagerbjor_packs_total/lagerbjor_count),lagerbjor_alag_total/ lagerbjor_packs_total))
		return medal_alag_a_kassa

