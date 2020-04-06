from tkinter import *

#Crear raiz de la interfaz
root=Tk()

root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('favicon.ico')


frame=Frame(root,width=480,height=200)
frame.pack() #Alinea por defecto en el centro

label=Label(frame, text="¡Hola mundo!")
label.place(x=0,y=0)



# bucle de la aplicación
root.mainloop()