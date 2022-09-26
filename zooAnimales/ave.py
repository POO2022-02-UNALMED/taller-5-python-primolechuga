from zooAnimales.animal import Animal
class Ave(Animal):
    _listado=[]
    halcones=0
    aguilas=0
    def __init__(self, nombre, edad, habitat, genero,colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)

    def movimiento(self):
        return "volar"

    @classmethod
    def cantidadAves(cls):
        return len(Ave._listado)

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

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, color):
        self._colorPlumas = color

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

    def toString(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"