import psycopg2
def Write_vendor_data(slot,vendor,timeslots,f):
		f.write("param {} := \r\n".format(vendor))
		for i in range(1,timeslots+1):
			if i == slot:
				f.write("{} {}\r\n".format(i,1))
			else:
				f.write("{} {}\r\n".format(i,0))
		f.write(";\r\n")
		f.write("\r\n")