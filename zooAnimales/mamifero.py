from zooAnimales.animal import Animal
class Mamifero(Animal):
    caballos=0
    leones=0
    listado=[]
    def __init__(self, nombre, edad, habitat, genero,pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje=pelaje
        self.patas=patas
        Mamifero.listado.append(self)
    @classmethod
    def cantidadMamiferos(cls):
        return len(Mamifero.listado)
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
        return self.pelaje