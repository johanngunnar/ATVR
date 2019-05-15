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
# CREATE MANNAMAL
# ----------------------------------------------------------
f = open("lausn_mannamal.txt", "w+")
lausn = {}
for x in results[startsolutionline:lastsolutionline]:
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
    # Create Lausn_for_print dictonary = slot [alag_sum, fjoldi_sendinga]
    counter = 0;
    alag_sum = 0;
    for x in range(0, len(lausn[i])):
        alag_sum = alag_sum + alag[float(lausn[i][x][1])][0]
        counter = counter + 1

    Lausn_for_print[i] = [alag_sum, counter]

# -------------------------------
# Create ALAG for days in week 
# -------------------------------
mon_alag = 0
thr_alag = 0
mid_alag = 0
fim_alag = 0
fos_alag = 0
for i in Lausn_for_print:
    print(i[1:],Lausn_for_print[i][0])
    if int(i[1:]) == 1:
        mon_alag = mon_alag + Lausn_for_print[i][0]
    elif int(i[1:]) == 2:
        thr_alag = thr_alag + Lausn_for_print[i][0]
    elif int(i[1:]) == 3:
        mid_alag = mid_alag + Lausn_for_print[i][0]
    elif int(i[1:]) == 4:
        fim_alag = fim_alag + Lausn_for_print[i][0]
    elif int(i[1:]) == 5:
        fos_alag = fos_alag + Lausn_for_print[i][0]



#-------------------------------
#Create Lausn_for_vendor dictonary
#-------------------------------
Lausn_for_vendor = {}
for i in lausn: 
    #Create Lausn_for_vendor dictonary = slot [alag_sum, fjoldi_sendinga]
    counter = 0;
    alag_sum = 0;
    #Lausn i[1],i[2],i[3] = sending, timeslott, dagur

    #NAFNID
    for x in range(0,len(lausn[i])):

        for y in select_data:
            
            if int(y) == int(lausn[i][x][1]):
                if i not in Lausn_for_vendor:
                    Lausn_for_vendor[i] = set()
                    Lausn_for_vendor[i].add(select_data[y][6])
                else:
                    Lausn_for_vendor[i].add(select_data[y][6])

# -----------------------------------------------------------------
# Vendorar
# -----------------------------------------------------------------
Vendorar_n_k = {'420369-7789':'Olgerdin','470169-1419':'Cola','570169-0339':'Globus','700103-3660':'Vintrio','541205-1520':'Brugghusstedja',
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
plt.subplots(1, 1, figsize=(12, 6))
cmap = matplotlib.colors.ListedColormap(['red', 'green', 'orange'])
plt.pcolor(A, edgecolors='k', linewidths=3, cmap=cmap)
first_date = select_data[0][2]
last_date = select_data[len(select_data)-1][2]
plt.title('Stundatafla ' + first_date + ' - ' + last_date)
plt.ylabel('Time')
plt.xlabel('\nDate')



plt.xticks(np.arange(dagar)+0.5, ['M \n Alag: {}'.format(mon_alag), 'T \n Alag: {}'.format(thr_alag), 'W \n Alag: {}'.format(mid_alag), 'T \n Alag: {}'.format(fim_alag), 'F \n Alag: {}'.format(fos_alag), 'S', 'S'])
plt.yticks(np.arange(timeslott + 1), ['7:30', '8:30', '9:30', '10:30', '11:30', '12:30', '13:30', '14:30', '15:30'])

# PRINT THE TARGET

for i in lausn:
    mainstring = 'Target: {}'
    plt.text(float(int(i[1])) - 0.5, float(int(i[0])) - 0.3, mainstring.format(target[int(i)][0]), size=8,
             ha="center", va="bottom",
             bbox=dict(boxstyle="square", ec=(0.1, 0.5, 0.5)))

for i in Lausn_for_print:
    insertstring = 'Fjöldi sendinga: {} \n Alag: {} \n Vendor: {}'

# PRINT VENDORAR
    current_set = set()
    for x in Vendorar_n_k:
        if x in Lausn_for_vendor[i]:
            current_set.add(Vendorar_n_k[x])

    string_print = ''
    for x in current_set:
        string_print = string_print + x + '\n'

    plt.text(float(int(i[1])) - 0.5, float(int(i[0])) - 0.9,
         insertstring.format(Lausn_for_print[i][1], Lausn_for_print[i][0],string_print[:-1]), size=5,
         ha="center", va="bottom",
         bbox=dict(boxstyle="square", ec=(0.1, 0.5, 0.9)))

plt.show()

