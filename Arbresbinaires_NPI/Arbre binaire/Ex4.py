# Kevin Kuzu

def creation_arbre(r,hauteur):
    Arbre = [r]+ [None for i in range(2**(hauteur+2)-2)]
    return Arbre

def insertion_noeud(arbre,n,fg,fd):
    indice = arbre.index(n)
    arbre[2*indice+1]= fg
    arbre[2*indice+2] = fd

# Question supp

def niemeoccurence2(tab, n, v):
    if n<= tab.count(v):
        long = len(tab)
        j = 0
        i = 0
    while i < n and j < long:
        if tab[j] == v:
            i=i+1
        j=j+1
    return j-1

def insertion_noeud2(arbre,n,fg,fd,occ=1):
    indice = niemeoccurence2(arbre,occ,n)
    arbre[2*indice+1] = fg
    arbre[2*indice+2] = fd

# ----------------------------------------------

arbre = creation_arbre("R", 4)

insertion_noeud(arbre,"R","A","B")
insertion_noeud(arbre,"A","C","D")
insertion_noeud(arbre,"B","E","F")
insertion_noeud(arbre,"C",None,"H")
insertion_noeud(arbre,"D","I","J")
insertion_noeud(arbre,"E","K",None)
insertion_noeud(arbre,"J","M",None)
insertion_noeud(arbre,"K",None,"O")
"""print(len(arbre))
print(arbre)"""

arbre2 = creation_arbre("x", 3)

insertion_noeud2(arbre2,"x","+","+")
insertion_noeud2(arbre2,"+",'2','3',1)
insertion_noeud2(arbre2,"+",'4',"*",2)
insertion_noeud2(arbre2,"*",'5','3')

"print('arbre2: ', arbre2)"