import AlgeVidav2.clases.Persona as Persona


class Veterinario(Persona.Persona):
    def __init__(self, dni, direccion, telefono, email, intereses, colegiado, especialidad, clinica):
        Persona.Persona(dni, direccion, telefono, email, intereses)
        self.colegiado = colegiado
        self.especialidad = especialidad
        self.clinica = clinica
