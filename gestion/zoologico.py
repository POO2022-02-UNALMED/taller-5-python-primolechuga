from gestion.zona import Zona
class Zoologico():
    def __init__(self,nombre,ubicacion):
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.zonas=[]
    def agregarZonas(self,zona):
        self.zonas.append(zona)

    def cantidadTotalAnimales(self):
        cantidad=0
        for zona in self.zonas:
            cantidad+=zona.cantidadAnimales
        return cantidad
    
    def getZona(self):
        return self.zonas
    
    def setZona(self, zona):
        self._zona = zona
        
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

