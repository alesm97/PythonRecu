from AlgeVidav2.clases.Persona import Persona


class Voluntario(Persona):
    def __init__(self, dni, telefono, direccion, email, intereses, habilidades):
        Persona.__init__(self, dni, telefono, direccion, email, intereses)
        self.habilidades = habilidades
