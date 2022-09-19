from tkinter import *
from tkinter import messagebox

main=Tk()
main.title("Calculadora")#nombre del titulo
main.geometry("300x200")#"primero lo ancho y dsp lo alto"
main.config(bg="DarkGray")#color del fondo

def Suma():
    num1=int(numeroEntry.get())
    num2=int(numeroEntry2.get())
    numeroEntry3.set(num1+num2)

def Resta():
    num1=int(numeroEntry.get())
    num2=int(numeroEntry2.get())
    numeroEntry3.set(num1-num2)

def Multiplicacion():
    num1=int(numeroEntry.get())
    num2=int(numeroEntry2.get())
    numeroEntry3.set(num1*num2)
def Division():
    num1=int(numeroEntry.get())
    num2=int(numeroEntry2.get())
    if num2==0:
        messagebox.showinfo(message="Error - No se puede dividir por 0")
    else:
        numeroEntry3.set(num1/num2)

def Calcular():
    opBotton=int(opRadioButton.get())
    if opBotton==1:
        Suma()
    if opBotton==2:
        Resta()
    if opBotton==3:
        Multiplicacion()
    if opBotton==4:
        Division()

varFrame=Frame(main)
varFrame.pack()

numeroEntry=IntVar()
numeroEntry.set(0)
numeroEntry2=IntVar()
numeroEntry2.set(0)
numeroEntry3=IntVar()
numeroEntry3.set(0)

opRadioButton= IntVar()
txtenResultado=StringVar()
txtenResultado.set("")


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

radButtonSum = Radiobutton(varFrame,text= "Sumar", variable=opRadioButton, value=1)
radButtonSum.grid(row=1, column=3, padx=5, pady=5)

radButtonRes = Radiobutton(varFrame,text= "Restar", variable=opRadioButton, value=2)
radButtonRes.grid(row=2, column=3, padx=5, pady=5)

radButtonMult = Radiobutton(varFrame,text= "Multiplicar", variable=opRadioButton, value=3)
radButtonMult.grid(row=3, column=3, padx=5, pady=5)

radButtonDiv = Radiobutton(varFrame,text= "Dividir", variable=opRadioButton, value=4)
radButtonDiv.grid(row=4, column=3)

varButton=Button(varFrame,text="Calcular", command=Calcular)
varButton.grid(row=4,column=1, padx=5, pady=5)

main.mainloop()