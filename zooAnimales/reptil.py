from zooAnimales.animal import Animal
class Reptil(Animal):
    iguanas=0
    serpientes=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,color,largoCola):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=color
        self._largoCola=largoCola
        Reptil._listado.append(self)
    
    def movimiento(self):
        return "reptar"
    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        Reptil.iguanas+=1
        iguana=Reptil(nombre,edad,"humedal",genero,"verde",3)
        return iguana

    @classmethod
    def crearSerpiente(cls,nombre, edad, genero):
        Reptil.serpientes+=1
        serpiente=Reptil(nombre,edad,"jungla",genero,"blanco",1)
        return serpiente

    @classmethod
    def cantidadReptiles():
        return len(Reptil._listado)

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
        
    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
        
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