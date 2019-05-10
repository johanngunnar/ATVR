import psycopg2
def Write_sendingar_data(arr,kenntolur,vendorname,Sendingar,f,all_sendingar):
	f.write("set {} := \r\n".format(vendorname))
	for i in range(0,Sendingar):
		for x in range(0,len(kenntolur)):
			if arr[i][6].strip() == kenntolur[x].strip():
				if i != 0:
					all_sendingar.append(i)
					f.write("{} \n".format(i))
	f.write(";\r\n")