from zooAnimales.animal import Animal
class Mamifero(Animal):
    caballos=0
    leones=0
    _listado=[]
    def __init__(self, nombre, edad, habitat, genero,pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)
    @classmethod
    def cantidadMamiferos(cls):
        return len(Mamifero._listado)
    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        Mamifero.caballos+=1
        caballo=Mamifero(nombre,edad,"pradera",genero,True,4)
        return caballo
    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        Mamifero.leones+=1
        leon=Mamifero(nombre,edad,"selva",genero,True,4)
        return leon
    #getters setters
    def isPelaje(self):
        return self._pelaje
    def getPelaje(self):
        return self._pelaje
    def getPatas(self):
        return self._patas

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
