import pickle


l=[1,2,3,4,5]

#Fichero escrito con estructura bin
fichero=open("lista.pckl",'wb')
pickle.dump(l,fichero)
fichero.close()

fichero=open("lista.pckl",'rb')
lista=pickle.load(fichero)
print (lista)
del (fichero)

class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
    def __str__(self):
        return self.nombre

nombres=["Hector","Mario","Marta"]
personas=[]
for n in nombres:
    p=Persona(n)
    personas.append(p)

fichero=open("personas.pckl","wb")
pickle.dump(personas,fichero)
fichero.close()
fichero=open("personas.pckl","rb")
personasL=pickle.load(fichero)
fichero.close()
for p in personas:
    print(p)