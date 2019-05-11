import csv
from Alagsstudull import Create_alag
from Update_alagsstudull import update_function_alagsstudull

#--------------------------------------------------
#RUN THIS FILE TO UPDATE THE ALAG IN THE DATA BASE.
#--------------------------------------------------

f1 = open('Voruspjald_Voruhus_afrit_ItemCAT_NEW.csv')
Item_Cat = []

dreader = csv.DictReader(f1, delimiter=';')
for row in dreader:
    Item_Cat.append(row)

f1.close()

#--------------------------------------------------
#Load into dictonary key=number , value= tegund
#--------------------------------------------------

Item_cat_numbersDict = {}
for x in range(0,len(Item_Cat)):
		Item_cat_numbersDict[int(float(Item_Cat[x]['\ufeffItem Category Code']))] = [Item_Cat[x]['Tegund'],Item_Cat[x]['Value']]

#--------------------------------------------------
#USE ALAGSSTUDULL.PY TO CREATE ALAG FOR EACH PRODUCT
#--------------------------------------------------

for i in Item_cat_numbersDict:
	Item_cat_numbersDict[i][1] = round(Create_alag(Item_cat_numbersDict[i][0]), 2)
	print(Item_cat_numbersDict[i][1])


for i in sorted(Item_cat_numbersDict):
	print(i, Item_cat_numbersDict[i])

#--------------------------------------------------
#NOW GO TO THE DATABASE AND UPDATE
#--------------------------------------------------
update_function_alagsstudull(Item_cat_numbersDict)