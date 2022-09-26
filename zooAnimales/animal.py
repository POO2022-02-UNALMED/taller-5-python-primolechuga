
class Animal():
    totalAnimales=0
    def __init__(self,nombre,edad,habitat,genero):
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        Animal.totalAnimales+=1
    def movimiento(self):
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.anfibio import Anfibio
        x=("Mamiferos: "+Mamifero.cantidadMamiferos()+"\n"
        +"Aves: "+Ave.cantidadAves()+"\n"
        +"Reptiles: "+Reptil.cantidadReptiles()+"\n"
        +"Peces: "+Pez.cantidadPeces()+"\n"
        +"Anfibios: "+Anfibio.cantidadAnfibios())
        return x

    @classmethod
    def getTotalAnimales(cls):
        return Animal.totalAnimales

    def __str__(self):
        return("mi nombre es",self.nombre,"tengo una edad de")#falta terminar
