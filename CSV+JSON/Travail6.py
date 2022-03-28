import requests
import json

r = requests.get('https://data.nantesmetropole.fr/explore/dataset/323266205_indice-atmo-previsionnel-agglomeration-nantaise/download/?format=json&timezone=Europe/Berlin&lang=fr')
print(r.text)

print("***********************************")
tabJSON = json.loads(r.text)
i=0
for objetJSON in tabJSON:
    print("objet n°",i)
    if objetJSON['fields']['code_qual']>=2 :
            print(objetJSON['fields']['lib_zone'])
    i+=1
print("***********************************")
print("Exemple de données issues du dernier objet du fichier json:")
print(objetJSON['fields']['date_ech'])
print(objetJSON['fields']['lib_qual'])
print(objetJSON['fields']['lib_zone'])
