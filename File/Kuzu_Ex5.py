from utils.pile_non_bornee import*

def enfiler(F, x):
    return empiler(F,x)

def defiler(F):
    s = creer_pile()
    for i in range(taille(F)-1):
        empiler(s,depiler(F))
    b = depiler(F)
    for i in range(taille(s)):
        empiler(F,depiler(s))
    return b

l=[1,2,3,4,5]
a = defiler(l)
print(a,l)

def depilerbis(P):
    s = creer_pile()
    for i in range(taille(P)-1):
        enfiler(s, defiler(P))
    b = defiler(P)
    for i in range(len(s)):
        enfiler(P, defiler(s))
    return b

r=[1,2,3,4,5]
o = depilerbis(r)
print(o,r)