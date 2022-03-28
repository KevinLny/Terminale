# Créé par kuzu9, le 09/09/2021 en Python 3.7
def nombre_de_cartes(n : int)-> int:
    '''
    Fonction qui permet de calculer le nombre necéssaire afin de construire
    un chateau de carte de 'n' d'étage.
    '''
    somme=0                             # Somme prend la valeur 0 -> int
    for etage in range(1,n+1):          # On fais une boucle borné (Un for)
        somme=somme + etage * 3 - 1     # Somme prend la valeur somme + etage * 3 - 1
    return somme                        # On retoure sommz dans la console

#nb_carte = int(input("Quel est le nombre d'étage que vous voulez ?"))
#print(nombre_de_cartes(nb_carte))

def chateau_plus_haut(nombre = int)-> int:
    assert nombre >=0
    etage = 0
    while nombre_de_cartes(etage+1) <= nombre:
        etage=etage+1
    
    return etage



print(chateau_plus_haut(100))


