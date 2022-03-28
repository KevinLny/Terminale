import json

f = open("alertes-pollens-nantes.json","rt", encoding='UTF8')
lecteurJSON = json.loads(f.read())
print(lecteurJSON)
print("*****************************************************")

i=0
for objet in lecteurJSON:
    if objet['fields']['etat']==2 :
        i+=1
        print(i)
        print(objet['fields']['nom'])

print("*****************************************************")
print(objet.keys())
print(objet['fields'].keys())
print(objet['fields']['nom'])

print("*****************************************************")
if objet['fields']['etat']==3 :
    print(objet['fields']['nom'])

f.close()