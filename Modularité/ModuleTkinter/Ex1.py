# Module tkinter
from tkinter import*
# Fenetre tkinter
root = Tk()
canvas = Canvas(root, width=600, height=600, background="white")
canvas.pack(fill="both", expand=True)

from random import*

colors=["red","purple","white","black","yellow","brown","green"]

# Le graphique en barre
def graphique_bares(liste):
    zoom=10
    pas=20
    lb=10
    x=260
    y=400
    for i in liste:
        canvas.create_rectangle(x,y,x+lb,y-(i*zoom), width=2, fill="red", outline="black")
        x=x+pas

liste = [randint(1,20) for i in range(10)]
print(liste)
print(graphique_bares(liste))

def graphique_cumulatif(liste):
    zoom=4
    pas=0
    lb=50
    x=300
    y=600
    for i in liste:
        y=y-(i*zoom)
        canvas.create_rectangle(x, y, x+lb, y+(i*zoom),width=2, fill=colors[randint(0,5)])

#print(graphique_cumulatif(liste))

# Ouverture de la fenêtre
root.mainloop()