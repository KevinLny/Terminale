import csv

f=open("alertes-pollens-nantes.csv", 'rt', encoding='UTF8')
lecteurCSV=csv.DictReader(f,delimiter=";")

for ligne in lecteurCSV:
    if ligne['Etat']=="2.0":
        print(ligne['Espèce'])

print(ligne.items())
print(ligne.keys())
print(ligne.values())
print(ligne['Espèce'])
if ligne['Etat']=="3.0":
    print(ligne['Espèce'])
f.close()


