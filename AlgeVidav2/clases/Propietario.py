import AlgeVidav2.clases.Persona as Persona


class Propietario(Persona.Persona):
    def __init__(self, dni, direccion, telefono, email, intereses, haTenidoMascota, conocAdiestramiento):
        Persona.Persona.__init__(self, dni, direccion, telefono, email, intereses)
        self.haTenidoMascota = haTenidoMascota
        self.conocAdiestramiento = conocAdiestramiento
