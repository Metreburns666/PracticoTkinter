from tkinter import *

main=Tk()
main.title("Contador Creciente")#nombre del titulo
main.geometry("300x300")#"primero lo ancho y dsp lo alto"
main.config(bg="dark orange")#color del fondo

def contadorCrecre():
    con=int(varEntry.get())
    con+= 1
    numeroEntry.set(con)


numeroEntry=IntVar()
numeroEntry.set(0)

varFrame=Frame(main)
varFrame.pack()

varLabel=Label(varFrame,text="Contador")
varLabel.grid(row=0,column=0)

varEntry=Entry(varFrame,state="readonly", textvariable= numeroEntry)
varEntry.grid(row=0,column=1)

varButton=Button(varFrame,text="+", command=contadorCrecre)
varButton.grid(row=0,column=2)


main.mainloop()