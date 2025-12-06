from .persona import Persona

class Profesor(Persona):
    def __init__(self, cedula, nombre, edad, especialidad):
        super().__init__(cedula, nombre, edad)
        self.especialidad = especialidad

    def descripcion(self):
        return f"Profesor - {self.nombre} - Especialidad en {self.especialidad}"