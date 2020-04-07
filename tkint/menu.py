from tkinter import *


#Crear raiz de la interfaz
root=Tk()

root.title("Radio buttons")
root.iconbitmap('favicon.ico')

menubar=Menu(root)
root.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

editmenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Cortar")
filemenu.add_command(label="Copiar")
filemenu.add_command(label="Pegar")


helpmenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Ayuda")
filemenu.add_separator()
filemenu.add_command(label="Acerca de ...", command=root.quit)


menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Edit",menu=editmenu)
menubar.add_cascade(label="Help",menu=helpmenu)

# bucle de la aplicación
root.mainloop()