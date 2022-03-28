from random import randint
from module import creer,contient,ajoute

def contient_doublon(t):
    '''Le tableau contient-il un doublon?'''
    s=creer()
    for x in t:
        if contient(s,x):
            print("*"*100)
            print("Doublon trouvé : ", x)
            return True #Arrete la fontion
        ajoute(s,x)
        print("S=",s)
    print("*"*100)
    return False

dates=[randint(1,366) for _ in range(35)]
print("Listes des jours de naissances",dates)
print("*"*100)
print(contient_doublon(dates))