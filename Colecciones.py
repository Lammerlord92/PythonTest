from collections import deque

tupla=(8,2,4,"aaa",[1,2,3,4],-50)
print(tupla)

print(tupla.index("aaa"))
#print(tupla.index(100))
print(tupla.count(("algo")))
tupla=(2,2,2,"aaa",[1,2,3,4],-50)
print(tupla.count((2)))



#SET

print("SET")
conjunto=set()
print(conjunto)
conjunto={0,1,2,3,4}
print(conjunto)
conjunto.add(5)
print(conjunto)
conjunto.add(5)
print(conjunto)

print(5 in conjunto)


print("LIST")
l=[1,2,3,4,5]
print(l)
l2=list(conjunto)
print(l2)
l3=[1,2,3,3,3,4,5]
print(l3)
l4=list(set(l3))
print(l4)

print("DICCIONARIOS")
vacio={}
print(type(vacio))
colores={"amarillo":"yellow","rojo":"red"}
print(colores)
print(colores["amarillo"])
colores["amarillo"]="white"
print(colores["amarillo"])
edades={"Hector":1,"ana":2}
edades["Hector"]+=1
print(edades["Hector"])
for edad in edades:
    print(edad)

for clave in edades:
     print(edades[clave])

for clave in edades:
     print(clave,edades[clave])

for c,v in edades.items():
     print(c,v)

print("PILAS")
pila=[3,4,5]
pila.append(6)
pila.append(7)
print(pila)
n=pila.pop()
print(pila)
print(n)

cola=deque()
print(cola)
cola=deque(['Hector','Juan'])
print(cola)
cola.append("Maria")
print(cola)
n=cola.popleft()
print(cola)
print(n)