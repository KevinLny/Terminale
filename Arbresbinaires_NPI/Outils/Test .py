import pile_non_bornee

Pilevide = creer_pile()
print(Pilevide)
l= [1,2,3,4,5]
for i in range(5):
    empiler(Pilevide, depiler(l))
    print(Pilevide)
print(pile_vide(l))