import csv
from Insert_function_basic import insert_function_basic
from Insert_function import insert_function
from Insert_function_Innstreymi import insert_function_innstreymi
from Insert_function_utstreymi import insert_function_utstreymi
from Insert_function_vinnsla import insert_function_vinnsla
from Insert_function_item import insert_function_item
from Insert_function_SENDING import insert_function_sending

import re

f1 = open('Vöruhús_Hópur_InnstreymiDM_Afrit_new.csv')
f2 = open('Voruspjald_Voruhus_afrit.csv')
f3 = open('Voruhus_Hopur_Utstreymi_Afrit.csv')
f4 = open('Voruhus_Hopur_Mottaka&Tiltekt_Afrit.csv')
f5 = open('Voruspjald_Voruhus_afrit_ItemCAT_NEW.csv')
f6 = open('Voruhus_Hopur_REAfrit.csv')

#Create List --------------------------------------------------
Innstreymi = []
Utstreymi = []
Voruspjald = []
Vinnsla = []
Item_Cat = []
Sending = []

# Load the DATA into LIST --------------------------------------

dreader = csv.DictReader(f1, delimiter=';')
for row in dreader:
    Innstreymi.append(row)

f1.close()

c = 0
dreader = csv.DictReader(f2, delimiter=';')
for row in dreader:
	if c < 19569: #HARDCODE
   		Voruspjald.append(row)
   		c = c + 1

print(c)
f2.close()


dreader = csv.DictReader(f3, delimiter=';')
for row in dreader:
    Utstreymi.append(row)

f3.close()


dreader = csv.DictReader(f4, delimiter=';')
next(f4)
next(f4)
next(f4)
for row in dreader:
    Vinnsla.append(row)

f4.close()

dreader = csv.DictReader(f5, delimiter=';')
for row in dreader:
    Item_Cat.append(row)

f5.close()

dreader = csv.DictReader(f6, delimiter=';')
for row in dreader:
    Sending.append(row)

f6.close()


#Check data -------------------------------------------------------
print('Innstreymi -------')
#print(Innstreymi[1])  #call for line 1 (list )and value for location code (dictonary)
print('Vöruspjald -------')
print(Vinnsla[5])
print(Voruspjald[2]['Heiti umboðsmanns'])
print(Voruspjald[2]['Heiti umboðsmanns'].replace(' ', ''))

print(Voruspjald[3328]['Unit Price'])
print(Voruspjald[3328]['Unit Price'].find(','))
print(Voruspjald[3328]['Unit Price'][2:])
print(Voruspjald[3328]['Unit Price'].replace((Voruspjald[3328]['Unit Price'][(Voruspjald[3328]['Unit Price'].find(',')):]),''))

#print(Item_Cat[5])

'''
#Create Item_Category-------------------------------------------------

Item_cat_numbersDict = {}

#Load into dictonary key=number , value= tegund

for x in range(0,len(Item_Cat)):
    Item_cat_numbersDict[int(float(Item_Cat[x]['\ufeffItem Category Code']))] = [Item_Cat[x]['Tegund'],Item_Cat[x]['Value']]

#print key with value

for i in sorted(Item_cat_numbersDict):
    print(i, Item_cat_numbersDict[i])


#print(Item_cat_numbersDict)

#INSERT FUNCTIONS CALL ----
#insert_function_basic(Item_cat_numbersDict)
insert_function(Item_cat_numbersDict)


#Creat Item (Vöruspjald)--------------------------------------------
Item_Dict = {}
for x in range(0,len(Voruspjald)):
    if(Voruspjald[x]['Vendor No_'] == ''):
        Voruspjald[x]['Vendor No_'] = 0
    
    if Voruspjald[x]['Item Category Code'] == '':
        continue
    Voruspjald[x]['Item Category Code'].strip("0")

    Voruspjald[x]['Description'] = re.sub("[!@'#$]", '', Voruspjald[x]['Description'])


    Voruspjald[x]['Unit Price'].replace((Voruspjald[x]['Unit Price'][(Voruspjald[x]['Unit Price'].find(',')):]),'')
    Voruspjald[x]['Millilítrar'].replace((Voruspjald[x]['Millilítrar'][(Voruspjald[x]['Millilítrar'].find(',')):]),'')
    
    Item_Dict[int(float(Voruspjald[x]['\ufeffNo_']))] = [Voruspjald[x]['Unit Price'],Voruspjald[x]['Söluflokkur'],Voruspjald[x]['Item Category Code'],Voruspjald[x]['ABC-Item'],Voruspjald[x]['Áfengisgjald (tegund)'],Voruspjald[x]['Base Unit of Measure'],Voruspjald[x]['Millilítrar'],Voruspjald[x]['Vendor No_'],Voruspjald[x]['Heiti umboðsmanns'],Voruspjald[x]['Description']]

for i in sorted(Item_Dict):
    print(i, Item_Dict[i])

insert_function_item(Item_Dict)


#Create Sending --------------------------------------------------
Sending_Dict = {}
for x in range(1,len(Sending)):
    if Sending[x]['Shelf No_'] == '':
        Sending[x]['Shelf No_'] = ' '
    Sending_Dict[x] = [Sending[x]['Source No_'],Sending[x]['Item No_'],Sending[x]['Whse_ Receipt No_'],(Sending[x]['Shelf No_']),Sending[x]['Status'],Sending[x]['Counted Quantity'],Sending[x]['Ordered Qty_'],Sending[x]['Posting Date']]

for i in sorted(Sending_Dict):
    print(i, Sending_Dict[i])

insert_function_sending(Sending_Dict)


#Create Innstreymi---------------------------------------------------
Innstreymi_Dict = {}
for x in range(0,len(Innstreymi)):
    if Innstreymi[x]['Quantity'][0] == '0':
        continue
    Innstreymi[x]['No_'] = Innstreymi[x]['No_'].replace('_', '')

    Innstreymi_Dict[x] = [Innstreymi[x]['No_'],Innstreymi[x]['Item No_'],Innstreymi[x]['Source No_'],(Innstreymi[x]['Qty_ per Unit of Measure']),(Innstreymi[x]['Quantity']),Innstreymi[x]['Qty_ (Base)'],Innstreymi[x]['Starting Date'],Innstreymi[x]['Whse_ Activity No_']]

for i in sorted(Innstreymi_Dict):
    print(i, Innstreymi_Dict[i])

print(Innstreymi_Dict[1])
print(Innstreymi_Dict[1][2])

insert_function_innstreymi(Innstreymi_Dict)
'''

#Create Utstreymi---------------------------------------------------
Utstreymi_Dict = {}
for x in range(0,len(Utstreymi)):
    if Utstreymi[x]['Quantity'][0] == '0' or Utstreymi[x]['Qty_ (Base)'][0] == '0' or Utstreymi[x]['Qty_ per Unit of Measure'][0] == '0' :
        continue
    else:
        Utstreymi_Dict[x] = [Utstreymi[x]['Ship-to Code'],Utstreymi[x]['Ship-to Name'],Utstreymi[x]['Item No_'],Utstreymi[x]['Qty_ per Unit of Measure'],Utstreymi[x]['Quantity'],Utstreymi[x]['Qty_ (Base)'],Utstreymi[x]['Millilítrar'],Utstreymi[x]['Fjöldi lítra'],Utstreymi[x]['Posting Date']]

for i in sorted(Utstreymi_Dict):
    print(i, Utstreymi_Dict[i])

print(Utstreymi_Dict[1])
print(Utstreymi_Dict[1][2])

insert_function_utstreymi(Utstreymi_Dict)

'''
#Create Vinnsla---------------------------------------------------
Vinnsla_Dict = {}
for x in range(0,len(Vinnsla)):
	if(Vinnsla[x]['Item No_']) == '':
		continue
	if(Vinnsla[x]['Qty_ per UOM']) == '':
		Vinnsla[x]['Qty_ per UOM'] = 0
	if(Vinnsla[x]['Quantity']) == '':
		Vinnsla[x]['Quantity'] = 0
	if(Vinnsla[x]['Qty_ (Base)']) == '':
		Vinnsla[x]['Qty_ (Base)'] = 0

	if(Vinnsla[x]['Document ID 2'] != ''):
		continue
	else:	
		Vinnsla_Dict[x] = [Vinnsla[x]['Document ID 1'],Vinnsla[x]['Document ID 2'],Vinnsla[x]['User ID'],int(Vinnsla[x]['Item No_']),Vinnsla[x]['Qty_ per UOM'],Vinnsla[x]['Quantity'],Vinnsla[x]['Qty_ (Base)'],Vinnsla[x]['Date Scanned'],Vinnsla[x]['Tími skönnunar'],Vinnsla[x]['Lok skönnunar']]

for i in sorted(Vinnsla_Dict):
	print(i, Vinnsla_Dict[i])

print(Vinnsla_Dict[1])
print(Vinnsla_Dict[1][2])

insert_function_vinnsla(Vinnsla_Dict)
'''










'''
#Create Vendor List--------------------------------------------------
#Create set of kennitala
Vendor_K = set()
for i in range(0, len(Voruspjald)) :
	Vendor_K.add(Voruspjald[i]['Vendor No_'])

#print(Vendor_K)


#Create dictonary and put kennitala as Key
Vendor_Dict = {}
for x in Vendor_K:
		Vendor_Dict[x] = ''

#Match names with kennitala and put it into dict
match = 0
for x in Vendor_Dict:
	for i in range(0, len(Voruspjald)) :
		if Voruspjald[i]['Vendor No_'] == x:
			if Vendor_Dict[x] == '':
				Vendor_Dict[x] = Voruspjald[i]['Heiti umboðsmanns']
				match = match +1
			else:
				break
		else:
			continue 


for d in Vendor_Dict:
	print(d, Vendor_Dict[d])

counter = 0
for d in Vendor_Dict:
	if Vendor_Dict[d] == '':
		counter = counter +1 

print(counter)
print(match)
'''

