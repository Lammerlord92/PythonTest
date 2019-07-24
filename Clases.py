class Galleta:
    pass


galleta1=Galleta()
galleta2=Galleta()

print(type(galleta1))



galleta1.sabor="Salado"

galleta1.color="Marrón"



class GalletaV2():
    chocolate=False
    def __init__(self):
        print("Galleta creada")
    def chocolatear(self):
        self.chocolate=True


g=GalletaV2()


class GalletaV3():
    chocolate = False

    def __init__(self,sabor,forma):
        print("Galleta creada:{},{}".format(sabor,forma))

    def chocolatear(self):
        self.chocolate = True


g = GalletaV3("Salada","cuadrada")


class Película():
    chocolate = False
    #Redefinir constructor
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento
        print("Se ha creado la película ",self.titulo)

    # Redefinir toString
    def __str__(self):
        return "{}, lanzada en {} con una duración de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)

    # Redefinir longitud
    def __len__(self):
        return self.duracion

    # Redefinir borrado
    def __del__(self):
        print("Se está borrando la película",self.titulo)


p = Película("El Padrino", 175,1997)
print(len(p))
print(str(p))
del(p)

class Catalogo:
    peliculas=[]
    __atributo_privado="inalcanzable desde fuera"

    def __init__(self,peliculas=[]):
        set.peliculas=peliculas

    def agregar(self,p):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)

    def __metodo_privado(self):
        print("Método privado")

class Corto(Película):
    def __init__(self,titulo,duracion,lanzamiento):
        #Película.__init__(self,titulo,duracion,lanzamiento)
        super().__init__(self,titulo,duracion,lanzamiento)
        print("Se ha creado el corto",self.titulo)

    def __str__(self):
        return "{}, lanzado en {} con una duración de {} segundos".format(self.titulo, self.lanzamiento, self.duracion)


a=Corto("Trailer El Padrino", 50,1997)
print(a)

class A:
    def __init__(self):
        print("Objeto clase A")


class A:
    def __init__(self):
        print("Objeto clase A")
    def a(self):
        print("Método heredado clase A")



class B:
    def __init__(self):
        print("Objeto clase B")
    def b(self):
        print("Método heredado clase B")


class C(B,A):
    def c(self):
        print("Método clase")
    pass

c=C()
c.a()
c.b()
c.c()