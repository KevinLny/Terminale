from Outils.pile_non_bornee import*

def calcule(express):
    P = creer_pile()
    operation = ["+","-","/","*"]
    for e in express:
        if e in operation:
            y = depiler(P)
            x = depiler(P)
            if e == "+":
                z=x+y
            if e == "-":
                z=x-y
            if e == "*":
                z=x*y
            if e == "/":
                z=x/y
            empiler(P, z)
        else:
            empiler(P, e)
    return depiler(P)

def calcule1(express):
    P = creer_pile()
    for e in express:
        if type(e) == int:
            empiler(P,e)
        if e in ["+","-","/","*"]:
            signe = e
            b = depiler(P)
            a = depiler(P)
            empiler(P, eval(f"{b}{signe}{a}"))
    return sommet(P)


def calculeNPI(express):
    P = creer_pile()
    for e in express.split():
        if e in ["+","-","/","*"]:
            signe = e
            b = depiler(P)
            a = depiler(P)
            empiler(P, eval(f"{b}{signe}{a}"))
        else:
            empiler(P, int(e))
    return sommet(P)

#rint(calcule([13,3,2,"+","*"]))
#print(calcule1([13,3,2,"+","*"]))
print(calculeNPI("13 3 2 + *"))
