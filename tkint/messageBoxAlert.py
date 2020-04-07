from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog


#Crear raiz de la interfaz
root=Tk()

def test():
    #MessageBox.showinfo("Hola", "Hola mundo")
    #MessageBox.showwarning("Warn", "Warning")
    #MessageBox.showerror("Error", "Error")
    #res=MessageBox.askquestion("Vital question", "Yes or no?") #tsmbién con askyesno, pero este devuelve boolean
    #if res=="yes": #no
    #    root.destroy()
    #res=MessageBox.askokcancel("Vital question", "accept or cancel?")
    #if res:
    #    root.destroy()
    #res=MessageBox.askretrycancel("Vital question", "Continue could not be sure")
    #if res:
    #    root.destroy()
    #fileRoute=FileDialog.askopenfile(title="Select the fucking file")#Devuelve la ruta de un fichero
    ##Tiene initialdir, filetypes=(("Fichero de texto","*.txt"),("Todos los ficheros",".*"))
    #print(fileRoute)
    fileRoute = FileDialog.asksaveasfile(title="Save the fucking file")
    print(fileRoute)


Button(root, text="Click me",command=test).pack()
# bucle de la aplicación
root.mainloop()