class GestorPersonas:
    def __init__(self):
        self.personas = []
    
    def agregar(self, persona):
        self.personas.append(persona)

    def buscar(self, cedula):
        persona_es = None
        for p in self.personas:
            if p.cedula == cedula:
                persona_es = p
        return persona_es
    
    def eliminar(self, cedula):
        persona = self.buscar(cedula)
        if persona:
            self.personas.remove(persona)
            return True
        return False
    
    def listar(self):
        return self.personas
    
    def listar_descripcion(self):
        # descripciones = []
        # for p in self.personas:
        #     descripciones.append(p.descripcion())
        # return descripciones
        return [p.descripcion() for p in self.personas]
    



