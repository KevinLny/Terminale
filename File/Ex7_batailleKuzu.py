from random import shuffle
from utils.file_non_bornee import*
from time import sleep

nbCarte = 32
L = [i for i in range(nbCarte)]
shuffle(L)
print(L)

J1 = creer_file()
J2 = creer_file()

for i in range(16):
    enfiler(J1,L.pop())
    enfiler(J2,L.pop())

print(J2,J1)

def jeu(J1,J2):
    while len(J1) != 0 and len(J2) != 0:
        carteJ1 = defiler(J1)
        carteJ2 = defiler(J2)
        main = creer_file()
        if carteJ1>carteJ2:
            enfiler(main,carteJ1)
            enfiler(main,carteJ2)
            shuffle(main)
            enfiler(J1,defiler(main))
            enfiler(J1,defiler(main))
            print(J1)
            print(J2)
            sleep(0.1)
        elif carteJ1<carteJ2:
            enfiler(main,carteJ1)
            enfiler(main,carteJ2)
            shuffle(main)
            enfiler(J2,defiler(main))
            enfiler(J2,defiler(main))
            print(J1)
            print(J2)
            sleep(0.1)
    if len(J1) == 0:
        return "Le gagnant est :J2"
    if len(J2) == 0:
        return "Le gagnant est :J1"

print(jeu(J1,J2))