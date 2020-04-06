from tkinter import *


def hola():
    print("Hola mundo")

def crear_label():
    Label(root,text="label creada dinámicamente").pack()
def sumar():
    r.set(float(n1.get())+float(n2.get()))
    borrar()
def restar():
    r.set(float(n1.get())-float(n2.get()))
    borrar()
def producto():
    r.set(float(n1.get())*float(n2.get()))
    borrar()
def borrar():
    n1.set("")
    n2.set("")
#Crear raiz de la interfaz
root=Tk()
root.config(bd=15)
root.title("Buttons")
root.iconbitmap('favicon.ico')

n1=StringVar()
n2=StringVar()
r=StringVar()

Label(root,text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack()
Label(root,text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack()
Label(root,text="").pack()
Label(root,text="Resultado").pack()
Entry(root, justify="center", textvariable=r,state="disabled").pack()

Button(root, text="Suma",command=sumar).pack(side="left")
Button(root, text="Resta",command=restar).pack(side="left")
Button(root, text="Producto",command=producto).pack(side="left")

# bucle de la aplicación
root.mainloop()