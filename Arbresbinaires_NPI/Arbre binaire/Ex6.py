# Kevin Kuzu

def arbreVide(arbre):
    """Fonction qui permet de savoir si l'arbre est vide ou non

    Args:
        arbre : Arbre binaire

    Returns:
        bool: True or False
    """
    return arbre.count(None) == len(arbre)

def enfants(arbre,val):
    """Fonction qui donne les fils d'un noeud père il retourne les clé des noeuds

    Args:
        arbre (): L'arbre binaire
        val (Str ou un INT): La valeur rechèrcher dans l'arbre

    Returns:
        Str: les clé des fils 
    """
    if not arbreVide(arbre):
        fils1 = (arbre[2*(arbre.index(val)+1)])
        fils2 = (arbre[2*(arbre.index(val)+2)])
    return fils1,fils2

def filsGauche(arbre, val):
    filsgauche = enfants(arbre, val)
    return filsgauche[0]

def filsDroit(arbre, val):
    filsdroit = enfants(arbre,val)
    return filsdroit[1]

def estRacine(arbre,val):
    return arbre[arbre.index(val)] == arbre[0]

def estFeuille(arbre,val):
    return enfants(arbre,val) == (None, None)

def avoirFrere(arbre,val):
    if not estRacine(arbre,val):
        noeud = arbre.index(val)
        if noeud%2 == 0:
            return arbre[noeud-1] != None
        else:
            return arbre[noeud+1] != None



#------------------ L'arbre -------------------------

def creation_arbre(r,hauteur):
    Arbre = [r]+ [None for i in range(2**(hauteur+2)-2)]
    return Arbre

def insertion_noeud(arbre,n,fg,fd):
    indice = arbre.index(n)
    arbre[2*indice+1]= fg
    arbre[2*indice+2] = fd

arbre = creation_arbre(None, 1)

#print(arbreVide(arbre))     # Fonction est vide

arbre = creation_arbre("A", 1)
insertion_noeud(arbre,"A","B","C")
#print(arbre)

#----------------- TEST ---------------------------- 
"""if __name__ == '__main__':
    print(enfants(arbre, 'A'))  # Fonction qui donne les enfant du noeuds père
    print(filsGauche(arbre, 'A'))
    print(filsDroit(arbre, 'A'))
    print(estRacine(arbre,'A'))
    print(estFeuille(arbre, 'A'))
    print(estFeuille(arbre, 'B'))
    print(estFeuille(arbre, 'C'))
    print(avoirFrere(arbre, 'A'))
    print(avoirFrere(arbre, 'B'))
    print(avoirFrere(arbre, 'C'))"""