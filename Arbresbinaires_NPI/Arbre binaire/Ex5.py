# Kevin Kuzu

def creation_arbre(r,hauteur):
    Arbre = [r]+ [None for i in range(2**(hauteur+2)-2)]
    return Arbre

def parent(arbre,p):
    """Cette fonction retourne le père ou la racine de la clé donnée

    Args:
        arbre: Arbre binaire
        p (str): valeur recherché

    Returns:
        str: Parents ou racine de la valeur p
    """
    if p in arbre:                      # Si p est dans l'arbre
        indice = arbre.index(p)         # l'indice est égale à l'indice de la valeur donnée p
        if indice % 2 == 0:             # si indice est divisable par 2 en ayant pour reste 0
            return arbre[(indice-2)//2] # On retourne de l'arbre à l'indice -2 //2 sa valeur
        else:                           # Sinon
            return arbre[(indice-1)//2] # On retourne de l'arbre à l'indice -1 //2 sa valeur

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

# ---------------------------------------
arbre2 = creation_arbre("x", 3)

insertion_noeud2(arbre2,"x","+","+")
insertion_noeud2(arbre2,"+",'2','3',1)
insertion_noeud2(arbre2,"+",'4',"*",2)
insertion_noeud2(arbre2,"*",'5','3')
""""
    print('arbre2: ', arbre2)
    print(parent(arbre2, '4'))"""