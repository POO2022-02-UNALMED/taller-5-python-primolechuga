from zooAnimales.animal import Animal
class Ave(Animal):
    listado=[]
    halcones=0
    aguilas=0
    def __init__(self, nombre, edad, habitat, genero,colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas=colorPlumas
        Ave.listado.append(self)

    def movimiento(self):
        return "volar"

    @classmethod
    def cantidadAves(cls):
        return len(Ave.listado)

    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        Ave.halcones+=1
        halcon=Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        return halcon

    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        Ave.aguilas+=1
        aguila=Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
        return aguila
    #getters setters