import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import collections
import matplotlib.colors

import psycopg2
from Select_function import Select_string

#------------------------------------------------
#Connection to SQL
#------------------------------------------------
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

#------------------------------------------------
#Load solution data and demo_data
results = []
with open('solution.sol') as inputfile:
    for line in inputfile:
        results.append(line.strip().replace(')',' ').replace('(',' ').replace(',',' ').split())

data = []
alag = {}
target = {}
with open('demo_data_real.txt') as inputfile:
    for line in inputfile:
        data.append(line)
#------------------------------------------------



#FIX FOR HARDCODE
#------------------------------------------------
#Find places to start and end for alag 
#------------------------------------------------
alag_start = 0
for line in data: 
	alag_start = alag_start + 1
	if line.strip() == 'param A :=':
		break

alag_end = alag_start
for line in data[alag_start:]: 
	if line.strip() == ';':
		break
	alag_end = alag_end + 1

#------------------
#Create alag
#------------------   ALAG ER HUGSA– VITLAUST SKO–A A MRG
for i in data[alag_start:alag_end]:
	i.strip()
	key = i[0:i.find(' ')]
	alag[int(key)] = [float(i[i.find(' '):])]

print(alag)


#------------------------------------------------
#Find places to start and end for target
#------------------------------------------------
target_start = 0
for line in data: 
	target_start = target_start + 1
	if line.strip() == 'param Ttarget :=':
		break

target_end = target_start
for line in data[target_start:]: 
	if line.strip() == ';':
		break
	target_end = target_end + 1

#------------------
#Create target
#-------------------
for i in data[target_start:target_end]: 
	key = i[0] + i[2]
	target[int(key)] = [int(i[i.find(' ',2):].strip())]

#------------------------------------------------
#Done loading Data
#------------------------------------------------



#-------------------------------
#Create select_data and lausn
#-------------------------------

selectstring = Select_string()   #call to SQL data base
cursor.execute(selectstring)
arr = cursor.fetchall()

select_data = {}
count = 0
for x in arr:
	select_data[count] = [x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]]
	count = count + 1

# Determine 3 values   HARDCODE !!!!!!!!!!!!!!!!!!!
fjoldiSendinga = count - 1;
dagar = 5
timeslott = 8

#---------------------------------
#CREATE MANNAMAL
#---------------------------------
f= open("lausn_mannamal.txt","w+")
lausn = {}
for x in results[(dagar*timeslott+3):(fjoldiSendinga*dagar*timeslott)+(dagar*timeslott+3)]:
	seperator = ''
	if int(x[4]) == 1:  #lausn
		seperator = ''
		key = seperator.join(x[2:4])
		if key not in lausn:
			lausn[key] = []
		lausn[key].append(x)

		#meira ef lausn  -- Write the solution
		for i in select_data:
			if int(x[1]) == i:
				f.write('Dagur {} Ì tÌmaslotti {}. Er sending {} er me ID: {} fr· Vendor: {} me kennitˆlu {} \n'.format(x[3],x[2],i,select_data[i][0],select_data[i][7],select_data[i][6]))
				f.write('Sendingin inniheldur {} stykki af {} me ·lagsvalue {} sem gerir ·lagi = {} \n'.format(select_data[i][3],select_data[i][8],select_data[i][4],(round(select_data[i][3]*select_data[i][4]))))
f.close()


f= open("mannamal_basic.txt","w+")
for x in results[(dagar*timeslott+3):(fjoldiSendinga*dagar*timeslott)+(dagar*timeslott+3)]:
	seperator = ''
	if int(x[4]) == 1:  #lausn
		for i in select_data:
			if int(x[1]) == i:
				f.write('Dagur {} Ì tÌmaslotti {}. Er sending {} er me ID: {} fr· Vendor {} A: {} \n'.format(x[3],x[2],i,select_data[i][0],select_data[i][6],round(select_data[i][3]*select_data[i][4])))