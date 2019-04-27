import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

#------------------------------------------------
#Load solution data and demo_data
results = []
with open('solution.sol') as inputfile:

    for line in inputfile:
        results.append(line.strip().replace(')',' ').replace('(',' ').replace(',',' ').split())

data = []
alag = {}
target = {}
with open('demo_data.dat2.txt') as inputfile:

    for line in inputfile:
        data.append(line)

#------------------------------------------------
#Carefull !!!!, hardcoded from the data file

#create alag
#------------------------------------------------
#Find places to start and end 
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
#-----------------------

for i in data[alag_start:alag_end]:
	i.strip()
	key = i[0] + i[1]

	alag[int(key)] = [int(i[i.rfind('\n')-1])]

print('------')


#-----------------------
#Find places to start and end 
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


#create target
for i in data[target_start:target_end]: 
	#print(i)
	key = i[0] + i[2]
	target[int(key)] = [int(i[4])]

print('Target: {}'.format(target))
#-------------------------

#------------------------------------------------
#Done loading Data
#------------------------------------------------

#Create lausn and print lausn_mannamal
f= open("lausn_mannamal.txt","w+")
lausn = {}
for x in results[13:]:

	seperator = ''
	if int(x[4]) == 1:
		seperator = ''
		key = seperator.join(x[2:4])
		if key not in lausn:
			lausn[key] = []
		lausn[key].append(x)

		f.write('Sending {} er á degi {} í tímaslotti {} \n'.format(x[1],x[3],x[2]))

print('Lausnar Directory: {}'.format(lausn))
f.close()


## -----------------------------------------------------------------
#print
## -----------------------------------------------------------------

Z = np.random.rand(2, 5)
#Z = np.array([0.1,0.1,0.1,0.1,0.1],[0.2,0.2,0.2,0.2,0.2])
#Z = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
#Z = []
#Z[0] = [0.50035921, 0.31742269, 0.18465873, 0.33234468, 0.47256083]
#Z[1] = [0.61936819, 0.16106473, 0.54516694, 0.48644065, 0.45649766]
print(Z)
print(Z[0][0])
print(Z[1][0])
type(Z)


plt.subplots(1, 1)

c = plt.pcolor(Z, edgecolors='k', linewidths=3)
plt.title('Stundatafla')
plt.ylabel('Time')
plt.xlabel('Date')

plt.xticks(np.arange(5),['M', 'T', 'W', 'T', 'F', 'S', 'S'])
plt.yticks(np.arange(3),['8:00','12:00','14:00', '18:00', '20:00', '14:00', 'S'])

#Print the solution for each slot
for i in lausn:
	print(i)
	#print the Target
	mainstring = 'Target: {}'
	#target[int(i)][0]
	plt.text(float(int(i[1]))-0.5, float(int(i[0]))-0.1,mainstring.format(target[int(i)][0]), size=7,
			ha="center", va="bottom",
			bbox=dict(boxstyle="square",ec=(0.1, 0.5, 0.5)))

	#print sending + alag
	sending = []
	for x in range(0,len(lausn[i])):
		sending.append(lausn[i][x][1])
		insertstring = 'Sending: {} \n Alag: {} '
		#alag[lausn[i][x][1]][0]
		plt.text(float(int(i[1]))-0.5, float(int(i[0]))-0.4-(x/7),insertstring.format(lausn[i][x][1],alag[int(lausn[i][x][1])][0]), size=7,
	         ha="center", va="bottom",
	         bbox=dict(boxstyle="square",ec=(0.1, 0.5, 0.5))
	         )

plt.show()

