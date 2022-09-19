from tkinter import *
from tkinter import messagebox
from unittest.mock import seal

main=Tk()
main.title("Peliculas")#nombre del titulo
main.geometry("400x300")#"primero lo ancho y dsp lo alto"
main.config(bg="dark orange")#color del fondo

def ListaPeliculas():
    if PeliculaEntry.get().strip()== "":
        messagebox.showinfo(message="Error - Ingrese una Pelicula por favor") 
    else:
        varListBox.insert(END,PeliculaEntry.get())
        PeliculaEntry.set("")

PeliculaEntry=StringVar()
PeliculaEntry.set("")

varFrame=Frame(main)
varFrame.pack()

varZero=Label(varFrame,text="")
varZero.grid(row=0,column=0,padx=5, pady=5)

varLabel=Label(varFrame,text="Escribe el titulo de una pelicula")
varLabel.grid(row=1,column=0,padx=5, pady=5)

varLabel2=Label(varFrame,text="Peliculas")
varLabel2.grid(row=1,column=1,padx=5, pady=5)

varEntry=Entry(varFrame,textvariable=PeliculaEntry)
varEntry.grid(row=2,column=0,padx=5, pady=5)

varListBox=Listbox(varFrame)
varListBox.grid(row=2,column=1,padx=5, pady=5)

varButton=Button(varFrame,text="Añadir", command=ListaPeliculas)
varButton.grid(row=3,column=0,padx=5, pady=5, sticky=EW)


main.mainloop()