from tkinter import *

#Crear raiz de la interfaz
root=Tk()

root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('favicon.ico')

# Variables dinámicas
texto=StringVar()
texto.set("Un nuevo texto")

frame=Frame(root,width=480,height=200)
frame.pack() #Alinea por defecto en el centro

label=Label(frame, text="¡Hola mundo!")
label.pack()
label.config(fg="blue",font={"Verdana",24})

label2=Label(frame, text="¡Hola mundo!")
label2.pack()
label2.config(fg="red",font={"Verdana",24})
label2.config(textvariable=texto)

image=PhotoImage(file="Different-phases-of-map-reduce-in-word-count-example.png")
Label(root,image=image).pack()
# bucle de la aplicación
root.mainloop()