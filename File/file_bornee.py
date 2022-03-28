# Kevin Kuzu

#Fonction file bornnée

def creer_file(n):
    F = [None] * (n+3)
    F[0] = 3
    F[1] = 3
    F[2] = 0
    return F

def file_vide(F):
    """Fonction qui permet de savoir si la file est vide ou non

    Args:
        F (list): La file

    Returns:
        Bool: Si True file vide
    """
    if F[2] == 0:
        return True
    else:
        return False

def file_pleine(F):
    """Fonction qui permet de savoir si la file est pleine ou non

    Args:
        F (List): La file

    Returns:
        Bool: Si True file pleine

    >>> file_pleine([3,3,4,1,2,3,4])
    True

    >>> file_pleine([3,3,4,1,2,3,4,None,None,None])
    False

    """
    if F[2] == len(F)-3:
        return True
    else:
        return False

def capacite(file):
    return len(file)-3

def indiceTete(file):
    return file[0]

def indiceQueue(file):
    if file_vide(file):
        if file[1] == 3:
            return len(file)-1
        else:
            return file[1]-1

def longeur(file):
    return file[2]

def tete(file):
    if not file_vide(file):
        return file[file[0]]
    else:
        return None

def Queue(file):
    if file_vide(file)==False:
        if file[1] == 3:
            return file[len(file)-1]
        else:
            return file[file[1]-1]

def indDisponible(file):
    return file[1]

def defiler(file):
    """Fonction qui permet de defiler une file bornnée

    Args:
        file (list): file bornée

    Returns:
        x: la valeur de la tete

    >>> defiler([3,3,2,5,6])
    5

    >>> defiler([4,3,1,None,10])
    10

    """
    if file_vide(file)==False:
        x = file[file[0]]
        if file[0] == len(file) - 1:
            file[0]=3
        else:
            file[0]=file[0]=1
        file[2] = file[2]-1
        return x

def enfiler(file,x):
    """Fonction qui permet de enfiler une file bornée   

    Args:
        file (list): file bornée
        x (int): La valeur ajouté à la file bornée

    Returns:
        file: file bornée


    >>> enfiler([3,5,2,10,8,None,None],5)
    [3, 6, 3, 10, 8, 5, None]

    >>> enfiler([3,3,3,None,8,7,6],5)
    [3, 4, 4, 5, 8, 7, 6]
    """
    if not file_pleine(file):
        file[file[1]]=x
        if file[1]==len(file)-1:
            file[1]=3
        else:
            file[1] += 1
        file[2]+=1
        return file



if __name__ == "__main__":
    from doctest import*
    testmod()