import csv
from Alagsstudull import Create_alag

f1 = open('Voruspjald_Voruhus_afrit_ItemCAT_NEW.csv')

Item_Cat = []

dreader = csv.DictReader(f1, delimiter=';')
for row in dreader:
    Item_Cat.append(row)

f1.close()



Item_cat_numbersDict = {}

#Load into dictonary key=number , value= tegund

for x in range(0,len(Item_Cat)):
		Item_cat_numbersDict[int(float(Item_Cat[x]['\ufeffItem Category Code']))] = [Item_Cat[x]['Tegund'],Item_Cat[x]['Value']]

#print key with value


#for i in Item_cat_numbersDict:
alex = 0.0
print(Create_alag(Item_cat_numbersDict[1][0]))
print(alex)

print('hey')
print(Item_cat_numbersDict[1][0])

print(Item_cat_numbersDict)


for i in Item_cat_numbersDict:
	Item_cat_numbersDict[i][1] = Create_alag(Item_cat_numbersDict[i][0])
	print(Item_cat_numbersDict[i][1])


for i in sorted(Item_cat_numbersDict):
	print(i, Item_cat_numbersDict[i])
