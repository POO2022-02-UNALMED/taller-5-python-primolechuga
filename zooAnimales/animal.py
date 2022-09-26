
class Animal():
    _totalAnimales=0
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        Animal._totalAnimales+=1
    def movimiento(self):
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.anfibio import Anfibio
        cantMam=Mamifero.cantidadMamiferos()
        cantAve =Ave.cantidadAves()
        cantRep=Reptil.cantidadReptiles()
        cantPe=Pez.cantidadPeces()
        cantAnf=Anfibio.cantidadAnfibios()
        txt=f"Mamiferos: {cantMam}\nAves: {cantAve}\nReptiles: {cantRep}\nPeces: {cantPe}\nAnfibios: {cantAnf}"
        return txt
    @classmethod
    def getTotalAnimales(cls):
        return Animal._totalAnimales
    
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
