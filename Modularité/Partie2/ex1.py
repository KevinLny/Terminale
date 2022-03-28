from random import randint

def contient_doublon(t):
    '''Le tableau contient-il un doublon?'''
    s=[]
    for x in t:
        if x in s:
            print("*"*10)
            print("Doulon troucé : ", x)
            return True #Arrete la fontion
        s.append(x)
        print("S=",s)
    print("*"*10)
    return False

dates=[randint(1,366) for _ in range(35)]
print("Listes des jours de naissances",dates)
print("*"*10)
print(contient_doublon(dates))