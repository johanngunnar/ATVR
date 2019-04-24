import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import collections

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
#create alag
for i in data[alag_start:alag_end]:
	i.strip()
	#key = i[0] + i[1]
	key = i[0:i.find(' ')]

	alag[int(key)] = [float(i[i.find(' '):])]

print('------')
print(i)
print(i.find(' '))


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

#-------------------------
#create target
for i in data[target_start:target_end]: 
	#print(i)
	key = i[0] + i[2]
	target[int(key)] = [int(i[i.find(' ',2):].strip())]
print('hey')
print(i)
print(i[i.find(' ',2):].strip())

print('Target: {}'.format(target))


#------------------------------------------------
#Done loading Data
#------------------------------------------------

#Create lausn and print lausn_mannamal

f= open("lausn_mannamal.txt","w+")
lausn = {}
print_lausn = {}
for x in results[23:]:

	seperator = ''
	if int(x[4]) == 1:
		seperator = ''
		key = seperator.join(x[2:4])
		if key not in lausn:
			lausn[key] = []
		lausn[key].append(x)

		f.write('Sending {} er á degi {} í tímaslotti {} \n'.format(x[1],x[3],x[2]))


od = collections.OrderedDict(sorted(print_lausn.items()))
print('SORTED ---------------')
print('Lausnar Directory: {}'.format(lausn))
f.close()


print('ALAG ---------------')
print(alag)

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
for i in range(0,4):
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

plt.xticks(np.arange(5),['M', 'T', 'W', 'T', 'F', 'S', 'S'])
plt.yticks(np.arange(5),['8:00','10:00','12:00', '14:00', '16:00', '14:00', 'S'])

#Print the solution for each slot
for i in lausn:
	#print(i)
	#print the Target
	mainstring = 'Target: {}'
	#target[int(i)][0]
	plt.text(float(int(i[1]))-0.5, float(int(i[0]))-0.1,mainstring.format(target[int(i)][0]), size=5,
			ha="center", va="bottom",
			bbox=dict(boxstyle="square",ec=(0.1, 0.5, 0.5)))

	#print sending + alag
	'''
	sending = []
	for x in range(0,len(lausn[i])):
		sending.append(lausn[i][x][1])
		insertstring = 'Sending: {} \n Alag: {} '
		#alag[lausn[i][x][1]][0]
		plt.text(float(int(i[1]))-0.5, float(int(i[0]))-0.4-(x/6),insertstring.format(lausn[i][x][1],alag[float(lausn[i][x][1])][0]), size=6,
	         ha="center", va="bottom",
	         bbox=dict(boxstyle="square",ec=(0.1, 0.5, 0.9))
	         )
	'''
	

for i in Lausn_for_print:
		insertstring = 'Fjöldi sendinga: {} \n Alag: {} '
		#alag[lausn[i][x][1]][0]
		plt.text(float(int(i[1]))-0.5, float(int(i[0]))-0.4,insertstring.format(Lausn_for_print[i][1],Lausn_for_print[i][0]), size=6,
	         ha="center", va="bottom",
	         bbox=dict(boxstyle="square",ec=(0.1, 0.5, 0.9))
	         )
	





print('Lausn for print')
print(Lausn_for_print)
for i in Lausn_for_print:
	print(i,Lausn_for_print[i])



plt.show()

