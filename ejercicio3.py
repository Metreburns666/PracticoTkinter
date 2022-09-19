from tkinter import *
import math

main=Tk()
main.title("Factorial")#nombre del titulo
main.geometry("500x100")#"primero lo ancho y dsp lo alto"
#main.config(bg="DarkGray")#color del fondo

def Factorial():
    con=int(numeroEntry.get())
    con+=1
    con2=math.factorial(con)
    numeroEntry.set(con)
    numeroEntry2.set(con2)

numeroEntry=IntVar()
numeroEntry.set(1)
numeroEntry2=IntVar()
numeroEntry2.set(1)


varFrame=Frame(main,padx=20, pady=20)
varFrame.pack()

varLabel=Label(varFrame,text="n")
varLabel.grid(row=0,column=0,padx=5, pady=5)

varEntry=Entry(varFrame,state="readonly", textvariable= numeroEntry)
varEntry.grid(row=0,column=1,padx=5, pady=5)

varLabel2=Label(varFrame,text="Factorial (n)")
varLabel2.grid(row=0,column=2,padx=5, pady=5)

varEntry2=Entry(varFrame,state="readonly", textvariable= numeroEntry2)
varEntry2.grid(row=0,column=3,padx=5, pady=5)

varButton=Button(varFrame,text="Siguiente", command=lambda:Factorial())
varButton.grid(row=0,column=4,padx=5, pady=5)


main.mainloop()