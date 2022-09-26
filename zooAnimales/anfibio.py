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
    def cantidadAnfibios(cls):
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

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero
        
    def __str__(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"