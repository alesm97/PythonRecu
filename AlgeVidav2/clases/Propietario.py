import AlgeVidav2.clases.Persona as Persona


class Veterinario(Persona.Persona):
    def __init__(self, dni, direccion, telefono, email, intereses, haTenidoMascota, conocAdiestramiento):
        Persona.Persona(dni, direccion, telefono, email, intereses)
        self.haTenidoMascota = haTenidoMascota
        self.conocAdiestramiento = conocAdiestramiento
