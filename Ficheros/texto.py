from io import  open

texto="Linea de texto \n con texto\nOtra línea"

fichero=open("fichero.txt",'w')
fichero.write(texto)
fichero.close()

fichero2=open("fichero.txt",'r')
textoFic=fichero2.read()
fichero2.close()
#print(textoFic)
#print(texto)
fichero2=open("fichero.txt",'r')
lineas=fichero2.readlines()
fichero2.close()
print(lineas)

fichero3=open("append_new.txt","a")
fichero3.write("\nCuarta línea")
fichero3.write(open("append.txt","r").read())
fichero3.write(open("fichero.txt","r").read())
fichero3.close()

#Cambiar el valor de una línea
fichero4=open("append_new.txt","r+")
lineas4=fichero4.readlines()
lineas4[-1]="Update de línea"
fichero4.seek(0)
fichero4.writelines(lineas4)
fichero4.close()