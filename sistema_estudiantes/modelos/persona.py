from .base import BasePersona
class Persona(BasePersona):
    def __init__(self, cedula, nombre, edad):
        super().__init__(cedula, nombre)
        self._edad = edad

    @property
    def edad(self):
        return self._edad
    
    def descripcion(self):
        return f"{self.nombre}, {self.edad} años"