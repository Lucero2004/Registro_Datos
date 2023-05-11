
from tkinter import * 
from tkinter import messagebox


def Abrir_Ventana():
    global toplevel_Ventana
    toplevel_Ventana=Toplevel()
    toplevel_Ventana.title("Ingresa los datos")
    toplevel_Ventana.resizable(0,0)
    toplevel_Ventana.geometry("500x300")
    toplevel_Ventana.config(bg="pink")

    lb_titulo1=Label(toplevel_Ventana, text="Datos Médicos")
    lb_titulo1.config( bg="light blue" , fg="black", bd=5,relief="raised",  font=("new time roma",12))
    lb_titulo1.place(x=10,y=5)
    lb_titulo2=Label(toplevel_Ventana, text="Datos Académico")
    lb_titulo2.config( bg="light blue" , fg="black", bd=5,relief="raised",  font=("new time roma",12))
    lb_titulo2.place(x=280,y=5)
    lb_nombre = Label(toplevel_Ventana, text = "Nombre: ")
    lb_nombre.config(bg="pink", fg="black", font=("Helvetica", 12))
    lb_nombre.place(x=10, y=36)

    lb_Edad= Label(toplevel_Ventana, text = "Edad: ")
    lb_Edad.config(bg="pink", fg="black", font=("Helvetica", 12))
    lb_Edad.place(x=10, y=76)

    lb_Estatura= Label(toplevel_Ventana, text = "Estatura: ")
    lb_Estatura.config(bg="pink", fg="black", font=("Helvetica", 12))
    lb_Estatura.place(x=10, y=116)

    lb_Peso= Label(toplevel_Ventana, text = "Peso: ")
    lb_Peso.config(bg="pink", fg="black", font=("Helvetica", 12))
    lb_Peso.place(x=10, y=156)

    lb_discapacidad= Label(toplevel_Ventana, text = "Posee alguna discapacidad: ")
    lb_discapacidad.config(bg="pink", fg="black", font=("Helvetica", 12))
    lb_discapacidad.place(x=10, y=196)

    lb_seguro= Label(toplevel_Ventana, text = "EPS: ")
    lb_seguro.config(bg="pink", fg="black", font=("Helvetica", 12))
    lb_seguro.place(x=10, y=236)


    lb_Quimica= Label(toplevel_Ventana, text = "Quimica: ")
    lb_Quimica.config(bg="pink", fg="black", font=("Helvetica", 12))
    lb_Quimica.place(x=250, y=36)

    lb_lenguaje= Label(toplevel_Ventana, text = "Lenguaje: ")
    lb_lenguaje.config(bg="pink", fg="black", font=("Helvetica", 12))
    lb_lenguaje.place(x=250, y=76)

    lb_CalculoI= Label(toplevel_Ventana, text = "CalculoI: ")
    lb_CalculoI.config(bg="pink", fg="black", font=("Helvetica", 12))
    lb_CalculoI.place(x=250, y=116)

    lb_Algebra= Label(toplevel_Ventana, text = "Algebra: ")
    lb_Algebra.config(bg="pink", fg="black", font=("Helvetica", 12))
    lb_Algebra.place(x=250, y=156)
   
    lb_Deportes= Label(toplevel_Ventana, text = "Deportes: ")
    lb_Deportes.config(bg="pink", fg="black", font=("Helvetica", 12))
    lb_Deportes.place(x=250, y=196)

    
    Nombre_Entry=Entry(toplevel_Ventana,textvariable=Nombre)
    Nombre_Entry.config(bg="white", fg="black", font=("Times New Roman", 12), width=25)
    Nombre_Entry.focus_set()
    Nombre_Entry.place(x=10, y=56)

    Edad_Entry=Entry(toplevel_Ventana,textvariable=Edad)
    Edad_Entry.config(bg="white", fg="black", font=("Times New Roman", 12), width=25)
    Edad_Entry.focus_set()
    Edad_Entry.place(x=10,y=98)

    Estatura_Entry=Entry(toplevel_Ventana,textvariable=Estatura )
    Estatura_Entry.config(bg="white", fg="black", font=("Times New Roman", 12), width=25)
    Estatura_Entry.focus_set()
    Estatura_Entry.place(x=10,y=138)

    Peso_Entry=Entry(toplevel_Ventana,textvariable=Peso)
    Peso_Entry.config(bg="white", fg="black", font=("Times New Roman", 12), width=25)
    Peso_Entry.focus_set()
    Peso_Entry.place(x=10,y=178)

    discapacidad_Entry=Entry(toplevel_Ventana,textvariable=discapacidad )
    discapacidad_Entry.config(bg="white", fg="black", font=("Times New Roman", 12), width=25)
    discapacidad_Entry.focus_set()
    discapacidad_Entry.place(x=10,y=216)

    seguro_Entry=Entry(toplevel_Ventana,textvariable=seguro )
    seguro_Entry.config(bg="white", fg="black", font=("Times New Roman", 12), width=25)
    seguro_Entry.focus_set()
    seguro_Entry.place(x=10,y=260)


    Quimica_Entry=Entry(toplevel_Ventana,textvariable=Quimica)
    Quimica_Entry.config(bg="white", fg="black", font=("Times New Roman", 12), width=25)
    Quimica_Entry.focus_set()
    Quimica_Entry.place(x=250,y=56)

    lenguaje_Entry=Entry(toplevel_Ventana,textvariable=lenguaje)
    lenguaje_Entry.config(bg="white", fg="black", font=("Times New Roman", 12), width=25)
    lenguaje_Entry.focus_set()
    lenguaje_Entry.place(x=250,y=98)

    CalculoI_Entry=Entry(toplevel_Ventana,textvariable=CalculoI)
    CalculoI_Entry.config(bg="white", fg="black", font=("Times New Roman", 12), width=25)
    CalculoI_Entry.focus_set()
    CalculoI_Entry.place(x=250,y=138)

    Algebra_Entry=Entry(toplevel_Ventana,textvariable=Algebra)
    Algebra_Entry.config(bg="white", fg="black", font=("Times New Roman", 12), width=25)
    Algebra_Entry.focus_set()
    Algebra_Entry.place(x=250,y=178)

    Deportes_Entry=Entry(toplevel_Ventana,textvariable=Deportes)
    Deportes_Entry.config(bg="white", fg="black", font=("Times New Roman", 12), width=25)
    Deportes_Entry.focus_set()
    Deportes_Entry.place(x=250,y=222)

    bt_Ok = Button(toplevel_Ventana,text="Ok", command=Ok)
    bt_Ok.place(x=276, y=254, width=100, height=30)
def Ok():
   toplevel_Ventana.destroy()
    
def Aceptar():
    t_resultados.insert(INSERT,"ESTADO MEDICO\n")
    N=Nombre.get()
    A=Edad.get()
    D=discapacidad.get()
    S=seguro.get()
    t_resultados.insert(INSERT,"Nombre:" f"{N}\n")
    t_resultados.insert(INSERT,"Edad:" f"{A}años\n")
    t_resultados.insert(INSERT,"Discapacidad:"f"{D}\n")
    t_resultados.insert(INSERT, "Seguro:"f"{S}\n")
    P=float(Peso.get())
    E=float(Estatura.get())
    Imc=P/(E**2)
    if Imc<18.5:
        t_resultados.insert(INSERT,"IMC:Peso bajo:Puede presentar Desnutrición:"+str(Imc))
    elif 18.5<=Imc and Imc<25:
       t_resultados.insert(INSERT,"IMC:Usted tiene un peso normal:"+str(Imc)) 
    else:
        if Imc<=25 and Imc<30:
         t_resultados.insert(INSERT,"IMC:Usted presenta sobrepeso:"+str(Imc))
    t_resultados.insert(INSERT,"\nESTADO ACADEMICO")
    n1=float(Quimica.get())
    n2=float(lenguaje.get())
    n3=float(CalculoI.get())
    n4=float(Algebra.get())
    n5=float(Deportes.get())
    Prom= (n1+n2+n3+n4+n5)/5
    if Prom>=3.0:
      t_resultados.insert(INSERT,"\nPromedio:Aprobado="+str(Prom))
    else:
       t_resultados.insert(INSERT,"\nPromedio:Reprobado="+str(Prom))
    
    
    

def borrar():
    messagebox.showinfo("","Se cerrará la app")   
    
    t_resultados.delete("1.0","end")
  

def Salir():
    
    messagebox.showinfo("","Se cerrará la app")   

    ventana_principal.destroy()
# Ventana principal
ventana_principal=Tk()
ventana_principal.geometry("800x600")
ventana_principal.title("Maria Lucero Gomez Pico")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="cadet blue4",bd=6,relief= "ridge")

Nombre=StringVar()
Edad=StringVar()
Estatura=StringVar()
Peso= StringVar()
discapacidad= StringVar()
seguro=StringVar()
Quimica=StringVar()
lenguaje=StringVar()
CalculoI=StringVar()
Algebra=StringVar()
Deportes=StringVar()
Imc=StringVar()
Prom=StringVar()

frame_entrada1=Frame(ventana_principal)
frame_entrada1.config(bg="pink" ,bd=10,relief="ridge", width=780 , height=270)
frame_entrada1.place(x=5, y=10)

lb_titulo=Label(frame_entrada1, text="Calcule aquí su Estado Médico y Académico")
lb_titulo.config( bg="light blue" , fg="black", bd=5,relief="raised",  font=("new time roma",15))
lb_titulo.place(x=180,y=20)

logo1 = PhotoImage(file="medicos.png")
lb_logo1 = Label(frame_entrada1, image=logo1, bg="white",bd=5,relief="raised")
lb_logo1.place(x=100,y=90) 
logo2 = PhotoImage(file="academicos.png")
lb_logo2 = Label(frame_entrada1, image=logo2, bg="white",bd=5,relief="raised")
lb_logo2.place(x=500,y=90) 


bt_Ingresar_datos  =Button( frame_entrada1 ,bd=5,relief="raised", text= "Ingresar datos" , command = Abrir_Ventana)
bt_Ingresar_datos.place ( x =330, y =130 )

frame_entrada2=Frame(ventana_principal)
frame_entrada2.config(bg="pink",bd=10,relief= "ridge", width=778 , height=180)
frame_entrada2.place(x=5, y=290)

bt_Aceptar  =Button(ventana_principal ,bd=5,relief="raised", text= "Aceptar" , command =Aceptar)
bt_Aceptar.place ( x =250, y =500 ,width=80, height=50)


bt_salir = Button(ventana_principal,bd=5,relief="raised",text="Salir", command=Salir)
bt_salir.place(x=600, y=500,width=80, height=50)

bt_borrar = Button(ventana_principal,bd=5,relief="raised",text="Borrar", command= borrar)
bt_borrar.place(x=100, y=500,width=80, height=50)

t_resultados = Text(frame_entrada2)
t_resultados.config(bg="light blue", fg="black", font=("Courier", 12))
t_resultados.place(x=8,y=8,width=740,height=145)



ventana_principal.mainloop()