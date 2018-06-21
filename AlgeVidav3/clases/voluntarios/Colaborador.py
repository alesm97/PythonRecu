from AlgeVidav3.clases.voluntarios.Voluntario import Voluntario


def generar_codigo(self, codigo):
    if codigo is None:
        codigo = "CO-{}".format(obtener_num_col(self))
    return codigo


def obtener_num_col(self):
    file = open("listas/numColaboradores.txt", "r")
    numero = int(file.readline())
    numero += 1

    file2 = open("listas/numColaboradores.txt", "w")
    file2.write("{}".format(numero))

    file.close()
    file2.close()

    return numero


class Colaborador(Voluntario):
    def __init__(self, dni, telefono, direccion, email, intereses, habilidades, poblacion, disposicion, codigo=None):
        Voluntario.__init__(self, dni, telefono, direccion, email, intereses, habilidades)
        self.poblacion = poblacion
        self.disposicion = disposicion
        self.codigo = generar_codigo(self,codigo)
