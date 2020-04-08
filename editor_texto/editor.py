from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from io import open as Open

file_route=""

def new():
    global file_route
    monitor_text.set("New File")
    file_route=""
    texto.delete(1.0,"end")
def open():
    global file_route
    file_route=FileDialog.askopenfilename(title="Select text file",
                                          initialdir='.',
                                          filetype=(("Fichero de texto",".txt"),))
    if file_route!="":
        selected_file=Open(file_route,'r')
        file_contend=selected_file.read()
        texto.delete(1.0,"end")
        texto.insert('insert',file_contend)
        selected_file.close()
        monitor_text.set("Working with file "+file_route)

def save_file_to_route():
    file_contend = texto.get(1.0, "end-1c")
    save_file = Open(file_route, 'w+')
    save_file.write(file_contend)
    save_file.close()
    monitor_text.set(file_route + " has been saved")
def save_as():
    global file_route
    file_route=FileDialog.asksaveasfile(title="Save as",mode="w",defaultextension=".txt").name
    print(file_route)
    if file_route is not None:
        save_file_to_route()
    else:
        monitor_text.set(file_route + " cannot be saved")
        file_route=""
def save():
    global file_route
    if file_route!="":
        save_file_to_route()
    else:
        save_as()

#Crear raiz de la interfaz
root=Tk()

root.title("Mi editor")
root.iconbitmap('favicon.ico')

menubar=Menu(root)
root.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=new)
filemenu.add_command(label="Open",command=open)
filemenu.add_command(label="Save",command=save)
filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")
menubar.add_cascade(label="Edit",menu=editmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de ...", command=root.quit)
menubar.add_cascade(label="Help",menu=helpmenu)

#Caja de texto central
texto= Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0,padx=6,pady=4,font=("Consolas",12))

#MONITOR INFERIOR
monitor_text=StringVar()
monitor_text.set("Welcome to hell")
monitor=Label(root,textvar=monitor_text,justify='left')
monitor.pack(side="left")
# bucle de la aplicación
root.mainloop()