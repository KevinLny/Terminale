# Kevin Kuzu

#Fonction file non bornnée


def creer_file():
    """Creer une file

    Returns:
        list: list file
    """
    return []

def enfiler(F,x):
    """Ajoute une valeur dans la liste file

    Args:
        F (list): list file
        x (int): add an item

    Returns:
        list : list file
    """
    F.append(x)
    return F

def defiler(F):
    """Enlève la première valeur

    Args:
        F (list): list file

    Returns:
        list: list file
    """
    if not file_vide(F):
        return F.pop(0)

def file_vide(F):
    """Savoir si la liste est file vide

    Args:
        F (list): list file

    Returns:
        Bool: True or false
    """
    if len(F) == 0:
        return True
    else:
        return False

def taille(F):
    """permet de savoir  la taile de la liste file

    Args:
        F (list): list file

    Returns:
        int: La taille de la liste F
    """
    return len(F)

def tete(F):
    """Donne la première valeur de la list file

    Args:
        F (list): List file 

    Returns:
        int: La première valeur de la list file
    """ 
    return F[0]

#___________________________________TEST______________________

if __name__ == "__main__":
    a = creer_file()
    for i in range(10):
        enfiler(a,i+1)
    b = creer_file()
    print(a)
    print(file_vide(a))
    print(file_vide(b))
    print(taille(a))
    print(tete(a))
    print(defiler(a))