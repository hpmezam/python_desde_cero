class Vehiculo:
    def __init__(self, marca, tipo_combustible):
        self.marca = marca # público
        self._tipo_combustible = tipo_combustible # protegido
        self.__velocidad = 0 # privado

    # Método común
    def encender(self):
        return "El vehiculo está encendiendo..."
    
    def acelerar(self, cantidad):
        self.__velocidad += cantidad

    def frenar(self, cantidad):
        self.__velocidad += cantidad
        if self.__velocidad < 0:
            self.__velocidad = 0

    def obtener_velocidad(self):
        return self.__velocidad
    
class  Auto(Vehiculo):
    def __init__(self, marca, tipo_combustible, puertas):
        super().__init__(marca, tipo_combustible)
        self.puertas = puertas

    def encender(self):
        return f"El auto {self.marca} esta encendiendo con llave."
    
class Moto(Vehiculo):
    def __init__(self, marca, tipo_combustible, cilindraje):
        super().__init__(marca, tipo_combustible)
        self.cilindraje = cilindraje