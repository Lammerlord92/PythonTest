from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text="")

#Crear raiz de la interfaz
root=Tk()

root.title("Radio buttons")
root.iconbitmap('favicon.ico')

opcion=IntVar()

Radiobutton(root,text="Option 1", variable=opcion, value=1,command=seleccionar).pack()
Radiobutton(root,text="Option 2", variable=opcion, value=2,command=seleccionar).pack()
Radiobutton(root,text="Option 3", variable=opcion, value=3,command=seleccionar).pack()
Label(root,text="").pack()
monitor=Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()
# bucle de la aplicación
root.mainloop()