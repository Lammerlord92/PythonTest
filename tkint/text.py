from tkinter import *

#Crear raiz de la interfaz
root=Tk()

root.title("Text")
root.iconbitmap('favicon.ico')


text=Text(root)
text.pack()
text.config(width=30,height=10, font=("Consolas",12),padx=15,pady=15) #indica los caracteres máximos por línea y líneas que se pueden ver

# bucle de la aplicación
root.mainloop()