import AlgeVidav2.clases.Mascota as Mascota


def generarCodigo(self, codigo):
    if codigo is None:
        codigo = "GAT{}".format(obtener_num_clinica(self))
    return codigo


def obtener_num_clinica(self):
    file = open("listas/numGatos.txt", "r")
    numero = int(file.readline())
    numero += 1

    file2 = open("listas/numGatos.txt", "w")
    file2.write("{}".format(numero))

    file.close()
    file2.close()

    return numero


class Gato(Mascota.Mascota):
    def __init__(self, nombre, fecNacimiento, fecRegistro, disponible, pelaje, sociable, codigo=None):
        Mascota.Mascota.__init__(self, nombre, fecNacimiento, fecRegistro, disponible, generarCodigo(self, codigo))
        self.pelaje = pelaje
        self.sociable = sociable
