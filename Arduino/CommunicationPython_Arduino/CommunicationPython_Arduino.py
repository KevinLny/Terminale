import serial
import tkinter

ser = serial.Serial('COM9', 9600, timeout=0.1)

def demandeConversion():
    ser.write(b"*")
    resultat.config(text=str(ser.read(4),encoding="ascii"))
    
fenetre=tkinter.Tk()
fenetre.title("AN0")

bouton=tkinter.Button(text="Lire AN0",command=demandeConversion)
bouton.grid(row=0,column=0,padx=30,pady=10)

resultat=tkinter.Label(text="????",font="helvetica,24")
resultat.grid(row=1,column=0)

fenetre.mainloop()