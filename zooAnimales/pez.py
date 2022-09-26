
from zooAnimales.animal import Animal
class Pez(Animal):
    salmones=0
    bacalaos=0
    _listado=[]
    def __init__(self,nombre,edad,habitat, genero,color,cantidad):
        super().__init__(nombre,edad,habitat,genero)  
        self._colorEsxamas=color
        self._cantidadAletas=cantidad
        Pez._listado.append(self)
    def movimiento(self):
        return "nadar"

    @classmethod
    def cantidadPeces(cls):
        return len(Pez.listado)
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        Pez.salmones+=1
        salmon=Pez(nombre,edad,"oceano",genero,"gris",6)
        return salmon

    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        Pez.salmones+=1
        salmon=Pez(nombre,edad,"oceano",genero,"gris",6)
        return salmon
    #getters setters

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
        
    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self,cantidad):
        self._cantidadAletas=cantidad