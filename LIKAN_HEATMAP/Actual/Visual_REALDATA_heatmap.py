import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import collections
import matplotlib.colors

import psycopg2
from Functions.Select_function import Select_string

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
    key = i[0] + i[2]
    target[int(key)] = [int(i[i.find(' ', 2):].strip())]

# -------------------------------------------------------------------------------------------


# ----------------------------------------------------------
# Create select_data and lausn
# ----------------------------------------------------------

selectstring = Select_string(1)  # call to SQL data base
cursor.execute(selectstring)
arr = cursor.fetchall()

select_data = {}
count = 0
for x in arr:
    select_data[count] = [x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]]
    count = count + 1

# Determine 3 values   HARDCODE !!!!!!!!!!!!!!!!!!!
fjoldiSendinga = count - 1;
dagar = 5
timeslott = 8

# ----------------------------------------------------------
# CREATE MANNAMAL
# ----------------------------------------------------------
f = open("lausn_mannamal.txt", "w+")
lausn = {}
for x in results[(dagar * timeslott + 3):(fjoldiSendinga * dagar * timeslott) + (dagar * timeslott + 3)]:
    seperator = ''
    if int(x[4]) == 1:  # lausn
        seperator = ''
        key = seperator.join(x[2:4])
        if key not in lausn:
            lausn[key] = []
        lausn[key].append(x)

        # meira ef lausn  -- Write the solution
        for i in select_data:
            if int(x[1]) == i:
                f.write('Dagur {} í tímaslotti {}. Er sending {} er með ID: {} frá Vendor: {} með kennitölu {} \n'.format(x[3],x[2],i,select_data[i][0],select_data[i][7],select_data[i][6]))
        f.write('Sendingin inniheldur {} stykki af {} með álagsvalue {} sem gerir álagið = {} \n'.format(select_data[i][3],select_data[i][8],select_data[i][4],(round(select_data[i][3]*select_data[i][4]))))
f.close()

f = open("mannamal_basic.txt", "w+")
for x in results[(dagar * timeslott + 3):(fjoldiSendinga * dagar * timeslott) + (dagar * timeslott + 3)]:
    seperator = ''
    if int(x[4]) == 1:  # lausn
        for i in select_data:
            if int(x[1]) == i:
                f.write('Dagur {} í tímaslotti {}. Er sending {} er með ID: {} frá Vendor {} A: {} \n'.format(x[3],x[2],i,select_data[i][0],select_data[i][6],round(select_data[i][3]*select_data[i][4])))
f.close()

# -------------------------------
# Create Lausn_for_print dictonary
# -------------------------------
Lausn_for_print = {}
for i in lausn:
    counter = 0;
    alag_sum = 0;
    for x in range(0, len(lausn[i])):
        alag_sum = alag_sum + alag[float(lausn[i][x][1])][0]
        counter = counter + 1

    Lausn_for_print[i] = [alag_sum, counter]

# -----------------------------------------------------------------
# print
# -----------------------------------------------------------------

# Determine the color

newLFP = {}
for i in range(1,9):
  for j in range(1,6):
    talan = str(i) + str(j);

    if (talan not in Lausn_for_print):
      newLFP[talan] = [0, 0]
    else:
      newLFP[talan] = Lausn_for_print.get(talan)


testTargets = list(target.values())
testTargets2 = np.zeros((8, 5))
counter = 0;
for i in range(0, 8):
    for j in range(0, 5):
        testTargets2[i][j] = int(testTargets[counter][0])
    counter = counter + 1

testAlag = list(newLFP.values())

toA = []
A = []

counter = 0;
for timi in range(0,8):
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
sumOfAll = []
counter = 0
for p in range(0, len(newLFP)):
    sumOfAll.append(list(newLFP.values())[counter][0])
    counter = counter + 1;
arr = np.array(sumOfAll)

sumOfAllFinal = np.array(sumOfAll)

sumOfAllFinal2 = np.zeros((8, 5))
counter = 0;
for j in range(0, 8):
    for i in range(0, 5):
        sumOfAllFinal2[j][i] = sumOfAllFinal[counter]
        counter = counter + 1;
        
plt.imshow(sumOfAllFinal2, cmap='RdYlGn_r' ,interpolation='nearest', origin='lower')
plt.ylabel('Time')
plt.xlabel('Date')

plt.xticks(np.arange(dagar), ['M', 'T', 'W', 'T', 'F', 'S', 'S'])
plt.yticks(np.arange(timeslott + 1), ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'])

plt.colorbar()
plt.show()


