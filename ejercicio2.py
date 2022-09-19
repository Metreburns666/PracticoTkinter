from tkinter import *

main=Tk()
main.title("Contador Decreciente")#nombre del titulo
main.geometry("300x300")#"primero lo ancho y dsp lo alto"
main.config(bg="magenta2")#color del fondo

def contadorDecre():
    con=int(varEntry.get())
    con-= 1
    numeroEntry.set(con)


numeroEntry=IntVar()
numeroEntry.set(88)

varFrame=Frame(main)
varFrame.pack()

varLabel=Label(varFrame,text="Contador")
varLabel.grid(row=0,column=0)

varEntry=Entry(varFrame,state="readonly", textvariable= numeroEntry)
varEntry.grid(row=0,column=1)

varButton=Button(varFrame,text="-", command=contadorDecre)
varButton.grid(row=0,column=2)




main.mainloop()