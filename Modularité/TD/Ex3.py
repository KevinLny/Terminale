from random import randint
from time import time

x = randint(0,100)
y = randint(0,100)
time = time()
somme = x+y
montemps=10
print("Que font ",x,"et" ,y)

while True:
    try :
        resutat=int(input("saisir un chiffre :"))
        y=time.time()-montemps
        if y >= montemps:  
                raise TimeoutError
        if resutat == somme:
            print("Bravo")
            break
        else: 
            print("Recommencer")
    except ValueError:
        print("Il faut saisir un chiffre")
