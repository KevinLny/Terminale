from utils.pile_non_bornee import*

def ouvrante_associee(s, f):
    pile = creer_pile()
    for i in range(f):
        if s[i] == '(':
            empiler(pile, i)
        elif s[i] == ")":
            depiler(pile)
    return sommet(pile)

print(ouvrante_associee("8*((3*(5+2))/(3+2))",11))