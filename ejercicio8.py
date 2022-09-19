from tkinter import *
from tkinter import messagebox

main=Tk()
main.title("Calculadora 2")#nombre del titulo
main.geometry("400x250")#"primero lo ancho y dsp lo alto"
#main.config(bg="DarkGray")#color del fondo

def Validar():
    contVal = 2
    a=0
    try:
        float(numeroEntry.get())
        contVal -= 1
    except:
        a=1
    try:
        float(numeroEntry2.get())
        contVal -= 1
    except:
        numeroEntry2.set("0")
        a=2
    if contVal!=0:
        if contVal==2:
            numeroEntry.set("0")
            numeroEntry2.set("0")
            numeroEntry3.set("0")
            messagebox.showinfo(message="Error en Valor 1 y Valor 2- Ingrese solo numeros por favor")
        if contVal==1:
            if a==1:
                numeroEntry.set("0")
                numeroEntry3.set("0")
                messagebox.showinfo(message="Error en Valor 1- Ingrese solo numeros por favor")
            if a==2:
                numeroEntry2.set("0")
                numeroEntry3.set("0")
                messagebox.showinfo(message="Error en Valor 2- Ingrese solo numeros por favor") 
    return contVal == 0

def Suma():
    if Validar()==True:
        num1=float(numeroEntry.get())
        num2=float(numeroEntry2.get())
        numeroEntry3.set(str(num1+num2))
    else:
        pass

def Resta():
    if Validar()==True:
        num1=float(numeroEntry.get())
        num2=float(numeroEntry2.get())
        numeroEntry3.set(str(num1-num2))
    else:
        pass

def Multiplicacion():
    if Validar()==True:
        num1=float(numeroEntry.get())
        num2=float(numeroEntry2.get())
        numeroEntry3.set(str(num1*num2))
    else:
        pass

def Division():
    if Validar()==True:
        num1=float(numeroEntry.get())
        num2=float(numeroEntry2.get())
        if num2==0:
            messagebox.showinfo(message="Error - No se puede dividir por 0")
        else:
            numeroEntry3.set(str(num1/num2))
    else:
        pass
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

varFrame=Frame(main,padx=20, pady=20)
varFrame.pack()

numeroEntry=StringVar()
numeroEntry.set("0")
numeroEntry2=StringVar()
numeroEntry2.set("0")
numeroEntry3=StringVar()
numeroEntry3.set("0")

opRadioButton= IntVar()

varLabel=Label(varFrame, text="Operaciones")
varLabel.grid(row=0,column=3, padx=5, pady=5)

varLabel2=Label(varFrame, text="Valor 1")
varLabel2.grid(row=1,column=0,sticky=W)

varLabel3=Label(varFrame, text="Valor 2")
varLabel3.grid(row=2,column=0,sticky=W)

varLabel4=Label(varFrame, text="Resultado")
varLabel4.grid(row=3,column=0)

varEntry=Entry(varFrame,textvariable= numeroEntry)
varEntry.grid(row=1,column=1, padx=5, pady=5)

varEntry2=Entry(varFrame,textvariable= numeroEntry2)
varEntry2.grid(row=2,column=1, padx=5, pady=5)

varEntry3=Entry(varFrame,state="readonly", textvariable= numeroEntry3)
varEntry3.grid(row=3,column=1, padx=5, pady=5)

radButtonSum = Radiobutton(varFrame,text= "Sumar", variable=opRadioButton, value=1)
radButtonSum.grid(row=1, column=3, padx=5, pady=5,sticky=W)

radButtonRes = Radiobutton(varFrame,text= "Restar", variable=opRadioButton, value=2)
radButtonRes.grid(row=2, column=3, padx=5, pady=5,sticky=W)

radButtonMult = Radiobutton(varFrame,text= "Multiplicar", variable=opRadioButton, value=3)
radButtonMult.grid(row=3, column=3, padx=5, pady=5,sticky=W)

radButtonDiv = Radiobutton(varFrame,text= "Dividir", variable=opRadioButton, value=4)
radButtonDiv.grid(row=4, column=3,padx=5, pady=5,sticky=W)

varButton=Button(varFrame,text="Calcular", command=Calcular)
varButton.grid(row=5,column=1, padx=5, pady=5, sticky=EW)

main.mainloop()