import datetime


class Mascota(object):
    def __init__(self, nombre, fecNacimiento, disponible, codigo):
        self.nombre = nombre
        self.fecNacimiento = fecNacimiento
        self.fecRegistro = datetime.datetime.now()
        self.disponible = disponible
        self.codigo = codigo
