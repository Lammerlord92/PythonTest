class Cliente:
    def __init__(self,dni,nombre,apellidos):
        self.dni=dni
        self.nombre=nombre
        self.apellidos=apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)


class Empresa:
    def __init__(self,clientes=[]):
        self.clientes=clientes
    def mostrar_cliente(self,dni=None):
        for c in self.clientes:
            if c.dni==dni:
                print(c)
                return
        print("Cliente no encontrado")







hector=Cliente(nombre="Hector",apellidos="Costa Guzman",dni="11111111A")

empresa=Empresa([hector])
empresa.mostrar_cliente("11111111A")