# Module tkinter
from tkinter import*
# Fenetre tkinter
root = Tk()
canvas = Canvas(root, width=600, height=300, background="white")
canvas.pack(fill="both", expand=True)
#Un rectangle
canvas.create_rectangle(50,50,150,100,width=2)
#Un rectangle à gros bord bleus
canvas.create_rectangle(200,50,300,150,width=5, outline="blue")
# Un rectangle remplis de violet 
canvas.create_rectangle(350,100,500,150,fill="purple")
# Un oval
canvas.create_oval(50,110,180,160,width=4)
# Du texte
canvas.create_text(400,75,text="Blablablabla", fill="red")
# Ouverture de la fenêtre
root.mainloop()