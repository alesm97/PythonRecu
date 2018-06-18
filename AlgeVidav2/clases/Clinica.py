def generarCodigo(self, codigo):
    if codigo is None:
        codigo = "CLI{}".format(obtener_num_clinica(self))
    return codigo


def obtener_num_clinica(self):
    file = open("listas/numClinicas.txt", "r")
    numero = int(file.readline())
    numero += 1

    file2 = open("listas/numClinicas.txt", "w")
    file2.write("{}".format(numero))

    file.close()
    file2.close()

    return numero


class Clinica(object):
    def __init__(self, direccion, telefono, email, titular, codigo=None):
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.titular = titular
        self.codigo = generarCodigo(self, codigo)
