# coding=utf-8
import xml.dom.minidom as minidom
import xml.etree.cElementTree as ET

from Biblioteca.clases.Libro import Libro
from Biblioteca.clases.Pelicula import Pelicula
from Biblioteca.clases.Prestamo import Prestamo
from Biblioteca.clases.Revista import Revista
from Biblioteca.clases.Usuario import Usuario

# region Variables
funcionesMenuPrincipal = ("menuLibros", "menuPeliculas", "menuRevistas", "menuPrestamos", "menuUsuarios", "Salir")
funcionesMenuLibros = ("listarLibros", "agregarLibro", "eliminarLibro", "listarLibros", "menuPrincipal")
funcionesMenuRevistas = ("listarRevistas", "agregarRevista", "eliminarRevista", "listarRevistas", "menuPrincipal")
funcionesMenuPeliculas = (
    "listarPeliculas", "agregarPelicula", "eliminarPelicula", "listarPeliculas", "menuPrincipal")
funcionesMenuUsuarios = ("listarUsuarios", "agregarUsuario", "eliminarUsuario", "menuPrincipal")
funcionesMenuPrestamos = ("listarPrestamos", "agregarPrestamo", "eliminarPrestamo", "menuPrincipal")

libros = []
revistas = []
peliculas = []
usuarios = []
prestamos = []

opcion = -1


# endregion

# region Menuses
def menuPrincipal():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             MENÚ PRINCIPAL            *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             1.- Libros                *\\")
    print("/*             2.- Películas             *\\")
    print("/*             3.- Revistas              *\\")
    print("/*             4.- Préstamos             *\\")
    print("/*             5.- Usuarios              *\\")
    print("/*             6.- Salir                 *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("consultar", 6)

    if funcionesMenuPrincipal[globals()["opcion"] - 1] in globals():
        if callable(globals()[funcionesMenuPrincipal[globals()["opcion"] - 1]]):
            globals()[funcionesMenuPrincipal[globals()["opcion"] - 1]]()
    # TODO salir si no existe la función avisando al usuario o programador


def menuLibros():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*                 LIBROS                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             1.- Listar                *\\")
    print("/*             2.- Añadir                *\\")
    print("/*             3.- Eliminar              *\\")
    print("/*             4.- Detalles              *\\")
    print("/*             5.- Volver                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("hacer", 6)

    if funcionesMenuLibros[opcion - 1] in globals():
        if callable(globals()[funcionesMenuLibros[opcion - 1]]):
            if globals()["opcion"] == 1:
                globals()[funcionesMenuLibros[opcion - 1]]("menuLibros")
            elif globals()["opcion"] == 4:
                globals()[funcionesMenuLibros[globals()["opcion"] - 1]]("menuLibros", True)
            else:
                globals()[funcionesMenuLibros[opcion - 1]]()


def menuRevistas():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*               REVISTAS                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             1.- Listar                *\\")
    print("/*             2.- Añadir                *\\")
    print("/*             3.- Eliminar              *\\")
    print("/*             4.- Detalles              *\\")
    print("/*             5.- Volver                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("hacer", 6)

    if funcionesMenuRevistas[globals()["opcion"] - 1] in globals():
        if callable(globals()[funcionesMenuRevistas[globals()["opcion"] - 1]]):
            if globals()["opcion"] == 1:
                globals()[funcionesMenuRevistas[globals()["opcion"] - 1]]("menuRevistas")
            elif globals()["opcion"] == 4:
                globals()[funcionesMenuRevistas[globals()["opcion"] - 1]]("menuRevistas", True)
            else:
                globals()[funcionesMenuRevistas[globals()["opcion"] - 1]]()


def menuPeliculas():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*               PELÍCULAS               *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             1.- Listar                *\\")
    print("/*             2.- Añadir                *\\")
    print("/*             3.- Eliminar              *\\")
    print("/*             4.- Detalles              *\\")
    print("/*             5.- Volver                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("hacer", 6)

    if funcionesMenuPeliculas[globals()["opcion"] - 1] in globals():
        if callable(globals()[funcionesMenuPeliculas[globals()["opcion"] - 1]]):
            if globals()["opcion"] == 1:
                globals()[funcionesMenuPeliculas[globals()["opcion"] - 1]]("menuPeliculas")
            elif globals()["opcion"] == 4:
                globals()[funcionesMenuPeliculas[globals()["opcion"] - 1]]("menuPeliculas", True)
            else:
                globals()[funcionesMenuPeliculas[globals()["opcion"] - 1]]()


def menuUsuarios():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*               USUARIOS                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             1.- Listar                *\\")
    print("/*             2.- Añadir                *\\")
    print("/*             3.- Eliminar              *\\")
    print("/*             4.- Volver                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("hacer", 5)

    if funcionesMenuUsuarios[globals()["opcion"] - 1] in globals():
        if callable(globals()[funcionesMenuUsuarios[globals()["opcion"] - 1]]):
            if globals()["opcion"] == 1:
                globals()[funcionesMenuUsuarios[globals()["opcion"] - 1]]("menuUsuarios")
            else:
                globals()[funcionesMenuUsuarios[globals()["opcion"] - 1]]()


def menuPrestamos():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*              PRÉSTAMOS                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             1.- Listar                *\\")
    print("/*             2.- Añadir                *\\")
    print("/*             3.- Eliminar              *\\")
    print("/*             4.- Volver                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("hacer", 5)

    if funcionesMenuPrestamos[globals()["opcion"] - 1] in globals():
        if callable(globals()[funcionesMenuPrestamos[globals()["opcion"] - 1]]):
            if opcion == 1:
                globals()[funcionesMenuPrestamos[globals()["opcion"] - 1]]("menuPrestamos")
            else:
                globals()[funcionesMenuPrestamos[globals()["opcion"] - 1]]()


# endregion

# region Carga de datos

# Función para la carga total de los datos de los .xml
def cargarDatos():
    cargarLibros()
    cargarPeliculas()
    cargarRevistas()
    cargarPrestamos()
    cargarUsuarios()


# Funciones para cargar cada tipo de dato por separado.
def cargarLibros():
    docLibros = minidom.parse('listas/listaLibros.xml')
    if len(docLibros.getElementsByTagName("libro")) > 0:
        contador = 0
        for libro in docLibros.getElementsByTagName("libro"):
            titulo = libro.getElementsByTagName("titulo")[contador]
            descripcion = libro.getElementsByTagName("descripcion")[contador]
            ejemplar = libro.getElementsByTagName("ejemplar")[contador]
            editorial = libro.getElementsByTagName("editorial")[contador]
            codigo = libro.getElementsByTagName("codigo")[contador]

            globals()["libros"].append(
                Libro(titulo.firstChild.data, descripcion.firstChild.data, ejemplar.firstChild.data,
                      editorial.firstChild.data, codigo.firstChild.data))


def cargarRevistas():
    docRevistas = minidom.parse('listas/listaRevistas.xml')
    if len(docRevistas.getElementsByTagName("revista")) > 0:
        contador = 0
        for revista in docRevistas.getElementsByTagName("revista"):
            titulo = revista.getElementsByTagName("titulo")[contador]
            descripcion = revista.getElementsByTagName("descripcion")[contador]
            ejemplar = revista.getElementsByTagName("ejemplar")[contador]
            tematica = revista.getElementsByTagName("tematica")[contador]
            mes = revista.getElementsByTagName("mes_publicacion")[contador]
            anho = revista.getElementsByTagName("anho_publicacion")[contador]
            codigo = revista.getElementsByTagName("codigo")[contador]

            globals()["revistas"].append(
                Revista(titulo.firstChild.data, descripcion.firstChild.data, ejemplar.firstChild.data,
                        tematica.firstChild.data, mes.firstChild.data, anho.firstChild.data, codigo.firstChild.data))


def cargarPeliculas():
    docPeliculas = minidom.parse('listas/listaPeliculas.xml')
    if len(docPeliculas.getElementsByTagName("pelicula")) > 0:
        contador = 0
        for pelicula in docPeliculas.getElementsByTagName("pelicula"):
            titulo = pelicula.getElementsByTagName("titulo")[contador]
            descripcion = pelicula.getElementsByTagName("descripcion")[contador]
            ejemplar = pelicula.getElementsByTagName("ejemplar")[contador]
            director = pelicula.getElementsByTagName("director")[contador]
            actor_principal = pelicula.getElementsByTagName("actor_principal")[contador]
            publicacion = pelicula.getElementsByTagName("publicacion")[contador]
            genero = pelicula.getElementsByTagName("genero")[contador]
            codigo = pelicula.getElementsByTagName("codigo")[contador]

            globals()["peliculas"].append(
                Pelicula(titulo.firstChild.data, descripcion.firstChild.data, ejemplar.firstChild.data,
                         director.firstChild.data, actor_principal.firstChild.data, publicacion.firstChild.data,
                         genero.firstChild.data, codigo.firstChild.data))


def cargarUsuarios():
    docUsuarios = ET.ElementTree(file='listas/listaUsuarios.xml').getroot()
    if len(docUsuarios) > 0:
        for usuario in docUsuarios:
            globals()["usuarios"].append(Usuario(usuario[0].text, usuario[1].text, usuario[2].text))


def cargarPrestamos():
    docPrestamos = ET.ElementTree(file='listas/listaPrestamos.xml').getroot()
    if len(docPrestamos) > 0:
        for prestamo in docPrestamos:
            globals()["prestamos"].append(Prestamo(prestamo[0].text, prestamo[1].text, prestamo[2].text))


# endregion

# region Guardado de datos
def guardarDatos():
    guardarLibros()
    guardarPeliculas()
    guardarRevistas()
    guardarUsuarios()
    guardarPrestamos()


def guardarLibros():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaLibros", None)
    docRoot = miXML.documentElement
    for libro in globals()["libros"]:
        nodo = miXML.createElement("libro")
        elemento = miXML.createElement("titulo")
        elemento.appendChild(miXML.createTextNode(libro.titulo))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("descripcion")
        elemento.appendChild(miXML.createTextNode(libro.descripcion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("ejemplar")
        elemento.appendChild(miXML.createTextNode(str(libro.ejemplar)))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("editorial")
        elemento.appendChild(miXML.createTextNode(libro.editorial))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("codigo")
        elemento.appendChild(miXML.createTextNode(libro.codigo))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaLibros.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarRevistas():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaRevistas", None)
    docRoot = miXML.documentElement
    for revista in globals()["revistas"]:
        nodo = miXML.createElement("libro")
        elemento = miXML.createElement("titulo")
        elemento.appendChild(miXML.createTextNode(revista.titulo))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("descripcion")
        elemento.appendChild(miXML.createTextNode(revista.descripcion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("ejemplar")
        elemento.appendChild(miXML.createTextNode(str(revista.ejemplar)))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("tematica")
        elemento.appendChild(miXML.createTextNode(revista.tematica))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("mes_publicacion")
        elemento.appendChild(miXML.createTextNode(revista.mes_publicacion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("anho_publicacion")
        elemento.appendChild(miXML.createTextNode(revista.anho_publicacion))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaRevistas.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarPeliculas():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaLibros", None)
    docRoot = miXML.documentElement
    for libro in globals()["libros"]:
        nodo = miXML.createElement("libro")
        elemento = miXML.createElement("titulo")
        elemento.appendChild(miXML.createTextNode(libro.titulo))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("descripcion")
        elemento.appendChild(miXML.createTextNode(libro.descripcion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("ejemplar")
        elemento.appendChild(miXML.createTextNode(str(libro.ejemplar)))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("editorial")
        elemento.appendChild(miXML.createTextNode(libro.editorial))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("codigo")
        elemento.appendChild(miXML.createTextNode(libro.codigo))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaPeliculas.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarUsuarios():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaUsuarios", None)
    docRoot = miXML.documentElement
    for usuario in globals()["usuarios"]:
        nodo = miXML.createElement("usuario")
        elemento = miXML.createElement("dni")
        elemento.appendChild(miXML.createTextNode(usuario.dni))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("nombre")
        elemento.appendChild(miXML.createTextNode(usuario.nombre))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("apellidos")
        elemento.appendChild(miXML.createTextNode(usuario.apellidos))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaUsuarios.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarPrestamos():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaPrestamos", None)
    docRoot = miXML.documentElement
    for prestamo in globals()["prestamos"]:
        nodo = miXML.createElement("prestamo")
        elemento = miXML.createElement("dni")
        elemento.appendChild(miXML.createTextNode(prestamo.dni))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("articulo")
        elemento.appendChild(miXML.createTextNode(prestamo.articulo))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("duracion")
        elemento.appendChild(miXML.createTextNode(str(prestamo.duracion)))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaPrestamos.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


# endregion

# region Listado de datos
def listarLibros(menu, detalles=False):
    contador = 0
    if len(globals()["libros"]) > 0:
        for libro in globals()["libros"]:
            contador += 1
            if not detalles:
                print("{} -> Código: {} Título: {} Disponible: {}".format(contador, libro.codigo, libro.titulo,
                                                                          "Sí" if int(libro.ejemplar) > 0 else "No"))
            else:
                print(
                    "{} -> Código: {} -- Título: {} -- Disponible: {} -- Editorial: {} -- Ejemplares: {} -- Días de prestamo: {}".format(
                        contador, libro.codigo, libro.titulo, "Sí" if int(libro.ejemplar) > 0 else "No",
                        libro.editorial, libro.ejemplar, libro.prestamo))
    else:
        print("No hay libros registrados")
    if menu is not None:
        globals()[menu]()


def listarRevistas(menu, detalles=False):
    contador = 0
    if len(globals()["revistas"]) > 0:
        for revista in globals()["revistas"]:
            contador += 1
            if not detalles:
                print("{} -> Código: {} Título: {} Disponible: {}".format(contador, revista.codigo, revista.titulo,
                                                                          "Sí" if int(revista.ejemplar) > 0 else "No"))
            else:
                print(
                    "{} -> Código: {} -- Título: {} -- Disponible: {} -- Descripción: {} -- Ejemplares: {} -- Temática: {} "
                    "-- Publicación: {}/{}".format(
                        contador, revista.codigo, revista.titulo, "Sí" if int(revista.ejemplar) > 0 else "No",
                        revista.descripcion, revista.ejemplar, revista.tematica, revista.mes_publicacion,
                        revista.anho_publicacion))
    else:
        print("No hay revistas registradas")
    if menu is not None:
        globals()[menu]()


def listarPeliculas(menu, detalles=False):
    contador = 0
    if len(globals()["peliculas"]) > 0:
        for pelicula in globals()["peliculas"]:
            contador += 1
            if not detalles:
                print("{} -> Código: {} Título: {} Disponible: {}".format(contador, pelicula.codigo, pelicula.titulo,
                                                                          "Sí" if int(pelicula.ejemplar) > 0 else "No"))
            else:
                print(
                    "{} -> Código: {} -- Título: {} -- Disponible: {} -- Sinopsis: {} -- Ejemplares: {} -- Días de prestamo: {}".format(
                        contador, pelicula.codigo, pelicula.titulo, "Sí" if int(pelicula.ejemplar) > 0 else "No",
                        pelicula.descripcion, pelicula.ejemplar, pelicula.prestamo))
    else:
        print("No hay películas registradas")
    if menu is not None:
        globals()[menu]()


def listarUsuarios(menu):
    contador = 0
    if len(globals()["usuarios"]) > 0:
        for usuario in globals()["usuarios"]:
            contador += 1
            print("{} -> DNI: {} Nombre: {} Apellidos: {}".format(contador, usuario.dni, usuario.nombre,
                                                                  usuario.apellidos))
    else:
        print("No hay usuarios registrados")
    if menu is not None:
        globals()[menu]()


def listarPrestamos(menu):
    contador = 0
    if len(globals()["prestamos"]) > 0:
        for prestamo in globals()["prestamos"]:
            contador += 1
            print("{} -> DNI: {} Artículo: {} Días de préstamo: {}".format(contador, prestamo.dni, prestamo.articulo,
                                                                           prestamo.duracion))
    else:
        print("No hay prestamos registrados")
    if menu is not None:
        globals()[menu]()


# endregion

# region Agregación de datos
def agregarLibro():
    valido = False
    titulo = input("Introduzca el título: ")
    descripcion = input("Introduzca la descripción: ")
    ejemplares = 0
    editorial = input("Introduzca la editorial: ")
    while not valido or ejemplares <= 0:
        try:
            ejemplares = int(input("Introduzca el número de ejemplares"))
            valido = True
        except ValueError:
            print("Debe introducir un número.")
            # valido = False
        if ejemplares <= 0:
            print("El valor debe ser mayor a 0.")
            valido = False

    globals()["libros"].append(Libro(titulo, descripcion, ejemplares, editorial))
    globals()["guardarLibros"]()
    globals()["menuLibros"]()


def agregarRevista():
    valido = False
    titulo = input("Introduzca el título: ")
    descripcion = input("Introduzca la descripción: ")
    ejemplares = 0
    tematica = input("Introduzca la temática: ")
    anho = input("Introduzca el año de publicación: ")
    mes = input("Introduzca el mes de publicación: ")
    while not valido or ejemplares <= 0:
        try:
            ejemplares = int(input("Introduzca el número de ejemplares"))
            valido = True
        except ValueError:
            print("Debe introducir un número.")
        if ejemplares <= 0:
            print("El valor debe ser mayor a 0.")
    globals()["revistas"].append(Revista(titulo, descripcion, ejemplares, tematica, mes, anho))
    globals()["guardarRevistas"]()
    globals()["menuRevistas"]()


def agregarPelicula():
    valido = False
    titulo = input("Introduzca el título: ")
    descripcion = input("Introduzca la descripción: ")
    ejemplares = 0
    director = input("Introduzca el director: ")
    actor = input("Introduzca el actor principal: ")
    genero = input("Introduzca el género: ")
    publicacion = input("Introduzca la fecha de publicación: ")
    while not valido or ejemplares <= 0:
        try:
            ejemplares = int(input("Introduzca el número de ejemplares"))
            valido = True
        except ValueError:
            print("Debe introducir un número.")
        if ejemplares <= 0:
            print("El valor debe ser mayor a 0.")
    globals()["peliculas"].append(Pelicula(titulo, descripcion, ejemplares, director, actor, genero, publicacion))
    globals()["guardarPeliculas"]()
    globals()["menuPeliculas"]()


def agregarUsuario():
    valido = False
    repetido = False
    salir = False
    while (not valido or repetido) or salir:
        dni = input("Introduzca el dni (formato AAAAAAAAA0): ")
        if dni == "@salir":
            salir = True
        else:
            valido = validarDNI(dni)
            if not valido:
                print("DNI no válido")
            else:
                for usuario in globals()["usuarios"]:
                    if usuario.dni == dni:
                        repetido = True
                        print("Ya existe un usuario con ese DNI")
    if not salir:
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")

        globals()["usuarios"].append(Usuario(dni, nombre, apellidos))
        print("Usuario agregado con éxito.")
        listarUsuarios(None)
        globals()["guardarUsuarios"]()
        globals()["menuUsuarios"]()
    else:
        print("Usuario no agregado")
        globals()["menuUsuarios"]()


def agregarPrestamo():
    tipo = -1
    noNumero = True
    while 1 > tipo or tipo > 3 and noNumero:
        try:
            tipo = int(input("¿De qué desea hacer el préstamo?\n\t1.- Libro\n\t2.- Revista\n\t3.- Película"))
        except ValueError:
            print("Debe introducir un número.")
        if 1 > tipo > 3:
            print("Número no válido.")
        else:
            noNumero = False

    if tipo == 1:
        listarLibros(None)
        if len(globals()["libros"]) > 0:
            libro = int(input("¿De qué libro desea hacer el préstamo?"))
            if 0 > libro > len(globals()["libros"]):
                print("Número no válido.")
            else:
                if globals()["libros"][libro - 1].ejemplar == 0:
                    print("No hay ejemplares de ese libro.")
                else:
                    listarUsuarios(None)
                    if len(globals()["usuarios"]) > 0:
                        usuario = int(input("¿A qué usuario desea hacerle el préstamo?"))
                        if 0 > usuario > len(globals()["usuarios"]):
                            print("Usuario no válido.")
                        else:

                            globals()["prestamos"].append(
                                Prestamo(globals()["usuarios"][usuario - 1].dni, globals()["libros"][libro - 1].codigo,
                                         globals()["libros"][libro - 1].prestamo))
                            globals()["libros"][libro - 1].ejemplar = int(globals()["libros"][libro - 1].ejemplar) - 1
                            print("Préstamo añadido correctamente.")
                            globals()["guardarPrestamos"]()
                    else:
                        print("Préstamo cancelado.")
        else:
            print("Préstamo cancelado.")
    elif tipo == 2:
        listarRevistas(None)
        if len(globals()["revistas"]) > 0:
            revista = int(input("¿De qué revista desea hacer el préstamo?"))
            if 0 > revista > len(globals()["revistas"]):
                print("Número no válido.")
            else:
                if globals()["revistas"][revista - 1].ejemplar == 0:
                    print("No hay ejemplares de ese revista.")
                else:
                    listarRevistas(None)
                    if globals()["usuarios"] > 0:
                        usuario = int(input("¿A qué usuario desea hacerle el préstamo?"))
                        if 0 > usuario > len(globals()["usuarios"]):
                            print("Usuario no válido.")
                        else:
                            globals()["prestamos"].add(
                                Prestamo(globals()["usuarios"][usuario - 1].dni,
                                         globals()["revistas"][revista - 1].codigo,
                                         globals()["revistas"][revista - 1].prestamo))
                            globals()["revistas"][revista - 1].ejemplar = int(
                                globals()["revistas"][revista - 1].ejemplar) - 1
                            print("Préstamo añadido correctamente.")
                            globals()["guardarPrestamos"]()
                    else:
                        print("Préstamo cancelado.")
        else:
            print("Préstamo cancelado.")
    elif tipo == 3:
        listarPeliculas(None)
        if len(globals()["peliculas"]) > 0:
            pelicula = int(input("¿De qué pelicula desea hacer el préstamo?"))
            if 0 > pelicula > len(globals()["peliculas"]):
                print("Número no válido.")
            else:
                if globals()["peliculas"][pelicula - 1].ejemplar == 0:
                    print("No hay ejemplares de esa película.")
                else:
                    listarPeliculas(None)
                    if len(globals()["usuarios"]) > 0:
                        usuario = int(input("¿A qué usuario desea hacerle el préstamo?"))
                        if 0 > usuario > len(globals()["usuarios"]):
                            print("Usuario no válido.")
                        else:
                            globals()["prestamos"].add(
                                Prestamo(globals()["usuarios"][usuario - 1].dni,
                                         globals()["peliculas"][pelicula - 1].codigo,
                                         globals()["peliculas"][pelicula - 1].prestamo))
                            globals()["peliculas"][pelicula].ejemplar = int(
                                globals()["peliculas"][pelicula].ejemplar) - 1
                            print("Préstamo añadido correctamente.")
                            globals()["guardarPrestamos"]()
                    else:
                        print("Préstamo cancelado.")
        else:
            print("Préstamo cancelado.")
    globals()["menuPrestamos"]()


# endregion

# region Eliminación de Datos
def eliminarLibro():
    if tieneRegistros(globals()["libros"]):
        listarLibros(None)
        valido = False

        while not valido:
            try:
                eliminado = int(input("¿Qué libro desea eliminar? (Para salir introduzca -1): "))
                valido = True
            except ValueError:
                print("Debe introducir un número")
                valido = False

        if 0 > eliminado > len(globals()["libros"]):
            print("Número inválido")
        else:
            if eliminado == -1:
                print("Eliminación cancelada")
            else:
                globals()["libros"].pop(eliminado - 1)
                print("Eliminado correctamente")
                globals()["guardarLibros"]()
    else:
        print("No hay libros para eliminar")
    globals()["menuLibros"]()


def eliminarRevista():
    if tieneRegistros(globals()["revistas"]):
        listarRevistas(None)
        valido = False
        while not valido:
            try:
                eliminado = int(input("¿Qué revista desea eliminar? (Para salir introduzca -1): "))
                valido = True
            except ValueError:
                print("Debe introducir un número")
                valido = False

        if 0 > eliminado > len(globals()["revistas"]):
            print("Número inválido")
        else:
            if eliminado == -1:
                print("Eliminación cancelada")
                globals()["menuRevistas"]()
            else:
                globals()["revistas"].pop(eliminado - 1)
                print("Eliminada correctamente")
                globals()["guardarRevistas"]()
    else:
        print("No hay revistas para eliminar")
    globals()["menuRevistas"]()


def eliminarPelicula():
    if tieneRegistros(globals()["peliculas"]):
        listarPeliculas(None)
        valido = False
        while not valido:
            try:
                eliminado = int(input("¿Qué revista desea eliminar? (Para salir introduzca -1): "))
                valido = True
            except ValueError:
                print("Debe introducir un número")
                valido = False

        if 0 > eliminado > len(globals()["peliculas"]):
            print("Número inválido")
        else:
            if eliminado == -1:
                print("Eliminación cancelada")
                globals()["menuPeliculas"]()
            else:
                globals()["libros"].pop(eliminado - 1)
                print("Eliminado correctamente")
                globals()["guardarPeliculas"]()
    else:
        print("No hay películas para eliminar.")
    globals()["menuPeliculas"]()


def eliminarUsuario():
    if tieneRegistros(globals()["usuarios"]):
        listarUsuarios(None)
        valido = False
        while not valido:
            try:
                eliminado = int(input("¿Qué usuario desea eliminar? (Para salir introduzca -1): "))
                valido = True
            except ValueError:
                print("Debe introducir un número")
                valido = False

        if 0 > eliminado > len(peliculas):
            print("Número inválido")
        else:
            if eliminado == -1:
                print("Eliminación cancelada")
            else:
                globals()["usuarios"].pop(eliminado - 1)
                print("Eliminado correctamente")
                globals()["guardarUsuarios"]()
    else:
        print("No hay usuarios para eliminar")
    globals()["menuUsuarios"]()


def eliminarPrestamo():
    if tieneRegistros(globals()["prestamos"]):
        listarPrestamos(None)
        valido = False
        while not valido:
            try:
                eliminado = int(input("¿Qué préstamo desea eliminar? (Para salir introduzca -1): "))
                valido = True
            except ValueError:
                print("Debe introducir un número")
                valido = False

        if 0 > eliminado > len(prestamos):
            print("Número inválido")
        else:
            if eliminado == -1:
                print("Eliminación cancelada")
            else:
                articulo = globals()["prestamos"][eliminado - 1].articulo
                if articulo.startswith("LIB"):
                    for libro in globals()["libros"]:
                        if libro.codigo == articulo:
                            libro.ejemplar = int(libro.ejemplar) + 1
                elif articulo.startswith("REV"):
                    for revista in globals()["revistas"]:
                        if revista.codigo == articulo:
                            revista.ejemplar = int(revista.ejemplar) + 1
                elif articulo.startswith("PEL"):
                    for pelicula in globals()["peliculas"]:
                        if pelicula.codigo == articulo:
                            pelicula.ejemplar = int(pelicula.ejemplar) + 1
                globals()["prestamos"].pop(eliminado - 1)
                print("Eliminado correctamente")
                globals()["guardarPrestamos"]()
    else:
        print("No hay prestamos para eliminar")
    globals()["menuPrestamos"]()


# endregion

# region Otras Funciones
# Función que finaliza la ejecución del programa.
def Salir():
    exit(0)


# Función para preguntarle al usuario que opción desea escoger.
def preguntarMenu(verbo, opciones):
    while 1 > globals()["opcion"] or globals()["opcion"] > opciones:
        try:
            globals()["opcion"] = int(input("¿Qué desesa " + verbo + "?"))
        except ValueError:
            globals()["opcion"] = -1
            print("Debe introducir un número.")
        if globals()["opcion"] < 1 or globals()["opcion"] > opciones:
            print("Número inválido.")


# Función que valida un DNI
def validarDNI(dni):
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    numeros = "1234567890"
    valido = False
    if len(dni) == 9:
        letraControl = dni[8].upper()
        dni2 = dni[:8]
        if len(dni2) == len([n for n in dni2 if n in numeros]):
            if tabla[int(dni2) % 23] == letraControl:
                valido = True
    return valido


# Función que devuelve si la lista tiene mas elementos
def tieneRegistros(lista):
    if len(lista) > 0:
        valido = True
    else:
        valido = False
    return valido


# endregion

# MAIN
globals()["prestamos"] = list(globals()["prestamos"])
cargarDatos()
menuPrincipal()
