
from utils.file_non_bornee import*
def creer_pile():
    F1 = creer_file()
    F2 = creer_file()
    return F1, F2

def empiler(pile, valeur):
    enfiler(pile[0], valeur)
    return pile

def depiler(pile):
    print(pile[0])
    while taille(pile[0]) > 1:
        x = defiler(pile[0])
        enfiler(pile[1],x)
    v = defiler(pile[0])
    while file_vide(pile[1]) == False:
        x = defiler(pile[1])
        enfiler(pile[0], x)
    return v

P = creer_pile()
empiler(P,1)
empiler(P,2)
empiler(P,3)
empiler(P,4)

#a = depiler(l)
print(P)
a = depiler(P)
print(a)