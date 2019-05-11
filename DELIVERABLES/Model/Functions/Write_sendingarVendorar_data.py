import psycopg2
def Write_sendingar_data(arr,kenntolur,vendorname,Sendingar,f,all_sendingar):
	f.write("set {} := \r\n".format(vendorname))
	counter = 0
	for i in arr:
		counter = counter + 1
		for x in kenntolur:
			if i[6].strip() == x.strip():
				all_sendingar.append(counter)
				f.write("{} \n".format(counter))
	f.write(";\r\n")
	'''
	for i in range(0,Sendingar):
		for x in range(0,len(kenntolur)):
			if arr[i][6].strip() == kenntolur[x].strip():
				#if i != 0:
					all_sendingar.append(i)
					f.write("{} \n".format(i))
	f.write(";\r\n")
	'''