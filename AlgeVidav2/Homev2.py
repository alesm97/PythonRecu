# region Variables
from xml.dom import minidom

from AlgeVidav2.clases.Clinica import Clinica
from AlgeVidav2.clases.Veterinario import Veterinario

funcionesMenuPrincipal = (
    "menuClinicas", "menuVeterinarios", "menuPropietarios", "menuMascotas", "menuAdopciones", "menuHTML", "Salir")
funcionesMenuClinica = ("listarClinicas", "agregarClinica", "eliminarClinica", "menuPrincipal")
funcionesMenuVeterinarios = (
    "listarVeterinarios", "agregarVeterinario", "eliminarVeterinario", "listarVeterinario", "menuPrincipal")
funcionesMenuPropietarios = (
    "listarPropietarios", "agregarPropietario", "eliminarPropietario", "menuPrincipal")
funcionesMenuMascotas = ("menuGatos", "menuPerros", "menuPrincipal")
funcionesMenuGatos = ("listarGatos", "agregarGato", "eliminarGato", "menuMascotas")
funcionesMenuPerros = ("listarPerros", "agregarPerro", "eliminarPerro", "menuMascotas")
funcionesMenuAdopciones = ("listarAdopciones", "agregarAdopcion", "eliminarAdopcion", "menuPrincipal")

clinicas = []
veterinarios = []
propietarios = []
gatos = []
perros = []
adopciones = []


# endregion

# region Menuses

# endregion

# region Carga de datos
def cargarDatos():
    cargarClinicas()
    cargarVeterinarios()
    cargarPropietarios()
    cargarGatos()
    cargarPerros()
    cargarAdopciones()


def cargarClinicas():
    docClinicas = minidom.parse('listas/listaClinicas.xml')
    if len(docClinicas.getElementsByTagName("clinica")) > 0:
        contador = 0
        for libro in docClinicas.getElementsByTagName("clinica"):
            direccion = libro.getElementsByTagName("direccion")[contador]
            telefono = libro.getElementsByTagName("telefono")[contador]
            email = libro.getElementsByTagName("email")[contador]
            titular = libro.getElementsByTagName("titular")[contador]
            codigo = libro.getElementsByTagName("codigo")[contador]

            globals()["clinicas"].append(
                Clinica(direccion.firstChild.data, telefono.firstChild.data, email.firstChild.data,
                        titular.firstChild.data, codigo.firstChild.data))


def cargarVeterinarios():
    docVeterinarios = minidom.parse('listas/listaVeterinarios.xml')
    if len(docVeterinarios.getElementsByTagName("veterinario")) > 0:
        contador = 0
        for libro in docVeterinarios.getElementsByTagName("veterinario"):
            dni = libro.getElementsByTagName("dni")[contador]
            direccion = libro.getElementsByTagName("direccion")[contador]
            telefono = libro.getElementsByTagName("telefono")[contador]
            email = libro.getElementsByTagName("email")[contador]
            intereses = libro.getElementsByTagName("intereses")[contador]
            colegiado = libro.getElementsByTagName("colegiado")[contador]
            especialidad = libro.getElementsByTagName("especialidad")[contador]
            clinica = libro.getElementsByTagName("clinica")[contador]

            globals()["clinicas"].append(
                Veterinario(dni.firstChild.data, direccion.firstChild.data, telefono.firstChild.data,
                            email.firstChild.data, intereses.firstChild.data, colegiado.firstChild.data,
                            especialidad.firstChild.data, clinica.firstChild.data))


def cargarPropietarios():
    docPropietarios = minidom.parse('listas/listaPropietarios.xml')
    if len(docPropietarios.getElementsByTagName("propietario")) > 0:
        contador = 0
        for libro in docPropietarios.getElementsByTagName("propietario"):
            dni = libro.getElementsByTagName("dni")[contador]
            direccion = libro.getElementsByTagName("direccion")[contador]
            telefono = libro.getElementsByTagName("telefono")[contador]
            email = libro.getElementsByTagName("email")[contador]
            intereses = libro.getElementsByTagName("intereses")[contador]
            colegiado = libro.getElementsByTagName("colegiado")[contador]
            especialidad = libro.getElementsByTagName("especialidad")[contador]
            clinica = libro.getElementsByTagName("clinica")[contador]

            globals()["clinicas"].append(
                Veterinario(dni.firstChild.data, direccion.firstChild.data, telefono.firstChild.data,
                            email.firstChild.data, intereses.firstChild.data, colegiado.firstChild.data,
                            especialidad.firstChild.data, clinica.firstChild.data))


# endregion

# region Listado de datos

# endregion

# region Agregación de datos

# endregion

# region Eliminación de datos

# endregion


# Main
cargarDatos()
menuPrincipal()
