import csv

f = open('Voruspjald_Voruhus_afrit.csv')

dreader = csv.DictReader(f, delimiter=';')

data = []
for row in dreader:
    data.append(row)

f.close()

insertstring = "insert into item_category (name, tegund) values ('{}','{}');\n"

f = open('insert_commands.sql', 'w')
for d in data:
    f.write(insertstring.format( d['Item Category Code'], d['Description'] ))
f.close()

