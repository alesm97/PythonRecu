from AlgeVidav3.clases.voluntarios.Voluntario import Voluntario


def generar_codigo(self, codigo):
    if codigo is None:
        codigo = "VET-{}".format(obtener_num_col(self))
    return codigo


def obtener_num_col(self):
    file = open("listas/numVetCol.txt", "r")
    numero = int(file.readline())
    numero += 1

    file2 = open("listas/numVetCol.txt", "w")
    file2.write("{}".format(numero))

    file.close()
    file2.close()

    return numero


class VeterinarioCol(Voluntario):
    def __init__(self, dni, telefono, direccion, email, intereses, habilidades, colegiado, codigo=None):
        Voluntario.__init__(self, dni, telefono, direccion, email, intereses, habilidades)
        self.colegiado = colegiado
        self.codigo = generar_codigo(self, codigo)
