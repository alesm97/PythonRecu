import Biblioteca.clases.Material as Material


def generar_codigo(self, codigo):
    if codigo is None:
        codigo = "LIB{}".format(obtener_num_libro(self))
    return codigo


def obtener_num_libro(self):
    file = open("listas/numLibros.txt", "r")
    numero = int(file.readline())
    numero += 1

    file2 = open("listas/numLibros.txt", "w")
    file2.write("{}".format(numero))

    file.close()
    file2.close()

    return numero


class Libro(Material.Material):
    def __init__(self, titulo, descripcion, ejemplar, editorial, codigo=None):
        Material.Material.__init__(self, titulo, descripcion, ejemplar, 7, generar_codigo(self, codigo))
        self.editorial = editorial
