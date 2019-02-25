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

date = '07/02/2018'
# Write the select Q -------------------------------
#selectstring_olgerd = "select * from Innstreymi i, item v, Item_Category c where i.itemno = v.id and v.vendor = '420369-7789' and i.date = '07/02/2018'"
selectstring = "select * from Innstreymi i, item v, Item_Category c where i.itemno = v.id and i.date = '07/02/2018'"

cursor.execute(selectstring)
arr = cursor.fetchall()

alag = 0.0
alag_olgerdin = 0.0
#1 Ölgerðin (edi) ,2 Coca-Cola (edi),3  Globus (edi), Vín tríó, 4 Brugghús Steðja, Dista , 5 Bakkus (edi), 6 Mekka (edi)
slot_dict = {'420369-7789':0,'550595-2579':0,'580483-0709':1,'470169-1419':1,'700103-3660':2,'570169-0339':2,'410999-2859':3,'530303-2410':4,'550595-2579':5}
alag_arr = [0,0,0,0,0,0,0,0]
#Dictornary lykill kennitala, value index --


print ('\nShow me the databases:\n')
for x in arr:
    print("   ", x)
    if x[16] == '550595-2579':
    	alag_olgerdin = alag_olgerdin + (x[19]*x[5])
    alag = (alag) + (x[19]*x[5])

    for i in slot_dict:
        if x[16] == i:
            alag_arr[slot_dict[i]] = alag_arr[slot_dict[i]] + (x[19]*x[5])

#Calculations with alag


print('Total alag yfir allan daginn i sek er {0:.2f}'.format(alag))
print('Total alag yfir allan daginn frá Ölgerðinni i sek er {0:.2f}'.format(alag_olgerdin))

staff_unit_capacity = 1
staffvalue_per_day = 60*60*8*staff_unit_capacity

print('We need {0:.2f} empl. per day'.format((alag/staffvalue_per_day)))
print('We need {0:.2f} empl. for olgerdin per day'.format((alag_olgerdin/staffvalue_per_day)))



print(alag_arr)
print(sum(alag_arr))
print('Total alag: {}'.format(alag))
print('Alag ur fyrst 5 slotunum: {}'.format(sum(alag_arr)))
print('Munurinn: {}'.format(alag - sum(alag_arr)))

# BRÁÐARBIRGÐALAUSN - deilum restinni jafna á milli siðustu slottana

alag_arr[6] = (alag - sum(alag_arr))/2
alag_arr[7] = alag_arr[6]


#Think about slot----------------------------------------------
time_slot = 60
start_min_from_midnight = 450

# Prepare the data
x = np.linspace(start_min_from_midnight,(start_min_from_midnight+(60*8)),8)

# Plot the data
plt.bar(x,alag_arr,width=30)
plt.title('Álag inn í kerfið {}'.format(date))
plt.xlabel('Min from midnight')
plt.ylabel('Álag í kerfið')
# Show the plot
plt.show()

conn.commit()
cursor.close()
conn.close()

