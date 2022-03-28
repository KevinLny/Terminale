# Kevin Kuzu

#Fonction pile bornee

def creer_pile(n):
    P = [None]*(n+1)
    P[0]=0
    return P

def pile_vide(P):
    if P[0] == 0:
        return True
    else:
        return False

def pile_pleine(P):
    if P[0] == len(P)-1:
        return True
    else:
        return False

def empiler(P,x):
    if not pile_pleine(P):
        P[P[0]+1] = x
        P[0] = P[0]+1
    return P

def depiler(P):
    if not pile_vide == False:
        x = P[P[0]]
        P[P[0]] = None
        P[0] = P[0]-1
        return x

def taille(P):
    return P[0]

def sommet(P):
    if pile_vide(P) == False:
        return P[P[0]]

#______________________TEST__________________________

if __name__ == "__main__":
    a = creer_pile(5)
    print("liste a:",a)
    for i in range(5):
        empiler(a,i+1)
    print(a)
    print(pile_vide(a))
    b = creer_pile(8)
    print(pile_vide(b))
    print(pile_pleine(a))
    print(pile_pleine(b))
    x = depiler(a)
    print(x)
    print(a)