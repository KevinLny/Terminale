# Exercice 3
from random import randint
from File_poo import*

F1 = File()
F2 = File()
F4 = File()

def valeurF1():
    R1 = File()
    for i in range(randint(0,80)):
            R1.enfiler(randint(0,1))
    return R1

def valeurF2():
    R2 = File()
    for i in range(randint(0,80)):
            R2.enfiler(randint(0,1)*2)
    return R2

def valeurF4():
    R3 = File()
    for i in range(randint(0,80)):
            R3.enfiler(randint(0,1)*4)
    return R3

F1.contenu = valeurF1()
F2.contenu = valeurF2()
F4.contenu = valeurF4()

# Question 1 : F3 = [2,2,2,1,2,1,1]
# Question 2 : Le sommet F2 passe en prioritaire
# Question 3 : Le sommet F1 passe si le sommet de F2 = 0
# Question 4 : Le sommet F2 passe dans tout les cas
# Question 5 : Si l'une des deux files est vide alors faire passer tout les elément de la liste non vide

# Question 6 :

def croisement(F1 : File,F2 : File):
    F3 = File()
    while not F1.estVide() and not F2.estVide():
        if F1.sommet() == 1:
            if F2.sommet() == 0:
                F2.defiler()
            x = F1.defiler()
            F3.enfiler(x)

        elif F2.sommet() == 2 and F1.sommet() == 0:
                F1.defiler()
                x = F2.defiler()
                F3.enfiler(x)
        else:
            F3.enfiler(0)
            F2.defiler()
            F1.defiler()

    if F1.estVide():
        for i in range(F2.taille()-1):
            x = F2.defiler()
            F3.enfiler(x)

    elif F2.estVide():
        for i in range(F1.taille()):
            x = F1.defiler()
            F3.enfiler(x)
    return F3

#print(F1,F2)
#print(croisement(F1,F2))

# Question SUPP

def croisement(F1 : File,F2 : File, F4: File):
    F3 = File()
    sorti = File()
    while not F1.estVide() and not F2.estVide():
        if F1.sommet() == 1:
            if F2.sommet() == 0:
                F2.defiler()
            x = F1.defiler()
            F3.enfiler(x)

        elif F2.sommet() == 2 and F1.sommet() == 0:
                F1.defiler()
                x = F2.defiler()
                F3.enfiler(x)
        else:
            F3.enfiler(0)
            F2.defiler()
            F1.defiler()

    if F1.estVide():
        for i in range(F2.taille()-1):
            x = F2.defiler()
            F3.enfiler(x)
            

    elif F2.estVide():
        for i in range(F1.taille()):
            x = F1.defiler()
            F3.enfiler(x)
    
    while not F3.estVide() and not F4.estVide():
        if F4.sommet() != 0:
            if F3.sommet() == 0:
                F3.defiler()
            x = F4.defiler()
            sorti.enfiler(x)

        elif F3.sommet() != 0 and F4.sommet() == 0:
                F4.defiler()
                x = F3.defiler()
                sorti.enfiler(x)
        else:
            sorti.enfiler(0)
            F3.defiler()
            F4.defiler()
        
        if F3.estVide():
            for i in range(F4.taille()-1):
                x = F4.defiler()
                sorti.enfiler(x)
        
        if F4.estVide():
            for i in range(F3.taille()-1):
                x = F3.defiler()
                sorti.enfiler(x)
    return sorti

#print(F1,F2,F4)
print(croisement(F1,F2,F4))