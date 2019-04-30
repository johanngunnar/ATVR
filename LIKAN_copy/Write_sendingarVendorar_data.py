import psycopg2
def Write_sendingar_data(arr,kenntolur,vendorname,Sendingar,f):
	f.write("set {} := \r\n".format(vendorname))
	for i in range(0,Sendingar):
		for x in range(0,len(kenntolur)):
			if arr[i][6].strip() == kenntolur[x].strip():
				f.write("{} \n".format(i))
	f.write(";\r\n")