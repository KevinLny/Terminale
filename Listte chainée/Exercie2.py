from liste_chaine_01 import*

def longueur_w(L):
  Nbcellule = 0            #1
  while not estVide(L):    # n
    x ,L = supprEnTete(L)  # 4n
    Nbcellule += 1         # 2n
  return "Le nombre de cellule est égale à :", Nbcellule

# La complexité de longueur_w() = T= O(n) = 1 + 7n

#print(longueur_w(cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, None))))))))

def longueur_rec(L, x = 0):
  if estVide(L):        # 1+1+1
    return x            
  else:
    return longueur_rec(supprEnTete(L)[1], x+1) #n(1+1+1+1)

# La complexité de longueur_rec() = T= O(n) = 3 + 4n
#print(longueur_rec(cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, None))))))))

def nieme_element_w(n,L):
  if longueur_rec(L) <= n:   # 1+1+1
    return None
  elif n == 0:              # 1+1+1
    return supprEnTete(L)[0] #+1
  else:
    for i in range(n+1):    # n+1
      x , L = supprEnTete(L)  # N(1+1+1+1)
    return x

# La complexité de nieme_element_w() = T= O(n) = 6 + 5n

def nieme_element_rec(n,L):
  if longueur_rec(L) <= n:      # 1+1+1+1
    return None
  elif n == 0:                  # 1+1+1
    return supprEnTete(L)[0]    # 1+1
  else:
    return nieme_element_rec(n-1, supprEnTete(L)[1])  # n(1+1+1)

# La complexité de nieme_element_w() = T= O(n) = 9 + 3n

L = cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, None))))))
"""for i in range(longueur_rec(L)):
  print("Avec le while , pour i=",i,":",nieme_element_w(i,cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, None))))))))
  print("Avec la récursivité , pour i=",i,":",nieme_element_rec(i,cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, None))))))))"""
#print(nieme_element_w(6,L))
#print(nieme_element_rec(6,L))


def concattenation(L1, L2):
  long = longueur_rec(L1)   # long prend la valeurs d nombre d'éléments dans L1
  L = L2                    # L prend la valeur de L2
  for i in range(long):
    a = nieme_element_w(long-1-i,L1)  # a prend comme valeur n-1-i elément de L1
    L = ajouteEnTete(L,a)             
  return L

L1 = cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, None))))))
L2 = cons(0, cons(18000000, cons(2, cons(3, cons(4, cons(5, None))))))

#print(L1,L2)
#print(concattenation(L1, L2))

def insersion(lst,pos,val):
  L = lst                     # On defini une copie de lst
  for i in range(pos):        # on effectue une boucle bornée allant de 0 à pos
    L=L[1]
  L = ajouteEnTete(L,val)     # On ajoute la valeur val dans la liste chaine 
  for i in range(pos):        # on effectue une boucle bornée allant de 0 à pos
    a = nieme_element_w(pos-1-i,lst)
    L=ajouteEnTete(L,a)
  return L

L3 = cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, None))))))
#print(insersion(L3,2,"val"))

def reverse_f(lst):
  long = longueur_rec(lst)
  L = vide()
  for i in range(long):
    a = nieme_element_w(i,lst)
    L = ajouteEnTete(L,a)
  return L

print(reverse_f(L3))

#def reverse_rec(lst, res):