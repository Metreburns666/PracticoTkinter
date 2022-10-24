from tkinter import *



class Window:
    def __init__(self, master,foto,foto2):

        desc=StringVar()
        desc.set("Enmarcado dentro de un paisaje excepcional entre montañas\n y lago sobre el acceso y principal avenida de Villa Carlos Paz,\n se emplaza MÓNACO Hotel & Resort, en un predio de 8.000 mts2.\n Cuenta con 93 habitaciones, terraza panorámica, pileta de 1.000.000 lts, tropical bar,\n salón de convenciones, entre otros servicios que interactúan con un magnífico parque de 5.000 mts2,\n con diversidad en especies de árboles y plantas.")

        frameS=Frame(master,bg="#1b201e")
        frameS.pack(fill=Y ,side=LEFT)
        titulo1=Label(frameS,text="Perfil",bg="red",fg="#1b201e").pack(expand=TRUE,fill=X,side=TOP)

        frames2=Frame(master,bg="orange")
        frames2.pack(expand=True, fill=BOTH, side=BOTTOM)
        titulo2=Label(frames2,text="Alojamientos",bg="#1b201e",fg="red",height=2,width=1000).pack(side=TOP)

        #frames2a=Frame(frames2,bg="orange")
        #frames2a.pack(expand=True,fill=BOTH,side=BOTTOM)
        #titulo2a=Label(frames2a,text="Hotel Monaco",bg="grey",fg="yellow",height=2,width=1000).pack(side=TOP)

        #frames2a1=Frame(frames2a,bg="orange").pack(side=BOTTOM)
        #fotito3=Label(frames2a1,image=foto)
        #fotito3.place(relx=0.5,rely=1.0)

        frames3=Frame(master,bg="Violet")
        frames3.pack(expand=True, fill=BOTH, side=BOTTOM)
        titulo3=Label(frames3,text="Comercios",bg="#1b201e",fg="red",height=2,width=1000).pack(side=TOP)

        frame=Frame(frameS,bg="#1b201e")
        frame.pack(side=TOP)
        fotito=Label(frame, image=foto, bg="#1b201e").grid(row=0,column=0,columnspan=3,padx=5, pady=10)
        fotito2=Label(frame, image=foto2, bg="#1b201e").grid(row=7,column=0,columnspan=3,padx=5, pady=10,rowspan=3)
        Label1= Label(frame, text= "Nombre de Usuario",bg="Red").grid(row=1,column=0,sticky=EW, padx=5,pady=5, ipadx=1, ipady=1)
        Entry1= Entry(frame, textvariable= "Metrebat13",bg="Red", state="readonly").grid(row=1,column=1,sticky=EW, padx=5,pady=5, ipadx=1, ipady=1)
        Label2= Label(frame, text= "Correo Electronico",bg="Red").grid(row=2,column=0,sticky=EW, padx=5,pady=5, ipadx=1, ipady=1)
        Entry2= Entry(frame, textvariable= "lucas.metrebian@gmail.com",bg="Red", state="readonly").grid(row=2,column=1, sticky=EW, padx=5,pady=5, ipadx=1, ipady=1)
        label3= Label(frame, text= "Numero de telefono",bg="Red").grid(row=3,column=0, sticky=EW, padx=5,pady=5, ipadx=1, ipady=1)
        Entry3= Entry(frame, textvariable= "03541-15691567",bg="Red",state="readonly").grid(row=3,column=1, sticky=EW, padx=5,pady=5, ipadx=1, ipady=1)
        button1=Button(frame, text= "Editar",bg="grey",fg="Red",relief=RAISED, bd=5).grid(row=4,column=0,columnspan=2, sticky=EW, padx=5,pady=5, ipadx=4, ipady=4)

        
        frames4=Frame(frames2,bg="#CCFFCC")
        frames4.pack(expand=True, fill=BOTH, side=BOTTOM)
        titulo4=Label(frames4,text="Hotel Monaco",bg="grey",fg="black",height=2,width=750).pack(side=TOP)
    
        foto3=Label(frames4,image=foto2,bg="#CCFFCC").pack(side=LEFT,expand=TRUE,fill=Y)
        caja1=Label(frames4,textvariable=desc,fg="black",bg="#CCFFCC").pack(side=TOP)

        
        frames6=Frame(frames3,bg="#FFCC66")
        frames6.pack(expand=True, fill=BOTH, side=BOTTOM)
        titulo6=Label(frames6,text="Mc Donalds",bg="grey",fg="black",height=2,width=750).pack(side=TOP)

        labelBarrio=Label(frames6,text="Centro",bg="#FFCC66").pack(side=LEFT,expand=TRUE,fill=Y)
        foto5=Label(frames6,image=foto2,bg="#FFCC66").pack(side=LEFT,expand=TRUE,fill=Y)
        caja3=Label(frames6,textvariable=desc,fg="black",bg="#FFCC66").pack(side=TOP)



root = Tk()
root.geometry("1020x800")
fotito=PhotoImage(file="zero two.png")
fotito2=PhotoImage(file="carlosPaz2.png")
window = Window(root,fotito,fotito2)
root.mainloop()
