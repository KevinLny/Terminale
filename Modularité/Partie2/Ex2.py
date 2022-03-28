from random import randint

def contient_doublon(t):
    '''Le tableau contient-il un doublon?'''
    s=[False]*367
    for x in t:
        if s[x]:
            print("*"*100)
            print("Doulon troucé : ", x)
            return True #Arrete la fontion
        s[x]=True
        print("S=",s)
    print("*"*100)
    return False

dates=[randint(1,366) for _ in range(35)]
print("Listes des jours de naissances",dates)
print("*"*100)
print(contient_doublon(dates))