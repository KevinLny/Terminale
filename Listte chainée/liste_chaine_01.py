# Kevin Kuzu
# Première version de liste chainée. Primaire



def vide():
  """Fonction qui creer un None

  Returns:
      None: retourne rien
  """
  return None

def cons(x,L):
  return (x,L)

def ajouteEnTete(L,x):
  return cons(x,L)

def supprEnTete(L):
  return (L[0],L[1])

def estVide(L):
  return L == None

def longueur_rec(L, x = 0):
  if estVide(L):        
    return x
  else:
    return longueur_rec(supprEnTete(L)[1], x+1)

def longueur_w(L):
  Nbcellule = 0            #1
  while not estVide(L):    # n
    x ,L = supprEnTete(L)  # 4n
    Nbcellule += 1         # 2n
  return Nbcellule

def nieme_element_w(n,L):
  if longueur_rec(L) < n:   # 1+1+1
    return None
  elif n == 0:              # 1+1+1
    return supprEnTete(L)[0] #+1
  else:
    for i in range(n+1):    # n+1
      x , L = supprEnTete(L)  # N(1+1+1+1)
    return x

def nieme_element_rec(n,L):
  if longueur_rec(L) <= n:      # 1+1+1+1
    return None
  elif n == 0:                  # 1+1+1
    return supprEnTete(L)[0]    # 1+1
  else:
    return nieme_element_rec(n-1, supprEnTete(L)[1])  # n(1+1+1)

# Kevin Kuzu

def renverse_rec(liste, l=vide()):
  if 0 < longueur_rec(liste):
    return renverse_rec(liste[1],ajouteEnTete(l, liste[0]))
  else:
    return l