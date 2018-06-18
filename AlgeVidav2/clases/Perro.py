import AlgeVidav2.clases.Mascota as Mascota


def generarCodigo(self, codigo):
    if codigo is None:
        codigo = "PER{}".format(obtener_num_clinica(self))
    return codigo


def obtener_num_clinica(self):
    file = open("listas/numPerros.txt", "r")
    numero = int(file.readline())
    numero += 1

    file2 = open("listas/numPerros.txt", "w")
    file2.write("{}".format(numero))

    file.close()
    file2.close()

    return numero


class Perro(Mascota):
    def __init__(self, nombre, fecNacimiento, disponible, raza, habilidades, codigo=None):
        Mascota.Mascota(nombre, fecNacimiento, disponible, generarCodigo(self, codigo))
        self.raza = raza
        self.habilidades = habilidades
