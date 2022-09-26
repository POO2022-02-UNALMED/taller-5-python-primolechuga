from zooAnimales.animal import Animal
class Anfibio(Animal):
    listado=[]
    ranas=0
    salamandras=0
    def __init__(self, nombre, edad, habitat, genero,colorPiel,venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio.listado.append(self)
    @classmethod
    def cantidadAnfibios():
        return len(Anfibio.listado)

    def movimiento(self):
        return "saltar"
    
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        Anfibio.ranas+=1
        rana=Anfibio(nombre,edad,"selva",genero,"rojo",True)
        return rana

    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        Anfibio.salamandras+=1
        salamandra=Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        return salamandra

    def isVenenoso(self):
        return self._venenoso

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, color):
        self._colorPiel = color