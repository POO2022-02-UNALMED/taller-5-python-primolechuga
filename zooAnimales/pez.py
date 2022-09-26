
from zooAnimales.animal import Animal
class Pez(Animal):
    salmones=0
    bacalaos=0
    _listado=[]
    def __init__(self,nombre,edad,habitat, genero,color,cantidad):
        super().__init__(nombre,edad,habitat,genero)  
        self._colorEscamas=color
        self._cantidadAletas=cantidad
        Pez._listado.append(self)
    def movimiento(self):
        return "nadar"

    @classmethod
    def cantidadPeces(cls):
        return len(Pez._listado)
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        Pez.salmones+=1
        salmon=Pez(nombre,edad,"oceano",genero,"rojo",6)
        return salmon

    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        Pez.bacalaos+=1
        bacalao=Pez(nombre,edad,"oceano",genero,"gris",6)
        return bacalao
    #getters setters

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self,cantidad):
        self._cantidadAletas=cantidad
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