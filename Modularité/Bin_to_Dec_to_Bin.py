from tkinter import *
# Fenêtre tkinter
window = Tk()
window.geometry("200x170")
window.title("Bin_to_Dec_to_Bin")

#variable
resultat = StringVar()

# Fonction

def conv_bin_dec(expression):
    """[Cette fonction permet de convertire un nombre binaire]

    Args:
        expression ([Str]): [La valeur récuperé de la saise de texte]
    """
    assert (len(expression)<=8)
    a = int("".join(map(str,expression)),2)
    resultat.a.get()


def conv_bin_dec2(): 
    return conv_bin_dec(expression)

def conv_dec_bin(a_10):
   a_2=""
   while a_10 != 0 :
      r=a_10%2 #permet d'avoir le reste de la division
      a_2= str(r)+a_2 #permet de concaténer les deux chaines
      a_10=a_10//2
   return a_2

# the label for user_name 
Nombre_binaire = Label(window, text = "Saisissez un nombre binaire : ").place(x = 20, y = 20)
expression=""
Entrerdetext = Entry(window,width = 30, textvariable = expression).place(x = 10, y = 40)
print(expression) 


# the label for user_password  
Nombredecimale = Label(window, text = "En decimal :").place(x = 20,y = 80) 

sortie = Label(window, textvariable = expression).place(x = 75, y = 110)

submit_button = Button(window,text = "Validez",command= conv_bin_dec2).place(x = 75, y = 140)




#print(conv_bin_dec("10000000"))
window.mainloop()