from tkinter import*
from random import*

root = Tk()
canvas = Canvas(root, width=600, height=600, background="white")
canvas.pack(fill="both", expand=True)

liste = [randint(1,20) for i in range(10)]

def changer_liste():
    global liste
    liste=[randint(1,20) for i in range(10)]

colors=["red","purple","white","black","yellow","brown","green"]

def action_bouton():
    canvas.delete("all")        #Efface tout
    couleurs=["red","purple","white","black","yellow","brown","green"]
    coul= choice(couleurs)      #couleur au hasard
    canvas.create_rectangle(100,50,300,150, width=5, fill=coul)
    return

# Le graphique en barre
def graphique_bares(liste):
    canvas.delete("all")
    zoom=10
    pas=20
    lb=10
    x=260
    y=400
    for i in liste:
        canvas.create_rectangle(x,y,x+lb,y-(i*zoom), width=2, fill="red", outline="black")
        x=x+pas

def graphique_cumulatif(liste):
    canvas.delete("all")        #Efface tout
    zoom=4
    pas=0
    lb=50
    x=300
    y=600
    for i in liste:
        y=y-(i*zoom)
        canvas.create_rectangle(x, y, x+lb, y+(i*zoom),width=2, fill=colors[randint(0,5)])

bouton_barres = Button(root,text="Graphique en barres", width=20, command= lambda:graphique_bares(liste))
bouton_barres.pack(pady=10)

bouton_cumulatif = Button(root,text="Graphique cumulatif", width=20, command= lambda:graphique_cumulatif(liste))
bouton_cumulatif.pack(pady=10)

bouton_donne = Button(root,text="Changer les données", width=20, command= changer_liste)
bouton_donne.pack(pady=10)

bouton_quitter = Button(root,text="Quitter", width=20, command=root.quit)
bouton_quitter.pack(side=BOTTOM, pady=10)



root.mainloop()