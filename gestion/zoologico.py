from gestion.zona import Zona
class Zoologico():
    def __init__(self,nombre,ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]

    def agregarZonas(self,zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        cantidad=0
        for zo in self._zonas:
            cantidad+=zo.cantidadAnimales()
        return cantidad
    
    def getZona(self):
        return self._zonas
    
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

