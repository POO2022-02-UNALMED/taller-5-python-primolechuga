
class Zona():
    def __init__(self,nombre="",zoo=None):
        self.nombre=nombre
        self.zoo=zoo
        self.animales=[]
    def agregarAnimales(self,animal):
        self.animales.append(animal)
    def cantidadAnimales(self):
        return len(self.animales)
    def getZoo(self):
        return self.zoo[0]
    def setZoo(self,zoo):
        self.zoo=zoo
    #setters y getters
