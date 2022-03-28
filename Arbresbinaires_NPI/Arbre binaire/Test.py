

#def enleverNone(arbre):










#-------------------------------------------------

def creation_arbre(r,hauteur):
    Arbre = [r]+ [None for i in range(2**(hauteur+1)-2)]
    return Arbre

def insertion_noeud(arbre,n,fg,fd):
    indice = arbre.index(n)
    arbre[2*indice+1]= fg
    arbre[2*indice+2] = fd

arbre = creation_arbre("A", 1)
insertion_noeud(arbre,"A","B","C")
print(arbre)