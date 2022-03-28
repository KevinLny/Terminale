# Kevin Kuzu

from Ex6 import arbreVide, filsDroit, filsGauche
from Ex7 import hauteur, profondeur

def sousArbre(arbre, ind):
    if arbre[ind] == None:                           # Si la valeur de l'arbre à l'indice est égale à None
        return []                                       # On retourne une liste vide
    else:
        profRacine = profondeur( arbre, arbre[ind])  # 
        haut = hauteur(arbre)
        nbligneSSarbre = haut - profRacine
        ssarbre = creation_arbre(arbre[ind], nbligneSSarbre)
        indarbre = [ind]
        i = 0
        c = 1
        while c<len(ssarbre):
            id = indarbre[i]
            fg = filsGauche(arbre, arbre[id])
            indarbre.append(2*id+1)
            c = c+1
            fd = filsDroit(arbre, arbre[id])
            indarbre.append(2*id+2)
            c = c+1
            insertion_noeud(ssarbre, arbre[id], fg, fd)
            i = i+1
        h = hauteur(ssarbre)
        ssarbre2=creation_arbre(ssarbre[0],h)
        m=len(ssarbre2)
        for i in range(m):
            ssarbre2[i]=ssarbre[i]
        return ssarbre2
"""
def sousArbreGauche(arbre, inndice):"""

#------------------ L'arbre -------------------------

def creation_arbre(r,hauteur):
    Arbre = [r]+ [None for i in range(2**(hauteur+2)-2)]
    return Arbre

def insertion_noeud(arbre,n,fg,fd):
    indice = arbre.index(n)
    arbre[2*indice+1]= fg
    arbre[2*indice+2] = fd

arbre1 = creation_arbre("R", 4)

insertion_noeud(arbre1,"R","A","B")
insertion_noeud(arbre1,"A","C","D")
insertion_noeud(arbre1,"B","E","F")
insertion_noeud(arbre1,"C",None,"H")
insertion_noeud(arbre1,"D","I","J")
insertion_noeud(arbre1,"E","K",None)
insertion_noeud(arbre1,"J","M",None)
insertion_noeud(arbre1,"K",None,"O")

#----------------- TEST ---------------------------- 

def sousabregauche(arbre, indice):
    return sousArbre(arbre, (2*indice+2))

def sousarbredroit(arbre, indice):
    return sousArbre(arbre, (2*indice+1))

'''print(sousarbredroit(arbre1,2))
print(sousabregauche(arbre1,2))'''

L = []

def parcoursPrefixe(arbre):
    if arbreVide(arbre) == False:
        L.append(arbre[0])
        parcoursPrefixe(sousabregauche(arbre, 0))
        parcoursPrefixe(sousarbredroit(arbre, 0))

print("ici",parcoursPrefixe(arbre1))