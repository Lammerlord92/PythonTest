def saludar():
    print("Hola!")

saludar()

def dibujaTablaMultiplicar(numero):
    print("Tabla del",numero)
    res=[]
    for i in range(10):
        res.append(str(numero)+"*"+str(i)+"="+"{:06d}".format(numero*i))
    return res

print(dibujaTablaMultiplicar(4))
print(dibujaTablaMultiplicar(6))

def doblar_valor(numero):
    return numero*2

def indeterminados_posicion(*args):
    for arg in args:
        print(arg)
indeterminados_posicion(5,"Hola",[1,2,3,4,5,6])
def indeterminados_nombre(**kwargs):
    print(kwargs)
indeterminados_nombre(n=5,s="Hola",l=[1,2,3,4,5,6])