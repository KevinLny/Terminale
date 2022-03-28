try:
    age= int(input("Age : "))   #Demande l'age
    assert age > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'age saisie est inférieure ou égale à 0")