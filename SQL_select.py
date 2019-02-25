import psycopg2
# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

#preventing from breaking terminal
#splt.ion()

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

kenntiolur = []

# Write the select Q -------------------------------
#selectstring_olgerd = "select * from Innstreymi i, item v, Item_Category c where i.itemno = v.id and v.vendor = '420369-7789' and i.date = '07/02/2018'"
selectstring = "select * from Innstreymi i, item v, Item_Category c where i.itemno = v.id and i.date = '07/02/2018'"


cursor.execute(selectstring)

arr = cursor.fetchall()
alag = 0.0
alag_olgerdin = 0.0
#1 Ölgerðin (edi) ,2 Coca-Cola (edi),3  Globus (edi), Vín tríó, 4 Brugghús Steðja, Dista , 5 Bakkus (edi), 6 Mekka (edi)
slot = ['420369-7789','580483-0709','570169-0339','410999-2859','530303-2410','550595-2579']
alag_arr = [0,0,0,0,0,0]

#Dictornary lykill kennitala, value index --

print ('\nShow me the databases:\n')
for x in arr:
    print("   ", x)
    if x[16] == '420369-7789':
    	alag_olgerdin = alag_olgerdin + (x[19]*x[5])
    alag = (alag) + (x[19]*x[5])

    for i in range(0,len(slot)):
    	if x[16] == slot[i]:
    		alag_arr[i] = alag_arr[i] + (x[19]*x[5])

print('Total alag yfir allan daginn i klst er {0:.2f}'.format(alag))
print('Total alag yfir allan daginn frá Ölgerðinni i sek er {0:.2f}'.format(alag_olgerdin))

staff_unit_capacity = 1
staffvalue_per_day = 60*60*8*staff_unit_capacity

print('We need {0:.2f} empl. per day'.format((alag/staffvalue_per_day)))
print('We need {0:.2f} empl. for olgerdin per day'.format((alag_olgerdin/staffvalue_per_day)))

#Think about slot
time_slot = 60
start_min_from_midnight = 450

print(alag_arr)


# Prepare the data
x = np.linspace(start_min_from_midnight,(start_min_from_midnight+(60*6)),6)

# Plot the data
plt.plot(x,alag_arr, label='Álag')

# Show the plot
plt.show()

conn.commit()

cursor.close()
conn.close()

plt.ion()
