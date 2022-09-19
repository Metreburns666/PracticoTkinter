from tkinter import *
from tkinter import messagebox

main=Tk()
main.title("Calculadora")#nombre del titulo
main.geometry("300x200")#"primero lo ancho y dsp lo alto"
main.config(bg="DarkGray")#color del fondo

def Calcular():
    pass


varFrame=Frame(main)
varFrame.pack()

numeroEntry=IntVar()
numeroEntry.set(0)
numeroEntry2=IntVar()
numeroEntry2.set(0)
numeroEntry3=IntVar()
numeroEntry3.set(0)

varLabel=Label(varFrame, text="Operaciones")
varLabel.grid(row=0,column=3, padx=5, pady=5)

varLabel2=Label(varFrame, text="Valor 1")
varLabel2.grid(row=1,column=0)

varLabel3=Label(varFrame, text="Valor 2")
varLabel3.grid(row=2,column=0)

varLabel4=Label(varFrame, text="Resultado")
varLabel4.grid(row=3,column=0)

varEntry=Entry(varFrame,textvariable= numeroEntry)
varEntry.grid(row=1,column=1, padx=5, pady=5)

varEntry2=Entry(varFrame,textvariable= numeroEntry2)
varEntry2.grid(row=2,column=1, padx=5, pady=5)

varEntry3=Entry(varFrame,state="readonly", textvariable= numeroEntry3)
varEntry3.grid(row=3,column=1, padx=5, pady=5)

varButton=Button(varFrame,text="Calcular", command=Calcular)
varButton.grid(row=4,column=1, padx=5, pady=5)


main.mainloop()