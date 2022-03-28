from random import randint

def contient_doublon(t):
    '''Le tableau contient-il un doublon?'''
    s=0
    for x in t:
        if s & (1<<x) !=0:
            print("*"*100)
            print("Doublon trouvé : ", x)
            return True #Arrete la fontion
        s=s| (1<<x)
        print("S=",bin(s))
    print("*"*100)
    return False

dates=[randint(1,366) for _ in range(35)]
print("Listes des jours de naissances",dates)
print("*"*100)
print(contient_doublon(dates))