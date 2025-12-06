from abc import ABC, abstractmethod

class BasePersona(ABC):
    def __init__(self, cedula, nombre):
        self._cedula = cedula
        self._nombre = nombre

    @property
    def cedula(self):
        return self._cedula
    
    @property
    def nombre(self):
        return self._nombre
    
    @abstractmethod
    def descripcion(self):
        """Debe implementarse en las clases hijas"""
        pass

