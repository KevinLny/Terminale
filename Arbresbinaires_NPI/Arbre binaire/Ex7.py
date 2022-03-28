#Kevin Kuzu
from math import log2
from Ex5 import parent
from Ex6 import estFeuille, filsDroit, filsGauche

def taille(arbre):
    return len(arbre) - arbre.count(None)

def profondeur_rec(arbre, val, compteur=0):
    index = arbre.index(val)
    if index == 0:
        return compteur
    else:
        return profondeur(arbre, parent(arbre, val), compteur + 1)

def profondeur(arbre, val, compteur=0):
    indice = arbre.index(val)
    while indice > 0:
        val = parent(arbre, val)
        indice = arbre.index(val)
        compteur += 1
    return compteur

def listeFeuilles(arbre):
    L = []
    l = len(arbre)
    for i in range(l):
        if estFeuille(arbre,arbre[i]):
            L.append(arbre[i])
    return L

def hauteur(arbre):
    maxi = 0
    n = listeFeuilles(arbre)
    for i in n:
        prof1 = profondeur_rec(arbre,i)
        if prof1 > maxi:
            maxi = prof1
    return maxi

def hauteur2(arbre):
    n = len(arbre)+1
    n = log2(n)-2
    return n

#------------------ L'arbre -------------------------

def creation_arbre(r,hauteur):
    Arbre = [r]+ [None for i in range(2**(hauteur+2)-2)]
    return Arbre

def insertion_noeud(arbre,n,fg,fd):
    indice = arbre.index(n)
    arbre[2*indice+1]= fg
    arbre[2*indice+2] = fd

arbre = creation_arbre("R", 4)

insertion_noeud(arbre,"R","A","B")
insertion_noeud(arbre,"A","C","D")
insertion_noeud(arbre,"B","E","F")
insertion_noeud(arbre,"C",None,"H")
insertion_noeud(arbre,"D","I","J")
insertion_noeud(arbre,"E","K",None)
insertion_noeud(arbre,"J","M",None)
insertion_noeud(arbre,"K",None,"O")
#print(arbre)

#----------------- TEST ---------------------------- 
#print(taille(arbre))
"""print(profondeur(arbre, "A"))
print(profondeur(arbre, "B"))
print(profondeur(arbre, "C"))
print(profondeur_rec(arbre, "A"))
print(profondeur_rec(arbre, "B"))
print(profondeur_rec(arbre, "C"))"""
#print("listeFeuilles",listeFeuilles(arbre))
"""print(hauteur(arbre))
print(hauteur2(arbre))"""