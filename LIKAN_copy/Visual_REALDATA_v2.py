import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import collections

import psycopg2
from Select_function import Select_string

#Connection to SQL
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
#Carefull !!!!, not hardcoded anymore
#------------------------------------------------

#Find places to start and end for alag <------------
alag_start = 0
for line in data: 
	alag_start = alag_start + 1
	if line.strip() == 'param A :=':
		break
print(alag_start)

alag_end = alag_start
for line in data[alag_start:]: 
	if line.strip() == ';':
		break
	alag_end = alag_end + 1
print(alag_end)

#------------------
#create alag
for i in data[alag_start:alag_end]:
	i.strip()
	#key = i[0] + i[1]
	key = i[0:i.find(' ')]

	alag[int(key)] = [float(i[i.find(' '):])]

print('------')
print(i)
print(i.find(' '))


#-------------------
#Find places to start and end for target
target_start = 0
for line in data: 
	target_start = target_start + 1
	if line.strip() == 'param Ttarget :=':
		break
print(target_start)

target_end = target_start
for line in data[target_start:]: 
	if line.strip() == ';':
		break
	target_end = target_end + 1
print(target_end)

#-------------------------
#create target
for i in data[target_start:target_end]: 
	#print(i)
	key = i[0] + i[2]
	target[int(key)] = [int(i[i.find(' ',2):].strip())]
print(i)
print(i[i.find(' ',2):].strip())

print('Target: {}'.format(target))


#------------------------------------------------
#Done loading Data
#------------------------------------------------

#Create select_data and lausn

selectstring = Select_string()
cursor.execute(selectstring)
arr = cursor.fetchall()

select_data = {}
print ('\nShow me the databases:\n')
count = 1
for x in arr:
	select_data[count] = [x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]]
	count = count + 1

fjoldiSendinga = count - 1;

print('------',fjoldiSendinga)

#----------------
#fá annarsstaðar frá
dagar = 5
timeslott = 8


#CREATE MANNAMAL
#-------------------------------
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
				f.write('Dagur {} í tímaslotti {}. Er sending {} er með ID: {} frá Vendor: {} með kennitölu {} \n'.format(x[3],x[2],i,select_data[i][0],select_data[i][7],select_data[i][6]))
				f.write('Sendingin inniheldur {} stykki af {} með álagsvalue {} sem gerir álagið = {} \n'.format(select_data[i][3],select_data[i][8],select_data[i][4],(round(select_data[i][3]*select_data[i][4]))))
f.close()




#Create Lausn_for_print dictonary -------------------------
Lausn_for_print = {}
for i in lausn: 
	#Create Lausn_for_print dictonary = slot [alag_sum, fjoldi_sendinga]
	counter = 0;
	alag_sum = 0;
	for x in range(0,len(lausn[i])):
		alag_sum = alag_sum + alag[float(lausn[i][x][1])][0]
		counter = counter + 1

	Lausn_for_print[i] = [alag_sum,counter]


## -----------------------------------------------------------------
#print
## -----------------------------------------------------------------

#Determine the color
Z = np.random.rand(4, 5)
A = []
for i in range(0,timeslott):
	A.append([0.1, 0.2, 0.3, 0.4, 0.5])

print('This is A')
print(A)

## -----------------------------------------------------------------
#PLOT
## -----------------------------------------------------------------
plt.subplots(1, 1)

c = plt.pcolor(A, edgecolors='k', linewidths=3)
plt.title('Stundatafla')
plt.ylabel('Time')
plt.xlabel('Date')

plt.xticks(np.arange(dagar),['M', 'T', 'W', 'T', 'F', 'S', 'S'])
plt.yticks(np.arange(timeslott+1),['8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00', '16:00'])

#Print the solution for each slot
for i in lausn:
	#print the Target
	mainstring = 'Target: {}'
	#target[int(i)][0]
	plt.text(float(int(i[1]))-0.5, float(int(i[0]))-0.3,mainstring.format(target[int(i)][0]), size=5,
			ha="center", va="bottom",
			bbox=dict(boxstyle="square",ec=(0.1, 0.5, 0.5)))
	

for i in Lausn_for_print:
		insertstring = 'Fjöldi sendinga: {} \n Alag: {} '
		#alag[lausn[i][x][1]][0]
		plt.text(float(int(i[1]))-0.5, float(int(i[0]))-0.8,insertstring.format(Lausn_for_print[i][1],Lausn_for_print[i][0]), size=5,
	         ha="center", va="bottom",
	         bbox=dict(boxstyle="square",ec=(0.1, 0.5, 0.9))
	         )
	

plt.show()

