import Biblioteca.clases.Material as Material


def generar_codigo(self, codigo):
    if codigo == None:
        codigo = "PEL{}".format(obtener_num_pelicula(self))
    return codigo


def obtener_num_pelicula(self):
    file = open("listas/numPeliculas.txt", "r")
    numero = int(file.readline())
    numero += 1

    file2 = open("listas/numPeliculas.txt", "w")
    file2.write("{}".format(numero))

    file.close()
    file2.close()

    return numero


class Pelicula(Material.Material):
    def __init__(self, titulo, descripcion, ejemplar, director, actor_principal, publicacion, genero, codigo=None):
        Material.Material.__init__(self, titulo, descripcion, ejemplar, 3, generar_codigo(self, codigo))
        self.director = director
        self.actor_principal = actor_principal
        self.publicacion = publicacion
        self.genero = genero
