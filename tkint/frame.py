from tkinter import *

#Crear raiz de la interfaz
root=Tk()

root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('favicon.ico')

frame=Frame(root)
frame.pack() #Alinea por defecto en el centro
frame.config(width=480,height=200) #Se puede añadir al crear el frame
frame.config(cursor="pirate") #cambia el curson dentro del frame
frame.config(bg="lightblue")
frame.config(relief="sunken",bd="25")

frame2=Frame(root)
frame2.pack(side="bottom",anchor="e") #Alinea abajo al este
frame2.config(width=480,height=200) #Se puede añadir al crear el frame
frame2.config(cursor="pirate") #cambia el curson dentro del frame
frame2.config(bg="red")
frame2.config(relief="sunken",bd="25")

frame3=Frame(root)
frame3.pack(fill='x',expand=1) #rellena en x
frame3.config(width=480,height=200) #Se puede añadir al crear el frame
frame3.config(cursor="pirate") #cambia el curson dentro del frame
frame3.config(bg="green")
frame3.config(relief="sunken",bd="25")

frame4=Frame(root)
frame4.pack(fill='both',expand=1) #rellena en ambos todo lo que pueda
frame4.config(width=480,height=200) #Se puede añadir al crear el frame
frame4.config(cursor="pirate") #cambia el curson dentro del frame
frame4.config(bg="yellow")
frame4.config(relief="sunken",bd="25")


root.config(cursor="arrow") #cambia el curson dentro del frame
root.config(bg="blue")
root.config(relief="ridge",bd="25")

# bucle de la aplicación
root.mainloop()