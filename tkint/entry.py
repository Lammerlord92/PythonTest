from tkinter import *

#Crear raiz de la interfaz
root=Tk()

root.title("Entry")
root.resizable(1,1)
root.iconbitmap('favicon.ico')

label=Label(root, text="Nombre")
label.grid(row=0,column=0,sticky="w")


entry=Entry(root)
entry.grid(row=0,column=1)
entry.config(justify="right",state="disabled") #state="normal"

label2=Label(root, text="Nombre muy largo")
label2.grid(row=1,column=0,sticky="w")


entry2=Entry(root)
entry2.grid(row=1,column=1)
entry2.config(justify="center",show="*")

# bucle de la aplicación
root.mainloop()