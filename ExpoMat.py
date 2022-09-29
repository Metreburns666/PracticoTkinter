from tkinter import *
from tkinter import messagebox

def volver(var1, var2):
    var1.withdraw()
    var2.deiconify()

def validar(n):
        try:
            float(n)
            return True
        except:
            return False
            
def Calcular():
    parametro=int(valorResta.get())/9
    suma=int(valorSumaDig.get())
    Resultado = 0
    print(opMayMen.get())
    if opMayMen.get() == 1:
        Resultado=((suma - parametro)/2)*10 + ((suma + parametro)/2)
    if opMayMen.get() == 2:
        Resultado=((suma + parametro)/2)*10 + ((suma - parametro)/2)
    return int(Resultado)

def ventanaUno():
    global vent1, opRadioButton
    vent1=Tk()
    vent1.title("Adivina, Adivinador")
    vent1.geometry("1366x700")

    varFrame=Frame(vent1,padx=20, pady=20)
    varFrame.pack()

    opRadioButton= IntVar()

    varLabel=Label(varFrame, text="Choose your lenguanje // Elige un idioma")
    varLabel.config(font=("Verdana",20))
    varLabel.grid(row=0,column=0,columnspan=2, padx=3, pady=3)

    radButtonEng = Radiobutton(varFrame,text= "Ingles", variable=opRadioButton, value=1)
    radButtonEng.config(font=("Verdana",10))
    radButtonEng.grid(row=1, column=1, padx=3, pady=3, sticky=W)

    radButtonEsp = Radiobutton(varFrame,text= "Español", variable=opRadioButton, value=2)
    radButtonEsp.config(font=("Verdana",10))
    radButtonEsp.grid(row=2, column=1, padx=3, pady=3,sticky=W)

    varButton=Button(varFrame,text="Continuar",command=lambda:ventanaDos())
    varButton.grid(row=6,column=1, padx=5, pady=5, sticky=W)

    vent1.mainloop()

def ventanaDos():
    global vent2
    vent1.withdraw()
    vent2=Tk()
    vent2.title("Adivina, Adivinador")
    vent2.geometry("1366x700")

    varFrame=Frame(vent2,padx=20, pady=20)
    varFrame.pack()

    if opRadioButton.get() == 1:

        varLabel1=Label(varFrame, text="Welcome to ExpoCarreras 2023")
        varLabel1.config(font=("Verdana",20))
        varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

        varLabel2=Label(varFrame, text="Would you be interested in playing a guessing game? \n")
        varLabel2.config(font=("Verdana",10))

        varLabel2.grid(row=1,column=1, padx=3, pady=3, sticky=EW)

        varButton1=Button(varFrame,text="Choose language again", command=lambda:volver(vent2, vent1))
        varButton1.grid(row=2,column=0, padx=5, pady=5, sticky=EW)

        varButton2=Button(varFrame,text="Start playing", command=lambda:ventanaTres())
        varButton2.grid(row=2,column=4, padx=5, pady=5, sticky=EW)
    
    elif opRadioButton.get() == 2:
        varLabel1=Label(varFrame, text="Bienvenidos a la ExpoCarreras 2023")
        varLabel1.config(font=("Verdana",20))
        varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

        varLabel2=Label(varFrame, text="¿Te interesaria jugar a una adivinanza? \n")
        varLabel2.config(font=("Verdana",10))
        varLabel2.grid(row=1,column=1, padx=3, pady=3, sticky=EW)

        varButton1=Button(varFrame,text="Volver	a elegir idioma", command=lambda:volver(vent2, vent1))
        varButton1.grid(row=2,column=0, padx=5, pady=5, sticky=EW)

        varButton2=Button(varFrame,text="Comenzar a Jugar", command=lambda:ventanaTres())
        varButton2.grid(row=2,column=4, padx=5, pady=5, sticky=EW)

    else:
        varLabel1=Label(varFrame, text="Por favor seleccione un idioma \n")
        varLabel1.config(font=("Verdana",20))
        varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

        varButton1=Button(varFrame,text="Volver	a elegir idioma", command=lambda:volver(vent2, vent1))
        varButton1.grid(row=4,column=1, padx=5, pady=5, sticky=EW)

    vent2.mainloop()

def ventanaTres():
    global vent3,nombreJugador
    vent2.withdraw()
    vent3=Tk()
    vent3.title("Adivina, Adivinador")
    vent3.geometry("1366x700")
    nombreJugador=StringVar(vent3,"")

    varFrame=Frame(vent3,padx=20, pady=20)
    varFrame.pack()

    if opRadioButton.get() == 1:

        varLabel1=Label(varFrame, text="Before I start playing I would like to know your name.")
        varLabel1.config(font=("Verdana",15))
        varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

        varLabel2=Label(varFrame, text="Please enter your name here.")
        
        varLabel2.config(font=("Verdana",10))
        varLabel2.grid(row=1,column=1, padx=3, pady=3, sticky=EW)

        varEntry=Entry(varFrame,textvariable= nombreJugador)
        varEntry.grid(row=2,column=1, padx=5, pady=5)

        varLabel3=Label(varFrame, text=" ")
        varLabel3.grid(row=2,column=0, padx=3, pady=3)

        varLabel4=Label(varFrame, text=" ")
        varLabel4.grid(row=3,column=0, padx=3, pady=3)

        varButton1=Button(varFrame,text="Return", command=lambda:volver(vent3, vent2))
        varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=EW)

        varButton2=Button(varFrame,text="Continue", command=lambda:ventanaCuatro())
        varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=EW)

    elif opRadioButton.get() == 2:

        varLabel1=Label(varFrame, text="Antes de empezar a jugar me gustaria saber tu nombre.")
        varLabel1.config(font=("Verdana",15))
        varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

        varLabel2=Label(varFrame, text="Ingresa aqui tu nombre por favor")
        varLabel2.config(font=("Verdana",10))
        varLabel2.grid(row=1,column=1, padx=3, pady=3, sticky=EW)

        varEntry=Entry(varFrame,textvariable= nombreJugador)
        varEntry.grid(row=2,column=1, padx=5, pady=5)

        varLabel3=Label(varFrame, text=" ")
        varLabel3.grid(row=2,column=0, padx=3, pady=3)

        varLabel4=Label(varFrame, text=" ")
        varLabel4.grid(row=3,column=0, padx=3, pady=3)

        varButton1=Button(varFrame,text="Volver", command=lambda:volver(vent3, vent2))
        varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=EW)

        varButton2=Button(varFrame,text="Continuar", command=lambda:ventanaCuatro())
        varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=EW)


    vent3.mainloop()

def ventanaCuatro():
    global vent4
    vent3.withdraw()
    vent4=Tk()
    vent4.title("Adivina, Adivinador")
    vent4.geometry("1366x700")

    varFrame=Frame(vent4,padx=20, pady=20)
    varFrame.pack()
    if nombreJugador.get() != "":
        if opRadioButton.get() == 1:
            textoNomJug=StringVar(vent4,"")
            textoNomJug.set("Very well "+ nombreJugador.get() + " I would like you to think of a 2-digit number (that are not the same).")
            varLabel1=Label(varFrame, textvariable=textoNomJug)
            varLabel1.config(font=("Verdana",15))
            varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

            varLabel2=Label(varFrame, text=" MMMM... You already did? ... If so, click the Continue button.")
            varLabel2.config(font=("Verdana",15))
            varLabel2.grid(row=1,column=1, padx=3, pady=3, sticky=EW)

            varButton1=Button(varFrame,text="Return", command=lambda:volver(vent4, vent3))
            varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=EW)

            varButton2=Button(varFrame,text="Continue", command=lambda:ventanaCinco())
            varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=EW)

        else:
            textoNomJug=StringVar(vent4,"")
            textoNomJug.set("Muy bien "+ nombreJugador.get() + " me gustaria que pienses en un numero de 2 cifras ( que no sean iguales).")
            varLabel1=Label(varFrame, textvariable=textoNomJug)
            varLabel1.config(font=("Verdana",15))
            varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

            varLabel2=Label(varFrame, text=" MMMM...Ya lo hiciste?...Si es asi Presiona en el boton Continuar.")
            varLabel2.config(font=("Verdana",15))
            varLabel2.grid(row=1,column=1, padx=3, pady=3, sticky=EW)

            varButton1=Button(varFrame,text="Volver", command=lambda:volver(vent4, vent3))
            varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=EW)

            varButton2=Button(varFrame,text="Continuar", command=lambda:ventanaCinco())
            varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=EW)

    else:
        if opRadioButton.get() == 1:
            varLabel1=Label(varFrame, text="Please enter a Name. \n")
            varLabel1.config(font=("Verdana",20))
            varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

            varButton1=Button(varFrame,text="Return", command=lambda:volver(vent4, vent3))
            varButton1.grid(row=4,column=1, padx=5, pady=5, sticky=EW)
        
        else:
            varLabel1=Label(varFrame, text="Por favor ingrese el nombre \n")
            varLabel1.config(font=("Verdana",20))
            varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

            varButton1=Button(varFrame,text="Volver", command=lambda:volver(vent4, vent3))
            varButton1.grid(row=4,column=1, padx=5, pady=5, sticky=EW)


    vent4.mainloop()

def ventanaCinco():
    global vent5
    vent4.withdraw()
    vent5=Tk()
    vent5.title("Adivina, Adivinador")
    vent5.geometry("1366x700")
    varFrame=Frame(vent5,padx=20, pady=20)
    varFrame.pack()
    if opRadioButton.get() == 1:
        textoNomJug=StringVar(vent5,"")
        textoNomJug.set("Perfect "+ nombreJugador.get() + ", now reverse the order of the digits\n of the number you chose.")

        varLabel1=Label(varFrame, textvariable=textoNomJug)
        varLabel1.config(font=("Verdana",15))
        varLabel1.grid(row=1, column=1,padx=3,pady=3,sticky=EW)

        varButton1=Button(varFrame,text="Return", command=lambda:volver(vent5, vent4))
        varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=EW)

        varButton2=Button(varFrame,text="Continue", command=lambda:ventanaSeis())
        varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=EW)
    
    if opRadioButton.get() == 2:
        
        textoNomJug=StringVar(vent5,"")
        textoNomJug.set("Perfecto "+ nombreJugador.get() + ", ahora inverti el orden de las cifras\n del numero que elegiste")
        

        varLabel1=Label(varFrame, textvariable=textoNomJug)
        varLabel1.config(font=("Verdana",15))
        varLabel1.grid(row=1, column=1,padx=3,pady=3,sticky=EW)

        varButton1=Button(varFrame,text="Volver", command=lambda:volver(vent5, vent4))
        varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=EW)

        varButton2=Button(varFrame,text="Continuar", command=lambda:ventanaSeis())
        varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=EW)


    vent5.mainloop()

def ventanaSeis():
    global vent6,opMayMen
    vent5.withdraw()
    vent6=Tk()
    vent6.title("Adivina, Adivinador")
    vent6.geometry("1366x700")
    opMayMen=IntVar(vent6, "")

    if opRadioButton.get() == 1:
        textoNomJug=StringVar(vent6,"")
        textoNomJug.set(nombreJugador.get() + ":The new number is higher or lower than the first?")
        
        
        varFrame=Frame(vent6,padx=20, pady=20)
        varFrame.pack()

        varLabel1=Label(varFrame, textvariable=textoNomJug)
        varLabel1.config(font=("Verdana",15))
        varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

        radButtonMay = Radiobutton(varFrame,width=5, text= " Higher ", variable=opMayMen, value=1)
        radButtonMay.grid(row=1, column=1, padx=3, pady=3, sticky=EW)

        radButtonMen = Radiobutton(varFrame,width=5,text= " Lower ", variable=opMayMen, value=2)
        radButtonMen.grid(row=2, column=1, padx=3, pady=3, sticky=EW)

        varButton1=Button(varFrame,text="Return", command=lambda:volver(vent6, vent5))
        varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=EW)

        varButton2=Button(varFrame,text="Continue", command=lambda:ventanaSiete())
        varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=EW)

    if opRadioButton.get() == 2:

        textoNomJug=StringVar(vent6,"")
        textoNomJug.set(nombreJugador.get() + ":¿ El nuevo numero es mayor o menor que el primero?")
        
        varFrame=Frame(vent6,padx=20, pady=20)
        varFrame.pack()

        varLabel1=Label(varFrame, textvariable=textoNomJug)
        varLabel1.config(font=("Verdana",15))
        varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

        radButtonMay = Radiobutton(varFrame,width=5, text= " Mayor ", variable=opMayMen, value=1)
        radButtonMay.grid(row=1, column=1, padx=3, pady=3, sticky=EW)

        radButtonMen = Radiobutton(varFrame,width=5,text= " Menor ", variable=opMayMen, value=2)
        radButtonMen.grid(row=2, column=1, padx=3, pady=3, sticky=EW)

        varButton1=Button(varFrame,text="Volver", command=lambda:volver(vent6, vent5))
        varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=EW)

        varButton2=Button(varFrame,text="Continuar", command=lambda:ventanaSiete())
        varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=EW)

def ventanaSiete():
    global vent7,valorResta
    vent6.withdraw()
    vent7=Tk()
    vent7.title("Adivina, Adivinador")
    vent7.geometry("1366x700")

    if opRadioButton.get() == 1:
        textoNomJug=StringVar(vent7,"")
        textoNomJug.set("So far a bit boring right? But well the end will surprise you MUAHAHA\n " + nombreJugador.get() + ", now between the numbers you thought of, the original and the inverted one,\n subtract the one with the highest value from the one with the lowest value." )
        varFrame=Frame(vent7,padx=20, pady=20)
        varFrame.pack()
        valorResta=StringVar(vent7,"")

        varLabel1=Label(varFrame, textvariable=textoNomJug)
        varLabel1.config(font=("Verdana",15))
        varLabel1.grid(row=0,column=0,columnspan=2, padx=3, pady=3, sticky=EW)

        varLabel2=Label(varFrame, text="Ingrese el resultado Aqui --->")
        varLabel2.config(font=("Verdana",15))
        varLabel2.grid(row=1,column=0, padx=3, pady=3, sticky=E)

        varEntry=Entry(varFrame,textvariable= valorResta)
        varEntry.grid(row=1,column=1, padx=5, pady=5, sticky=W)

        varButton1=Button(varFrame,text="Return", command=lambda:volver(vent7, vent6))
        varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=W)

        varButton2=Button(varFrame,text="Continue", command=lambda:ventanaOcho())
        varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=E)

    if opRadioButton.get() == 2:
        textoNomJug=StringVar(vent7,"")
        textoNomJug.set("Hasta ahora un poco aburrido verdad? pero bueno el final te sorprendera MUAHAHA\n " + nombreJugador.get() + ", ahora entre los numeros que pensaste, el original y el invertido,\nal de mayor valor restale el de menor valor." )
        varFrame=Frame(vent7,padx=20, pady=20)
        varFrame.pack()
        valorResta=StringVar(vent7,"")

        varLabel1=Label(varFrame, textvariable=textoNomJug)
        varLabel1.config(font=("Verdana",15))
        varLabel1.grid(row=0,column=0,columnspan=2, padx=3, pady=3, sticky=EW)

        varLabel2=Label(varFrame, text="Ingrese el resultado Aqui --->")
        varLabel2.config(font=("Verdana",15))
        varLabel2.grid(row=1,column=0, padx=3, pady=3, sticky=E)

        varEntry=Entry(varFrame,textvariable= valorResta)
        varEntry.grid(row=1,column=1, padx=5, pady=5, sticky=W)

        varButton1=Button(varFrame,text="Volver", command=lambda:volver(vent7, vent6))
        varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=W)

        varButton2=Button(varFrame,text="Continuar", command=lambda:ventanaOcho())
        varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=E)

def ventanaOcho():
    global vent8,valorSumaDig
    vent7.withdraw()
    vent8=Tk()
    vent8.title("Adivina, Adivinador")
    vent8.geometry("1366x700")
    varFrame=Frame(vent8,padx=20, pady=20)
    varFrame.pack()
    valorSumaDig=StringVar(vent8,"")

    if validar(valorResta.get()):
        if opRadioButton.get() == 1:
            varLabel1=Label(varFrame, text="We are almost there, you could say that the number you thought we are already seeing it JAJA!!!\n Now add the digits of the number you thought of at the beginning")
            varLabel1.config(font=("Verdana",15))
            varLabel1.grid(row=0,column=0,columnspan=2, padx=3, pady=3, sticky=W)

            varLabel2=Label(varFrame, text="Enter the result here --->")
            varLabel2.config(font=("Verdana",15))
            varLabel2.grid(row=2,column=0, padx=3, pady=3, sticky=E)

            varEntry=Entry(varFrame,textvariable= valorSumaDig)
            varEntry.grid(row=2,column=1, padx=5, pady=5, sticky=W)

            varButton1=Button(varFrame,text="Return", command=lambda:volver(vent8, vent7))
            varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=W)

            varButton2=Button(varFrame,text="Continue", command=lambda:ventanaNueve())
            varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=E)

        else:

            varLabel1=Label(varFrame, text="Ya casi estamos, se podria decir que el numero que pensaste ya lo estamos viendo JAJA!!! \n Ahora suma las cifras del numero que pensaste al principio")
            varLabel1.config(font=("Verdana",15))
            varLabel1.grid(row=0,column=0,columnspan=2, padx=3, pady=3, sticky=W)

            varLabel2=Label(varFrame, text="Ingrese el resultado Aqui --->")
            varLabel2.config(font=("Verdana",15))
            varLabel2.grid(row=2,column=0, padx=3, pady=3, sticky=E)

            varEntry=Entry(varFrame,textvariable= valorSumaDig)
            varEntry.grid(row=2,column=1, padx=5, pady=5, sticky=W)

            varButton1=Button(varFrame,text="Volver", command=lambda:volver(vent8, vent7))
            varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=W)

            varButton2=Button(varFrame,text="Continuar", command=lambda:ventanaNueve())
            varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=E)
    else:
        if opRadioButton.get() == 1:
            varLabel1=Label(varFrame, text="Please enter a number. \n")
            varLabel1.config(font=("Verdana",20))
            varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

            varButton1=Button(varFrame,text="Return", command=lambda:volver(vent8, vent7))
            varButton1.grid(row=4,column=1, padx=5, pady=5, sticky=EW)
        
        else:
            varLabel1=Label(varFrame, text="Por favor ingrese un numero.\n")
            varLabel1.config(font=("Verdana",20))
            varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

            varButton1=Button(varFrame,text="Volver	a ingresar numero", command=lambda:volver(vent8, vent7))
            varButton1.grid(row=4,column=1, padx=5, pady=5, sticky=EW)

def ventanaNueve():
    global vent9
    vent8.withdraw()
    vent9=Tk()
    vent9.title("Adivina, Adivinador")
    vent9.geometry("1366x700")
    textoNomJug=StringVar(vent9,"")

    if validar(valorSumaDig.get()):
        if opRadioButton.get() == 1:
            textoNomJug.set("VERY GOOD "+ nombreJugador.get().upper()  +" THE NUMBER YOU THOUGHT IS....\n " + str(Calcular()) )
            varFrame=Frame(vent9,padx=20, pady=20)
            varFrame.pack()

            varLabel1=Label(varFrame, textvariable=textoNomJug)
            varLabel1.config(font=("Verdana",20))
            varLabel1.grid(row=0,column=0,columnspan=2, padx=3, pady=3, sticky=EW)

            varButton1=Button(varFrame,text="Return", command=lambda:volver(vent9, vent8))
            varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=W)

            varButton2=Button(varFrame,text="Play Again", command=lambda:volver(vent9, vent1) )
            varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=E)
        else:
            textoNomJug.set("MUY BIEN "+ nombreJugador.get().upper() +" EL NUMERO QUE PENSASTE ES....TA TAN TA TAN\n " + str(Calcular())  )
            varFrame=Frame(vent9,padx=20, pady=20)
            varFrame.pack()

            varLabel1=Label(varFrame, textvariable=textoNomJug)
            varLabel1.config(font=("Verdana",20))
            varLabel1.grid(row=0,column=0,columnspan=2, padx=3, pady=3, sticky=EW)

            varButton1=Button(varFrame,text="Volver", command=lambda:volver(vent9, vent1))
            varButton1.grid(row=4,column=0, padx=5, pady=5, sticky=W)

            varButton2=Button(varFrame,text="Jugar de Nuevo", command=lambda:volver(vent9, vent1) )
            varButton2.grid(row=4,column=4, padx=5, pady=5, sticky=E)
    
    else:
        if opRadioButton.get() == 1:
            varLabel1=Label(varFrame, text="Please enter a number. \n")
            varLabel1.config(font=("Verdana",20))
            varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

            varButton1=Button(varFrame,text="Return", command=lambda:volver(vent9, vent8))
            varButton1.grid(row=4,column=1, padx=5, pady=5, sticky=EW)
        
        else:
            varLabel1=Label(varFrame, text="Por favor ingrese un numero.\n")
            varLabel1.config(font=("Verdana",20))
            varLabel1.grid(row=0,column=1, padx=3, pady=3, sticky=EW)

            varButton1=Button(varFrame,text="Volver	a ingresar numero", command=lambda:volver(vent9, vent8))
            varButton1.grid(row=4,column=1, padx=5, pady=5, sticky=EW)
ventanaUno()