from tkinter import *

class Ventana:
    def __init__(self,master,foto):
        

        titulo=Label(master,fg="Black",bg="Orange",font=("Helvetica, 16"), text="Perfil")
        titulo.pack(side=TOP,fill=X)
        frame1=Frame(master,bg="#1b201e")
        frame1.pack(fill=Y,side=LEFT)
        frame2=Frame(master,bg="#1b201e")
        frame2.pack(expand=TRUE,fill=BOTH,side=BOTTOM)

        fotoPerfil=Label(frame1,bg="#1b201e",image=foto).grid(row=0,column=0,columnspan=3,sticky=EW,padx=15,pady=15)
        labelFotoPerfil=Label(frame1,bg="#1b201e",fg="white",text="Foto de perfil").grid(row=1,column=1, padx=15,pady=15,)
        ButtonCambiarFoto=Button(frame1,bg="red",fg="white",text="Modificar Foto de Perfil",relief=RAISED)
        ButtonCambiarFoto.grid(row=2,column=1,sticky=EW, padx=15,pady=15, ipadx=10, ipady=10)

        ButtonCambiarPw=Button(frame1,bg="red",fg="white",text="Modificar Contraseña",relief=RAISED)
        ButtonCambiarPw.grid(row=3,column=1,sticky=EW, padx=15,pady=15, ipadx=10, ipady=10)

        nameUser=Label(frame2,fg="white",bg="#1b201e",font=("Helvetica, 16"), text="Nombre de Usuario")
        nameUser.grid(row=0,column=0,columnspan=2,sticky=W,padx=50,pady=10)

        entryUser=Entry(frame2,bg="grey",fg="white",font=("Helvetica, 16"))
        entryUser.grid(row=1,column=0,columnspan=3,sticky=EW,padx=50,pady=10)

        Email=Label(frame2,fg="white",bg="#1b201e",font=("Helvetica, 16"), text="Email")
        Email.grid(row=2,column=0,columnspan=2,sticky=W,padx=50,pady=10)

        entryEmail=Entry(frame2,bg="grey",fg="white",font=("Helvetica, 16"))
        entryEmail.grid(row=3,column=0,columnspan=3,sticky=EW,padx=50,pady=10)

        telUser=Label(frame2,fg="white",bg="#1b201e",font=("Helvetica, 16"), text="Telefono #1")
        telUser.grid(row=4,column=0,columnspan=2,sticky=W,padx=50,pady=10)

        entrytelUser=Entry(frame2,bg="grey",fg="white",font=("Helvetica, 16"))
        entrytelUser.grid(row=5,column=0,columnspan=3,sticky=EW,padx=50,pady=10)

        botonDescartar=Button(frame2,bg="orange",fg="black",text="Descartar Cambios",relief=RAISED)
        botonDescartar.grid(row=6,column=0,padx=50,pady=45,ipadx=10, ipady=10)

        botonGuardar=Button(frame2,bg="red",fg="white",text="Guardar Cambios",relief=RAISED)
        botonGuardar.grid(row=6,column=2,padx=50,pady=45,ipadx=10, ipady=10)

root = Tk()
root.geometry("1020x800")
fotito=PhotoImage(file="zero two.png")
fotito2=PhotoImage(file="carlosPaz2.png")
Ventanita =Ventana(root,fotito)
root.mainloop()
