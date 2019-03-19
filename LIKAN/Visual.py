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
for i in data[7:22]:
	i.strip()
	key = i[0] + i[1]

	alag[int(key)] = [int(i[i.rfind('\n')-1])]

print('------')
print(alag)


#create target
for i in data[25:35]: 
	print(i)
	key = i[0] + i[2]
	target[int(key)] = [int(i[4])]

print('Target: {}'.format(target))

#------------------------------------------------
#Done loading Data
#------------------------------------------------

#Create lausn and print lausn_mannamal
f= open("lausn_mannamal.txt","w+")
lausn = {}
for x in results[3:]:

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
type(Z)
#Z = np.array([0.1,0.1,0.1,0.1,0.1],[0.2,0.2,0.2,0.2,0.2])
#Z = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
#Z = [[0.2,0.2,0.2,0.2,0.2][0.3,0.3,0.3,0.3,0.3]]
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

