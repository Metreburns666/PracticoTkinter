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
def Modulo():
    num1=int(numeroEntry.get())
    num2=int(numeroEntry2.get())
    numeroEntry3.set(num1%num2)
def Reset():
    numeroEntry.set(0)
    numeroEntry2.set(0)
    numeroEntry3.set(0)

numeroEntry=IntVar()
numeroEntry.set(0)
numeroEntry2=IntVar()
numeroEntry2.set(0)
numeroEntry3=IntVar()
numeroEntry3.set(0)

varFrame=Frame(main)
varFrame.pack()

varLabel=Label(varFrame,text="Primer Numero")
varLabel.grid(row=0,column=0, padx=5, pady=5)

varLabel2=Label(varFrame,text="Segundo Numero")
varLabel2.grid(row=1,column=0, padx=5, pady=5)

varLabel3=Label(varFrame,text="Resultado")
varLabel3.grid(row=2,column=0, padx=5, pady=5)

varEntry=Entry(varFrame,textvariable= numeroEntry)
varEntry.grid(row=0,column=1, padx=5, pady=5)

varEntry2=Entry(varFrame,textvariable= numeroEntry2)
varEntry2.grid(row=1,column=1, padx=5, pady=5)

varEntry3=Entry(varFrame,state="readonly", textvariable= numeroEntry3)
varEntry3.grid(row=2,column=1, padx=5, pady=5)

varButton=Button(varFrame,text="+", command=Suma)
varButton.grid(row=3,column=0, sticky=EW, padx=5, pady=5)

varButton2=Button(varFrame,text="-", command=Resta)
varButton2.grid(row=3,column=1, sticky=EW, padx=5, pady=5)

varButton3=Button(varFrame,text="*", command=Multiplicacion)
varButton3.grid(row=4,column=0, sticky=EW, padx=5, pady=5)

varButton4=Button(varFrame,text="/", command=Division)
varButton4.grid(row=4,column=1, sticky=EW, padx=5, pady=5)

varButton5=Button(varFrame,text="%", command=Modulo)
varButton5.grid(row=5,column=0, sticky=EW, padx=5, pady=5)

varButton6=Button(varFrame,text="CLEAR", command=Reset)
varButton6.grid(row=5,column=1, sticky=EW, padx=5, pady=5)

main.mainloop()