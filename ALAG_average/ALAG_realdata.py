import psycopg2
import math
# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

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


#----------------------------------------------------------------------------
# Write the select Q
#----------------------------------------------------------------------------

selectstring = " select c.tegund, vi.Document_ID1, vi.UserID, vi.Quantity, vi.Qty_perUnit, vi.picked, vi.Picked_Unit,s.date,s.RE_number, s.Shelf, i.Vendor, i.Description, c.Timevalue from vinnsla vi, sending s, item i, Item_Category c where vi.itemno = i.id and s.ItemNo = i.id and s.RE_number = vi.Document_ID1 and c.name = i.Tegund and s.date = '09/02/2018' order by vi.Picked"

cursor.execute(selectstring)
arr = cursor.fetchall()

selectstring2 = "select * from Item_Category"
cursor.execute(selectstring2)
record = cursor.fetchall()

#1 Ölgerðin (edi) ,2 Coca-Cola (edi),3  Globus (edi), Vín tríó, 4 Brugghús Steðja, Dista , 5 Bakkus (edi), 6 Mekka (edi)
#slot_dict = {'420369-7789':0,'550595-2579':0,'580483-0709':1,'470169-1419':1,'700103-3660':2,'570169-0339':2,'410999-2859':3,'530303-2410':4,'550595-2579':5}

print ('\nShow me the databases:\n')
for x in arr:
    print(x)

#----------------------------------------------------------------------------
# Dictornary lykill kennitala, value index
#----------------------------------------------------------------------------

time_slot_length = 5
start_min_from_midnight = 450
end_min_from_midnight = start_min_from_midnight+(60*9)


xaxis = []
slot_dict = {}
for i in range(start_min_from_midnight,(end_min_from_midnight),time_slot_length):
    
    x = '{}....{}:{}'.format(i,math.floor(i/60),i%60)
    slot_dict[i] = [0]
    xaxis.append(x)

print(xaxis)

for i in range(0,len(arr)):
    first_num = int((arr[i][5])[0:2])
    second_num = int((arr[i][5])[3:5])
    for j in slot_dict:
        if (first_num*60 + second_num) <= j+time_slot_length:
            #margfoldunarstudull = 1
            margfoldunarstudull = arr[i][12]
            slot_dict[j] = [slot_dict[j][0] + (arr[i][3]* margfoldunarstudull)]
            break


print('This is the dictonary --')
print(slot_dict)
print('\n')


#put Slot_dict values into a list
slot_arr = []
for i in slot_dict:
    slot_arr.append(slot_dict[i][0])

print(slot_arr)


#----------------------------------------------------------------------------
# Plot the data
#----------------------------------------------------------------------------
# Prepare the data
j = np.arange(start_min_from_midnight,end_min_from_midnight,60)


x = np.linspace(start_min_from_midnight,end_min_from_midnight,(end_min_from_midnight-start_min_from_midnight)/time_slot_length)
plt.bar(x,slot_arr,width = 4)

timeslots = []
for i in range(start_min_from_midnight,end_min_from_midnight,60):
    timeslots.append('{}:{} '.format(math.floor(start_min_from_midnight/60),start_min_from_midnight%60))
    start_min_from_midnight = start_min_from_midnight + (60)

plt.xticks(j, (timeslots[0],timeslots[1],timeslots[2],timeslots[3],timeslots[4],timeslots[5],timeslots[6],timeslots[7]))
plt.title('Magn af kössum inn í kerfið')
plt.xlabel('Timi')
plt.ylabel('Álag [Magn * Margfoldunarstuðull]')
# Show the plot
plt.show()


conn.commit()
cursor.close()
conn.close()

