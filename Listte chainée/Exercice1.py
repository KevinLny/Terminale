from liste_chaine_01 import *

nil = vide()
print(estVide(nil))


L = cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, nil))))))
print(L)

x, L = supprEnTete(L)
print(x)
print(L)

x,L = supprEnTete(L)
print(x)
print(L)