# Kevin Kuzu

#Fonction pile non bornnée

def creer_pile():
    """[Creer une pile vide]

    Returns:
        [Liste]: [Vide]
    """
    return []

def empiler(P, x):
    """[Rajoute une valeur dans la liste ]

    Args:
         P ([liste]): [Elle est vide ou non]
         x ([int]): [On l'ajoute dans la fonction]

    Returns:
          [type]: [description]
    """
    return P.append(x)
    
def depiler(P):
    """[Enlève la dèrniere valeur de la liste P]

    Args:
        P ([liste])

    Returns:
        [P.pop]: [Dernière]
    """
    if P!=[]:
        return P.pop()

# Fonction auxilière

def pile_vide(P):
    """Permet de savoir si la liste est vide ou non

    Args:
        P ([Liste]): [Vide ou non]

    Returns:
        [Booléen]: [True or False]
    """
    if len(P) == 0:
        return True
    else:
        return False

def taille(P):
    """Permet de savoir la taille de la liste

    Args:
        P ([Liste]): [Vide ou non]

    Returns:
        [int]: [Taille de P]
    """
    return len(P)

def sommet(P):
    """La plus haute donnée de laliste P

    Args:
        P ([Liste]): [Vide ou non]

    Returns:
        [int]: [La plus haute donnée]
    """
    if pile_vide(P)==False:
          return P[taille(P)-1]

# ============================================================#
# Fonction  TEST
# ============================================================#

if __name__ == "__main__":
    Pilevide = creer_pile()
    print(Pilevide)
    l= [1,2,3,4,5]
    for i in range(5):
        empiler(Pilevide, depiler(l))
        print(Pilevide)
    print(pile_vide(l))
