from tkinter import *

main=Tk()
main.title("Calculadora")#nombre del titulo
main.geometry("300x200")#"primero lo ancho y dsp lo alto"
main.config(bg="dark orange")#color del fondo

def contadorCrecre():
    con=int(varEntry.get())
    con+= 1
    numeroEntry.set(con)


numeroEntry=IntVar()
numeroEntry.set(0)

varFrame=Frame(main)
varFrame.pack()

varLabel=Label(varFrame,text="Primer Numero")
varLabel.grid(row=0,column=0)

varLabel2=Label(varFrame,text="Segundo Numero")
varLabel2.grid(row=1,column=0)

varLabel3=Label(varFrame,text="Resultado")
varLabel3.grid(row=2,column=0)

varEntry=Entry(varFrame,state="readonly", textvariable= numeroEntry)
varEntry.grid(row=0,column=1)

varEntry2=Entry(varFrame,state="readonly", textvariable= numeroEntry)
varEntry2.grid(row=1,column=1)

varEntry3=Entry(varFrame,state="readonly", textvariable= numeroEntry)
varEntry3.grid(row=2,column=1)

varButton=Button(varFrame,text="+", command=contadorCrecre)
varButton.grid(row=3,column=0)

varButton2=Button(varFrame,text="-", command=contadorCrecre)
varButton2.grid(row=3,column=1)

varButton3=Button(varFrame,text="*", command=contadorCrecre)
varButton3.grid(row=4,column=0)

varButton4=Button(varFrame,text="/", command=contadorCrecre)
varButton4.grid(row=4,column=1)

varButton5=Button(varFrame,text="%", command=contadorCrecre)
varButton5.grid(row=5,column=0)

varButton6=Button(varFrame,text="CLEAR", command=contadorCrecre)
varButton6.grid(row=5,column=1)

main.mainloop()