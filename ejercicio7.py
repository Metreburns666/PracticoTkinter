from tkinter import *
import random

main=Tk()
main.title("Generador de Numeros")#nombre del titulo
main.geometry("300x300")#"primero lo ancho y dsp lo alto"
main.config(bg="dark orange")#color del fondo

def Random():
    num1=int(numEntry1.get())
    num2=int(numEntry2.get())
    if num1 > num2:
        numEntry3.set(random.randint(num2,num1)) 
    else:
        numEntry3.set(random.randint(num1,num2))


varFrame=Frame(main)
varFrame.pack()

numEntry1=IntVar()
numEntry1.set(0)

numEntry2=IntVar()
numEntry2.set(0)

numEntry3=IntVar()
numEntry3.set(0)

varLabel=Label(varFrame,text="Numero 1")
varLabel.grid(row=0,column=0,padx=5, pady=5)

varLabel2=Label(varFrame,text="Numero 2")
varLabel2.grid(row=1,column=0,padx=5, pady=5)

varLabel3=Label(varFrame,text="Numero Generado")
varLabel3.grid(row=2,column=0,padx=5, pady=5)

varEntry=Entry(varFrame,state="readonly",textvariable=numEntry3)
varEntry.grid(row=2,column=1,padx=5, pady=5)

varSpinbox=Spinbox(varFrame,state="readonly",from_=-999,to=999,textvariable=numEntry1)
varSpinbox.grid(row=0,column=1,padx=5, pady=5)

varSpinbox2=Spinbox(varFrame,state="readonly",from_=-999,to=999,textvariable=numEntry2)
varSpinbox2.grid(row=1,column=1,padx=5, pady=5)

varButton=Button(varFrame,text="Generar", command=Random)
varButton.grid(row=3,column=1,padx=5, pady=5)

main.mainloop()