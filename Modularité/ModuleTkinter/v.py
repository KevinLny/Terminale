from random import* 

liste = [randint(1,20) for i in range(10)]
print(liste)

def changer_liste():
    global liste
    liste=[randint(1,20) for i in range(10)]
    
    

print(changer_liste())
print(liste)