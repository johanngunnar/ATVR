import csv
from Alagsstudull import Create_alag
from Update_alagsstudull import update_function_alagsstudull

#--------------------------------------------------
#RUN THIS FILE TO UPDATE THE ALAG IN THE DATA BASE.
#--------------------------------------------------

f1 = open('Voruspjald_Voruhus_afrit.csv')
Item_Cat = []

dreader = csv.DictReader(f1, delimiter=';')
for row in dreader:
    Item_Cat.append(row)

f1.close()

#--------------------------------------------------
#Load into dictonary key=number , value= tegund
#--------------------------------------------------

Item_cat_numbersDict = {}
lengd = len(Item_Cat)-13
#lengd = 200
for x in range(0,lengd):
		Item_cat_numbersDict[int(Item_Cat[x]['\ufeffNo_'])] = []

#--------------------------------------------------
#USE ALAGSSTUDULL.PY TO CREATE ALAG FOR EACH PRODUCT
#--------------------------------------------------

for i in Item_cat_numbersDict:
	check = round(Create_alag(i),2)
	Item_cat_numbersDict[i].append(check)
	print(i)


#--------------------------------------------------
#NOW GO TO THE DATABASE AND UPDATE
#--------------------------------------------------
update_function_alagsstudull(Item_cat_numbersDict)