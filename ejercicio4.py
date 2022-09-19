from tkinter import *

main=Tk()
main.title("Contador")#nombre del titulo
main.geometry("500x100")#"primero lo ancho y dsp lo alto"
main.config(bg="magenta2")#color del fondo

def contadorCrecre():
    con=int(varEntry.get())
    con+= 1
    numeroEntry.set(con)

def contadorDecre():
    con=int(varEntry.get())
    con-= 1
    numeroEntry.set(con)

def reset():
    numeroEntry.set(0)

numeroEntry=IntVar()
numeroEntry.set(0)

varFrame=Frame(main)
varFrame.pack()

varLabel=Label(varFrame,text="Contador")
varLabel.grid(row=0,column=0)

varEntry=Entry(varFrame,state="readonly", textvariable= numeroEntry)
varEntry.grid(row=0,column=1)

varButton1=Button(varFrame,text="Count Up", command=contadorCrecre)
varButton1.grid(row=0,column=2)

varButton2=Button(varFrame,text="Count Down", command=contadorDecre)
varButton2.grid(row=0,column=3)

varButton3=Button(varFrame,text="Reset", command=reset)
varButton3.grid(row=0,column=4)


main.mainloop()