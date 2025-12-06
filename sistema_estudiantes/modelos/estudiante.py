from .persona import Persona
class Estudiante(Persona):
    def __init__(self, cedula, nombre, edad, carrera):
        super().__init__(cedula, nombre, edad)
        self.carrera = carrera

    def descripcion(self):
        return f"Estudiante {self.nombre} - {self.carrera}"