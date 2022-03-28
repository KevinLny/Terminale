from utils.pile_non_bornee import*

def creer_file():
    P1 = creer_pile()
    P2 = creer_pile()
    return P1, P2

def enfiler(file, valeur):
    empiler(file[0], valeur)
    return file

def defiler(file):
    while pile_vide(file[0]) == False:
        x = depiler(file[0])
        empiler(file[1],x)
    v = depiler(file[1])
    while pile_vide(file[1]) == False:
        x = depiler(file[1])
        empiler(file[0], x)
    return v

#l= ([1,2,3,4,5], [])
#a = defiler(l)
#print(l,a)
#enfiler(l, a)
#print(l,a)
