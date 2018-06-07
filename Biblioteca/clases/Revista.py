import Biblioteca.clases.Material as Material


def generar_codigo(self, codigo):
    if codigo is None:
        codigo = "REV{}".format(obtener_num_revista(self))
    return codigo


def obtener_num_revista(self):
    file = open("listas/numRevistas.txt", "r")
    numero = int(file.readline())
    numero += 1

    file2 = open("listas/numRevistas.txt", "w")
    file2.write("{}".format(numero))

    file.close()
    file2.close()

    return numero


class Revista(Material.Material):
    def __init__(self, titulo, descripcion, ejemplar, tematica, mes_publicacion, anho_publicacion, codigo=None):
        Material.Material.__init__(self, titulo, descripcion, ejemplar, 10, generar_codigo(self, codigo))
        self.tematica = tematica
        self.mes_publicacion = mes_publicacion
        self.anho_publicacion = anho_publicacion
