import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import collections
import matplotlib.colors

import psycopg2
from Functions.Select_function import Select_string
from Functions.Select_function_out import Select_string_OUT
# ------------------------------------------------
# HARDCODE
# ------------------------------------------------
dagar = 5
timeslott = 8
vikunumer = 1

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
# Load solution data and demo_data
# ------------------------------------------------
results = []
with open('solution.sol') as inputfile:
    for line in inputfile:
        results.append(line.strip().replace(')', ' ').replace('(', ' ').replace(',', ' ').split())

data = []
alag = {}
target = {}
with open('demo_data_real.txt') as inputfile:
    for line in inputfile:
        data.append(line)

# -------------------------------------------------------------------------------------------
# FIX FOR HARDCODE
# ------------------------------------------------
# Find places to start and end for alag
# ------------------------------------------------
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

alag_end = alag_end
# ------------------
# Create alag
# ------------------   ALAG ER HUGSA– VITLAUST SKO–A A MRG
for i in data[alag_start:alag_end]:
    i.strip()
    key = i[0:i.find(' ')]
    alag[int(key)] = [float(i[i.find(' '):])]

# ------------------------------------------------
# Find places to start and end for target
# ------------------------------------------------
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

# ------------------
# Create target
# -------------------
for i in data[target_start:target_end]:
	strengur = []
	strengur.append(i.split())

	target[int(strengur[0][0]+strengur[0][1])] = [int(strengur[0][2])]
	'''
	if len(strengur) == 6:
		key = i[0] + i[2]
		target[int(key)] = [int(i[i.find(' ', 3):].strip())]
	else:
    key = i[0] + i[2]
    print(i[0],'--',i[1],'---',i[2],'--',i[4:7])
    target[int(key)] = [int(i[i.find(' ', 3):].strip())]
	'''
# -------------------------------------------------------------------------------------------
#Feeds arr information about INNSTREYMI
#[id, SourceNo, date, Quantity, Timevalue, tegund, Vendor, Vendor_name, description]
selectstring = Select_string(vikunumer)  # call to SQL data base
cursor.execute(selectstring)
arr = cursor.fetchall()

#SELECT fyrir utstreymi
selectstring_uts = Select_string_OUT()
cursor.execute(selectstring_uts)
arr_uts = cursor.fetchall()



select_data_inn = {}
count_inn = 1
for x in arr:
    select_data_inn[count_inn] = [x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]]
    count_inn = count_inn + 1

select_data_uts = {}
print("Number of INNSTREYMI: " + str(count_inn))
count_ut = count_inn
for x in arr_uts:
    select_data_uts[count_ut] = [x[0], x[1], x[2], x[3], x[4]]
    count_ut = count_ut + 1

print("Number of UTSTREYMI: " + str(count_ut - count_inn))
print("Number of TOTALSHIPMENTS: " + str(count_ut))

fjoldiSendinga = count_ut -1


# ----------------------------------------------------------
# CREATE LAUSN
# ----------------------------------------------------------
#FIX TO NOT BE HARDCODED
counter = 0
first = 1
last = 1
lastsolutionline = (fjoldiSendinga * dagar * timeslott) + (dagar * timeslott * 8 + 4)
for x in results:
	if x[0] == 'x' and first:
		startsolutionline = counter
		first = 0

	if x[0] != 'x' and last and first == 0:
		lastsolutionline = counter
		last = 0
	counter = counter + 1

# ----------------------------------------------------------
# CREATE LAUSN
# ----------------------------------------------------------
lausn = {}
seperator = ''
for x in results[startsolutionline:lastsolutionline]:
    #print(x)
    if int(x[4]) == 1:  # lausn
        key = seperator.join(x[2:4])
        if key not in lausn:
            lausn[key] = []
        lausn[key].append(x)
#print(lausn)
# ----------------------------------------------------------
# CREATE THE BEST DICTIONRY IN THE WORLD
# ----------------------------------------------------------
#ID = sending
#[slott, dagur, innstreymi/utstreymi, alag, destination, shipcode, date, kennitala, description]
Best_Dict = {}

for x in lausn:
	#print(x,lausn[x])
	print('---\n')
	for i in range(0,len(lausn[x])):
		print(x,lausn[x][i],lausn[x][i][1])
		index = int(lausn[x][i][1])
		if index >= count_inn:
			Inn_ut = 'Ut'
			alag = select_data_uts[index][2]
			destination = select_data_uts[index][1]
			shipcode = select_data_uts[index][0]
			date = select_data_uts[index][3]
			kennitala = ''
			vendor = ''
		else:
			Inn_ut = 'Inn'
			alag = select_data_inn[index][3]*select_data_inn[index][4]
			destination = ''
			shipcode = ''
			date = ''
			kennitala = select_data_inn[index][6]
			vendor = select_data_inn[index][7]
		Best_Dict[index] = [int(lausn[x][i][2]),int(lausn[x][i][3]),Inn_ut,round(alag),destination,shipcode,date,kennitala,vendor]
		print(Best_Dict[index])

#print(Best_Dict)
#print(select_data_inn)
#print(select_data_uts)



# ----------------------------------------------------------
# MANNAMAL
# ----------------------------------------------------------
f = open("mannamal_basic.txt", "w+")
for x in results[startsolutionline:lastsolutionline]:
	if x[4] == '1':
		print(x,x[0])
		print(x[1],Best_Dict[int(x[1])])
		f.write('Dagur {} í tímaslotti {}. Er sending {}  frá Vendor/Dest {},{} A: {} \n'.format(Best_Dict[int(x[1])][1],Best_Dict[int(x[1])][0],x[1],Best_Dict[int(x[1])][5],Best_Dict[int(x[1])][7],Best_Dict[int(x[1])][3]))

f.close()

# ----------------------------------------------------------
# Create Lausn_for_print dictonary
# ----------------------------------------------------------

Lausn_for_print = {}

for i in range(1,dagar+1):
	for x in range(1,timeslott+1):
		alag_sum = 0
		counter = 0
		for y in Best_Dict:

			if Best_Dict[y][0] == x and Best_Dict[y][1] == i:
				alag_sum = alag_sum + Best_Dict[y][3]
				counter = counter + 1
		number =  str(x) + str(i)
		Lausn_for_print[(number)] = [alag_sum, counter]

#-------------------------------
#Create Lausn_for_vendor dictonary
#-------------------------------
Lausn_for_vendor = {}
Lausn_for_destination = {}

for i in range(1,timeslott+1):
	for x in range(1, dagar+1):

		number =  str(i) + str(x)
		Lausn_for_vendor[number] = set()
		Lausn_for_destination[number] = set()
		for y in Best_Dict:
			if Best_Dict[y][0] == i and Best_Dict[y][1] == x:
				if Best_Dict[y][2] == 'Inn':
					Lausn_for_vendor[number].add(Best_Dict[y][7])
				elif Best_Dict[y][2] == 'Ut':
					Lausn_for_destination[number].add(Best_Dict[y][5].split()[0])




#---

Vendorar_n_k = {'420369-7789':'Ölgerðin','470169-1419':'Cola','570169-0339':'Globus','700103-3660':'Vintrio','541205-1520':'Brugghusstedja',
'410999-2859':'Dista', '530303-2410':'Bakkus' ,'550595-2579':'Mekka',
"601083-0789":'Eimskip',"470105-2240":'Eimskip',"490104-2160":'Eimskip',"450310-0500":'Eimskip',
"491007-1680":'Eimskip',"511105-1290":'Eimskip',"601289-1489":'Eimskip',"470302-4290":'Eimskip',
"640485-0949":'Eimskip',"420178-0349":'Eimskip',"531212-0530":'Eimskip',"451205-0560":'Eimskip',
"470706-1040":'Eimskip',"451295-2929":'Eimskip',"530206-0330":'Eimskip',"620509-0190":'Eimskip',"470205-0400":'Eimskip',
'550394-2359':'Samskip','470415-1260':'Samskip','660509-0970':'Samskip','470710-0390':'Samskip','670616-1690':'Samskip',
'460999-2519':'Samskip','501117-0210':'Samskip','520914-2180':'Samskip','500316-0470':'Samskip','490211-0630':'Samskip',
'681215-1740':'Samskip','430913-0690':'Samskip','660169-1729':'Samskip','600112-1390':'Samskip','590515-3290':'Samskip',
'550609-1420':'Samskip','471289-2569':'Samskip','650387-1399':'Samskip','560113-0480':'Samskip','560793-2199':'Samskip',
'550405-0400':'Samskip','571214-0240':'Samskip','451115-1460':'Samskip','510515-1020':'Samskip','440417-0510':'Samskip'}


# -----------------------------------------------------------------
# Determine the color
# -----------------------------------------------------------------
newLFP = {}
for i in range(1,timeslott+1):
  for j in range(1,6):
    talan = str(i) + str(j);

    if (talan not in Lausn_for_print):
      newLFP[talan] = [0, 0]
    else:
      newLFP[talan] = Lausn_for_print.get(talan)


testTargets = list(target.values())
testTargets2 = np.zeros((timeslott, 5))
counter = 0;
for i in range(0, timeslott):
    for j in range(0, 5):
        testTargets2[i][j] = int(testTargets[counter][0])
    counter = counter + 1

testAlag = list(newLFP.values())

toA = []
A = []

counter = 0;
for timi in range(0,timeslott):
  for dagur in range(0,5):
    counter = counter + 1
    if(testAlag[counter-1][:1] > testTargets2[timi][dagur]): 
      toA.append(0.1) 
    elif(abs(testAlag[counter-1][:1] - testTargets2[timi][dagur]) < 100):
      toA.append(0.3)
    else:
      toA.append(0.2)

  A.append(toA)
  toA = []

# -----------------------------------------------------------------
# PLOT
# -----------------------------------------------------------------
'''
A = []

for i in range(0,timeslott):
	A.append([0.2,0.2,0.2,0.2,0.2])
'''

plt.subplots(1, 1, figsize=(12, 6))
cmap = matplotlib.colors.ListedColormap(['red', 'green', 'orange'])
plt.pcolor(A, edgecolors='k', linewidths=3, cmap=cmap)
#first_date = select_data[0][2]
#last_date = select_data[len(select_data)-1][2]
#plt.title('Stundatafla ' + first_date + ' - ' + last_date)
plt.ylabel('Time')
plt.xlabel('Date')

plt.xticks(np.arange(dagar), ['M', 'T', 'W', 'T', 'F', 'S', 'S'])
plt.yticks(np.arange(timeslott + 1), ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00','17:00','18:00','19:00','20:00'])


# PRINT ALAG & SENDINGAR
for i in Lausn_for_print:
	insertstring = 'Fjöldi sendinga: {} \n Alag: {} V/D: {},{}'

	# NUMBERSTING TO SEE NUMBER OF LETTERS IN SLOTTS
	numberstring = []
	numberstring = i.split()

	string_print = '\n'
	counter = 0
	for x in Lausn_for_destination[i]:
	    if counter in(0,1,2,4,5,6,8,9,10,11,13,14,15,16,18,19,20,22,23,24,26,27,28):
	    	string_print = string_print + x + ','
	    else:
	    	string_print = string_print + x + '\n'
	    counter = counter + 1

	#LINK VENDORS TO KENNITALA
	current_set = set()	
	if len(numberstring[0]) != 3:
		if int(i[0]) < 9:
			for x in Vendorar_n_k:
				if x in Lausn_for_vendor[i]:
					current_set.add(Vendorar_n_k[x])


	# LAGA ÞARF EKKI ALLAR ÞESSAR IF SETNINGAR
	insertstring = insertstring.format(Lausn_for_print[i][1], Lausn_for_print[i][0],current_set,string_print[:-1])
	plt.text(float(int(i[1])) - 0.5, float(int(i[0])) - 0.9,
	insertstring, size=4,
	ha="center", va="bottom",
	bbox=dict(boxstyle="square", ec=(0.1, 0.5, 0.9)))

	# PRINT THE TARGET
	for i in lausn:
		mainstring = 'Target: {}'
		plt.text(float(int(i[1])) - 0.5, float(int(i[0])) - 0.3, mainstring.format(target[int(i)][0]), size=4,
		         ha="center", va="bottom",
		         bbox=dict(boxstyle="square", ec=(0.1, 0.5, 0.5)))


plt.show()







