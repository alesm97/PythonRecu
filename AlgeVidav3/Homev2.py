import webbrowser
from datetime import datetime
from xml.dom import minidom

from AlgeVidav2.clases.Adopcion import Adopcion
from AlgeVidav2.clases.Clinica import Clinica
from AlgeVidav2.clases.Gato import Gato
from AlgeVidav2.clases.Perro import Perro
from AlgeVidav2.clases.Veterinario import Veterinario
from AlgeVidav2.clases.Propietario import Propietario

# region Variables
from AlgeVidav3.clases.Trabajo import Trabajo
from AlgeVidav3.clases.Vacuna import Vacuna
from AlgeVidav3.clases.voluntarios.Colaborador import Colaborador
from AlgeVidav3.clases.voluntarios.VeterinarioCol import VeterinarioCol

funcionesMenuPrincipal = (
    "menuClinicas", "menuVeterinarios", "menuPropietarios", "menuMascotas", "menuAdopciones", "menuVoluntarios",
    "menuTrabajos", "menuVacunas", "menuHTML", "Salir")
funcionesMenuClinicas = ("listarClinicas", "agregarClinica", "eliminarClinica", "menuPrincipal")
funcionesMenuVeterinarios = (
    "listarVeterinarios", "agregarVeterinario", "eliminarVeterinario", "menuPrincipal")
funcionesMenuPropietarios = (
    "listarPropietarios", "agregarPropietario", "eliminarPropietario", "menuPrincipal")
funcionesMenuMascotas = ("menuGatos", "menuPerros", "menuPrincipal")
funcionesMenuPerros = ("listarPerros", "agregarPerro", "eliminarPerro", "menuMascotas")
funcionesMenuGatos = ("listarGatos", "agregarGato", "eliminarGato", "menuMascotas")
funcionesMenuHTML = ("mostrarAdopcionesHTML", "mostrarClinicasHTML", "mostrarMascotasHTML", "menuPrincipal")
funcionesMenuAdopciones = ("listarAdopciones", "agregarAdopcion", "eliminarAdopcion", "menuPrincipal")
funcionesMenuVoluntarios = ("menuColaboradores", "menuVetCol", "menuPrincipal")
funcionesMenuColaboradores = ("listarColaboradores", "agregarColaborador", "eliminarColaborador", "menuVoluntarios")
funcionesMenuVetCol = ("listarVeterinariosCol", "agregarVeterinarioCol", "eliminarVeterinarioCol", "menuVoluntarios")
funcionesMenuTrabajos = ("listarTrabajos", "agregarTrabajo", "menuPrincipal")
funcionesMenuVacunas = ("listarVacunas", "agregarVacuna", "menuPrincipal")

clinicas = []
veterinarios = []
propietarios = []
gatos = []
perros = []
adopciones = []
colaboradores = []
veterinariosCol = []
trabajos = []
vacunas = []

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
    print("/*             1.- Clínicas              *\\")
    print("/*             2.- Veterinarios          *\\")
    print("/*             3.- Propietarios          *\\")
    print("/*             4.- Mascotas              *\\")
    print("/*             5.- Adopciones            *\\")
    print("/*             6.- Voluntarios           *\\")
    print("/*             7.- Trabajos              *\\")
    print("/*             8.- Vacunas               *\\")
    print("/*             9.- HTML                  *\\")
    print("/*            10.- Salir                 *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("consultar", 11)

    if funcionesMenuPrincipal[globals()["opcion"] - 1] in globals():
        if callable(globals()[funcionesMenuPrincipal[globals()["opcion"] - 1]]):
            globals()[funcionesMenuPrincipal[globals()["opcion"] - 1]]()


def menuClinicas():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*                CLINICAS               *\\")
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

    if funcionesMenuClinicas[opcion - 1] in globals():
        if callable(globals()[funcionesMenuClinicas[opcion - 1]]):
            if globals()["opcion"] == 1:
                globals()[funcionesMenuClinicas[opcion - 1]]("menuClinicas")
            else:
                globals()[funcionesMenuClinicas[opcion - 1]]()


def menuVeterinarios():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*              VETERINARIOS             *\\")
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

    if funcionesMenuVeterinarios[opcion - 1] in globals():
        if callable(globals()[funcionesMenuVeterinarios[opcion - 1]]):
            if globals()["opcion"] == 1:
                globals()[funcionesMenuVeterinarios[opcion - 1]]("menuVeterinarios")
            else:
                globals()[funcionesMenuVeterinarios[opcion - 1]]()


def menuPropietarios():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*              PROPIETARIOS             *\\")
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

    if funcionesMenuPropietarios[opcion - 1] in globals():
        if callable(globals()[funcionesMenuPropietarios[opcion - 1]]):
            if globals()["opcion"] == 1:
                globals()[funcionesMenuPropietarios[opcion - 1]]("menuPropietarios")
            else:
                globals()[funcionesMenuPropietarios[opcion - 1]]()


def menuGatos():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*                 GATOS                 *\\")
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

    if funcionesMenuGatos[opcion - 1] in globals():
        if callable(globals()[funcionesMenuGatos[opcion - 1]]):
            if globals()["opcion"] == 1:
                globals()[funcionesMenuGatos[opcion - 1]]("menuGatos")
            else:
                globals()[funcionesMenuGatos[opcion - 1]]()


def menuPerros():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*                PERROS                 *\\")
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

    if funcionesMenuPerros[opcion - 1] in globals():
        if callable(globals()[funcionesMenuPerros[opcion - 1]]):
            if globals()["opcion"] == 1:
                globals()[funcionesMenuPerros[opcion - 1]]("menuPerros")
            else:
                globals()[funcionesMenuPerros[opcion - 1]]()


def menuMascotas():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*               MASCOTAS                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             1.- Gatos                 *\\")
    print("/*             2.- Perros                *\\")
    print("/*             3.- Volver                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("hacer", 4)

    if funcionesMenuMascotas[opcion - 1] in globals():
        if callable(globals()[funcionesMenuMascotas[opcion - 1]]):
            globals()[funcionesMenuMascotas[opcion - 1]]()


def menuAdopciones():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*              ADOPCIONES               *\\")
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

    if funcionesMenuAdopciones[opcion - 1] in globals():
        if callable(globals()[funcionesMenuAdopciones[opcion - 1]]):
            if globals()["opcion"] == 1:
                globals()[funcionesMenuAdopciones[opcion - 1]]("menuAdopciones")
            else:
                globals()[funcionesMenuAdopciones[opcion - 1]]()


def menuHTML():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*                  HTML                 *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             1.- Adopciones            *\\")
    print("/*             2.- Clinicas              *\\")
    print("/*             3.- Masc y Prop           *\\")
    print("/*             4.- Volver                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("hacer", 5)

    if funcionesMenuHTML[opcion - 1] in globals():
        if callable(globals()[funcionesMenuHTML[opcion - 1]]):
            globals()[funcionesMenuHTML[opcion - 1]]()


def menuVoluntarios():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*              VOLUNTARIOS              *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             1.- Colaboradores         *\\")
    print("/*             2.- Veteri. Col.          *\\")
    print("/*             3.- Volver                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("hacer", 5)

    if funcionesMenuVoluntarios[opcion - 1] in globals():
        if callable(globals()[funcionesMenuVoluntarios[opcion - 1]]):
            globals()[funcionesMenuVoluntarios[opcion - 1]]()


def menuVetCol():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*            VETERINARIOS COL           *\\")
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

    if funcionesMenuVetCol[opcion - 1] in globals():
        if callable(globals()[funcionesMenuVetCol[opcion - 1]]):
            if opcion == 1:
                globals()[funcionesMenuVetCol[opcion - 1]]("menuVetCol")
            else:
                globals()[funcionesMenuVetCol[opcion - 1]]()


def menuColaboradores():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             COLABORADORES             *\\")
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

    if funcionesMenuColaboradores[opcion - 1] in globals():
        if callable(globals()[funcionesMenuColaboradores[opcion - 1]]):
            if opcion == 1:
                globals()[funcionesMenuColaboradores[opcion - 1]]("menuColaboradores")
            else:
                globals()[funcionesMenuColaboradores[opcion - 1]]()


def menuTrabajos():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*                TRABAJOS               *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             1.- Listar                *\\")
    print("/*             2.- Añadir                *\\")
    print("/*             3.- Volver                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("hacer", 4)

    if funcionesMenuTrabajos[opcion - 1] in globals():
        if callable(globals()[funcionesMenuTrabajos[opcion - 1]]):
            globals()[funcionesMenuTrabajos[opcion - 1]]()


def menuVacunas():
    globals()["opcion"] = -1
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*                VACUNAS                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")
    print("/*                                       *\\")
    print("/*             1.- Listar                *\\")
    print("/*             2.- Añadir                *\\")
    print("/*             3.- Volver                *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("hacer", 4)

    if funcionesMenuVacunas[opcion - 1] in globals():
        if callable(globals()[funcionesMenuVacunas[opcion - 1]]):
            globals()[funcionesMenuVacunas[opcion - 1]]()


# endregion

# region Carga de datos -- done
def cargarDatos():
    cargarClinicas()
    cargarVeterinarios()
    cargarPropietarios()
    cargarGatos()
    cargarPerros()
    cargarAdopciones()
    cargarColaboradores()
    cargarVetCol()
    cargarTrabajos()
    cargarVacunas()


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

            globals()["veterinarios"].append(
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
            haTenidoMascota = libro.getElementsByTagName("haTenidoMascota")[contador]
            conocAdiestramiento = libro.getElementsByTagName("conocAdiestramiento")[contador]

            globals()["propietarios"].append(
                Propietario(dni.firstChild.data, direccion.firstChild.data, telefono.firstChild.data,
                            email.firstChild.data, intereses.firstChild.data, haTenidoMascota.firstChild.data,
                            conocAdiestramiento.firstChild.data))


def cargarGatos():
    docGatos = minidom.parse('listas/listaGatos.xml')
    if len(docGatos.getElementsByTagName("gato")) > 0:
        contador = 0
        for libro in docGatos.getElementsByTagName("gato"):
            nombre = libro.getElementsByTagName("nombre")[contador]
            fecNacimiento = libro.getElementsByTagName("fecNacimiento")[contador]
            fecRegistro = libro.getElementsByTagName("fecRegistro")[contador]
            disponible = libro.getElementsByTagName("disponible")[contador]
            pelaje = libro.getElementsByTagName("pelaje")[contador]
            sociable = libro.getElementsByTagName("sociable")[contador]
            codigo = libro.getElementsByTagName("codigo")[contador]

            globals()["gatos"].append(
                Gato(nombre.firstChild.data, fecNacimiento.firstChild.data, fecRegistro.firstChild.data,
                     disponible.firstChild.data, pelaje.firstChild.data, sociable.firstChild.data,
                     codigo.firstChild.data))


def cargarPerros():
    docGatos = minidom.parse('listas/listaPerros.xml')
    if len(docGatos.getElementsByTagName("perro")) > 0:
        contador = 0
        for libro in docGatos.getElementsByTagName("perro"):
            nombre = libro.getElementsByTagName("nombre")[contador]
            fecNacimiento = libro.getElementsByTagName("fecNacimiento")[contador]
            fecRegistro = libro.getElementsByTagName("fecRegistro")[contador]
            disponible = libro.getElementsByTagName("disponible")[contador]
            raza = libro.getElementsByTagName("raza")[contador]
            habilidades = libro.getElementsByTagName("habilidades")[contador]
            codigo = libro.getElementsByTagName("codigo")[contador]

            globals()["perros"].append(
                Gato(nombre.firstChild.data, fecNacimiento.firstChild.data, fecRegistro.firstChild.data,
                     disponible.firstChild.data, raza.firstChild.data, habilidades.firstChild.data,
                     codigo.firstChild.data))


def cargarAdopciones():
    docAdopciones = minidom.parse('listas/listaAdopciones.xml')
    if len(docAdopciones.getElementsByTagName("adopcion")) > 0:
        contador = 0
        for libro in docAdopciones.getElementsByTagName("adopcion"):
            mascota = libro.getElementsByTagName("mascota")[contador]
            propietario = libro.getElementsByTagName("propietario")[contador]
            fecha = libro.getElementsByTagName("fecha")[contador]

            globals()["adopciones"].append(
                Adopcion(mascota.firstChild.data, propietario.firstChild.data, fecha.firstChild.data))


def cargarColaboradores():
    docClinicas = minidom.parse('listas/listaColaboradores.xml')
    if len(docClinicas.getElementsByTagName("colaborador")) > 0:
        contador = 0
        for libro in docClinicas.getElementsByTagName("colaborador"):
            dni = libro.getElementsByTagName("dni")[contador]
            direccion = libro.getElementsByTagName("direccion")[contador]
            telefono = libro.getElementsByTagName("telefono")[contador]
            email = libro.getElementsByTagName("email")[contador]
            intereses = libro.getElementsByTagName("intereses")[contador]
            habilidades = libro.getElementsByTagName("habilidades")[contador]
            poblacion = libro.getElementsByTagName("poblacion")[contador]
            disposicion = libro.getElementsByTagName("disposicion")[contador]
            codigo = libro.getElementsByTagName("codigo")[contador]

            globals()["colaboradores"].append(
                Colaborador(dni.firstChild.data, direccion.firstChild.data, telefono.firstChild.data,
                            email.firstChild.data, intereses.firstChild.data, habilidades.firstChild.data,
                            poblacion.firstChild.data, disposicion.firstChild.data, codigo.firstChild.data))


def cargarVetCol():
    docClinicas = minidom.parse('listas/listaVeterinariosCol.xml')
    if len(docClinicas.getElementsByTagName("veterinarioCol")) > 0:
        contador = 0
        for libro in docClinicas.getElementsByTagName("veterinarioCol"):
            dni = libro.getElementsByTagName("dni")[contador]
            direccion = libro.getElementsByTagName("direccion")[contador]
            telefono = libro.getElementsByTagName("telefono")[contador]
            email = libro.getElementsByTagName("email")[contador]
            intereses = libro.getElementsByTagName("intereses")[contador]
            habilidades = libro.getElementsByTagName("habilidades")[contador]
            colegiado = libro.getElementsByTagName("colegiado")[contador]
            codigo = libro.getElementsByTagName("codigo")[contador]

            globals()["veterinariosCol"].append(
                VeterinarioCol(dni.firstChild.data, direccion.firstChild.data, telefono.firstChild.data,
                               email.firstChild.data, intereses.firstChild.data, habilidades.firstChild.data,
                               colegiado.firstChild.data, codigo.firstChild.data))


def cargarTrabajos():
    docAdopciones = minidom.parse('listas/listaTrabajos.xml')
    if len(docAdopciones.getElementsByTagName("trabajo")) > 0:
        contador = 0
        for libro in docAdopciones.getElementsByTagName("adopcion"):
            codigo = libro.getElementsByTagName("codigo")[contador]
            descripcion = libro.getElementsByTagName("descripcion")[contador]
            mascota = libro.getElementsByTagName("mascota")[contador]

            globals()["trabajos"].append(
                Trabajo(codigo.firstChild.data, descripcion.firstChild.data, mascota.firstChild.data))


def cargarVacunas():
    docAdopciones = minidom.parse('listas/listaVacunas.xml')
    if len(docAdopciones.getElementsByTagName("vacuna")) > 0:
        contador = 0
        for libro in docAdopciones.getElementsByTagName("vacuna"):
            veterinario = libro.getElementsByTagName("veterinario")[contador]
            mascota = libro.getElementsByTagName("mascota")[contador]
            nombre = libro.getElementsByTagName("nombre")[contador]
            fecha = libro.getElementsByTagName("fecha")[contador]

            globals()["vacunas"].append(
                Vacuna(veterinario.firstChild.data, mascota.firstChild.data, nombre.firstChild.data,
                       fecha.firstChild.data))


# endregion done

# region Guardado de Datos -- done
def guardarClinicas():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaClinicas", None)
    docRoot = miXML.documentElement
    for clinica in globals()["clinicas"]:
        nodo = miXML.createElement("clinica")
        elemento = miXML.createElement("direccion")
        elemento.appendChild(miXML.createTextNode(clinica.direccion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("telefono")
        elemento.appendChild(miXML.createTextNode(clinica.telefono))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("email")
        elemento.appendChild(miXML.createTextNode(clinica.email))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("titular")
        elemento.appendChild(miXML.createTextNode(clinica.titular))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("codigo")
        elemento.appendChild(miXML.createTextNode(clinica.codigo))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaClinicas.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarVeterinarios():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaVeterinarios", None)
    docRoot = miXML.documentElement
    for clinica in globals()["veterinarios"]:
        nodo = miXML.createElement("veterinario")
        elemento = miXML.createElement("dni")
        elemento.appendChild(miXML.createTextNode(clinica.dni))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("direccion")
        elemento.appendChild(miXML.createTextNode(clinica.direccion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("telefono")
        elemento.appendChild(miXML.createTextNode(clinica.telefono))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("email")
        elemento.appendChild(miXML.createTextNode(clinica.email))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("intereses")
        elemento.appendChild(miXML.createTextNode(clinica.intereses))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("colegiado")
        elemento.appendChild(miXML.createTextNode(clinica.colegiado))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("especialidad")
        elemento.appendChild(miXML.createTextNode(clinica.especialidad))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("clinica")
        elemento.appendChild(miXML.createTextNode(clinica.clinica))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaVeterinarios.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarPropietarios():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaPropietarios", None)
    docRoot = miXML.documentElement
    for clinica in globals()["propietarios"]:
        nodo = miXML.createElement("propietario")
        elemento = miXML.createElement("dni")
        elemento.appendChild(miXML.createTextNode(clinica.dni))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("direccion")
        elemento.appendChild(miXML.createTextNode(clinica.direccion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("telefono")
        elemento.appendChild(miXML.createTextNode(clinica.telefono))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("email")
        elemento.appendChild(miXML.createTextNode(clinica.email))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("intereses")
        elemento.appendChild(miXML.createTextNode(clinica.intereses))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("haTenidoMascota")
        elemento.appendChild(miXML.createTextNode(str(clinica.haTenidoMascota)))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("conocAdiestramiento")
        elemento.appendChild(miXML.createTextNode(str(clinica.conocAdiestramiento)))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaPropietarios.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarPerros():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaPerros", None)
    docRoot = miXML.documentElement
    for clinica in globals()["perros"]:
        nodo = miXML.createElement("perro")
        elemento = miXML.createElement("nombre")
        elemento.appendChild(miXML.createTextNode(clinica.nombre))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("fecNacimiento")
        elemento.appendChild(miXML.createTextNode(clinica.fecNacimiento))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("disponible")
        elemento.appendChild(miXML.createTextNode(str(clinica.disponible)))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("raza")
        elemento.appendChild(miXML.createTextNode(clinica.raza))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("habilidades")
        elemento.appendChild(miXML.createTextNode(clinica.habilidades))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("codigo")
        elemento.appendChild(miXML.createTextNode(clinica.codigo))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaPerros.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarGatos():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaGatos", None)
    docRoot = miXML.documentElement
    for clinica in globals()["gatos"]:
        nodo = miXML.createElement("gato")
        elemento = miXML.createElement("nombre")
        elemento.appendChild(miXML.createTextNode(clinica.nombre))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("fecNacimiento")
        elemento.appendChild(miXML.createTextNode(clinica.fecNacimiento))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("fecRegistro")
        elemento.appendChild(miXML.createTextNode(str(clinica.fecRegistro)))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("disponible")
        elemento.appendChild(miXML.createTextNode(str(clinica.disponible)))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("pelaje")
        elemento.appendChild(miXML.createTextNode(clinica.pelaje))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("sociable")
        elemento.appendChild(miXML.createTextNode(str(clinica.sociable)))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("codigo")
        elemento.appendChild(miXML.createTextNode(clinica.codigo))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaGatos.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarAdopciones():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaAdopciones", None)
    docRoot = miXML.documentElement
    for clinica in globals()["adopciones"]:
        nodo = miXML.createElement("adopcion")
        elemento = miXML.createElement("mascota")
        elemento.appendChild(miXML.createTextNode(clinica.mascota))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("propietario")
        elemento.appendChild(miXML.createTextNode(clinica.propietario))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("fecha")
        elemento.appendChild(miXML.createTextNode(clinica.fecha))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaAdopciones.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarColaboradores():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaColaboradores", None)
    docRoot = miXML.documentElement
    for clinica in globals()["colaboradores"]:
        nodo = miXML.createElement("colaborador")
        elemento = miXML.createElement("dni")
        elemento.appendChild(miXML.createTextNode(clinica.dni))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("direccion")
        elemento.appendChild(miXML.createTextNode(clinica.direccion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("telefono")
        elemento.appendChild(miXML.createTextNode(clinica.telefono))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("email")
        elemento.appendChild(miXML.createTextNode(clinica.email))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("intereses")
        elemento.appendChild(miXML.createTextNode(clinica.intereses))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("habilidades")
        elemento.appendChild(miXML.createTextNode(clinica.habilidades))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("poblacion")
        elemento.appendChild(miXML.createTextNode(clinica.poblacion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("disposicion")
        elemento.appendChild(miXML.createTextNode(clinica.disposicion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("codigo")
        elemento.appendChild(miXML.createTextNode(clinica.codigo))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaColaboradores.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarVeterinariosCol():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaVeterinariosCol", None)
    docRoot = miXML.documentElement
    for clinica in globals()["veterinariosCol"]:
        nodo = miXML.createElement("veterinarioCol")
        elemento = miXML.createElement("dni")
        elemento.appendChild(miXML.createTextNode(clinica.dni))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("direccion")
        elemento.appendChild(miXML.createTextNode(clinica.direccion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("telefono")
        elemento.appendChild(miXML.createTextNode(clinica.telefono))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("email")
        elemento.appendChild(miXML.createTextNode(clinica.email))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("intereses")
        elemento.appendChild(miXML.createTextNode(clinica.intereses))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("habilidades")
        elemento.appendChild(miXML.createTextNode(clinica.habilidades))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("colegiado")
        elemento.appendChild(miXML.createTextNode(clinica.colegiado))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("codigo")
        elemento.appendChild(miXML.createTextNode(clinica.codigo))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaVeterinariosCol.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarVacunas():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaVacunas", None)
    docRoot = miXML.documentElement
    for clinica in globals()["vacunas"]:
        nodo = miXML.createElement("vacuna")
        elemento = miXML.createElement("veterinario")
        elemento.appendChild(miXML.createTextNode(clinica.veterinario))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("mascota")
        elemento.appendChild(miXML.createTextNode(clinica.mascota))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("nombre")
        elemento.appendChild(miXML.createTextNode(clinica.nombre))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("fecha")
        elemento.appendChild(miXML.createTextNode(str(clinica.fecha)))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaVacunas.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


def guardarTrabajos():
    miDOM = minidom.getDOMImplementation()
    miXML = miDOM.createDocument(None, "listaTrabajos", None)
    docRoot = miXML.documentElement
    for clinica in globals()["trabajos"]:
        nodo = miXML.createElement("trabajo")
        elemento = miXML.createElement("codigo")
        elemento.appendChild(miXML.createTextNode(clinica.codigo))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("descripcion")
        elemento.appendChild(miXML.createTextNode(clinica.descripcion))
        nodo.appendChild(elemento)
        elemento = miXML.createElement("mascota")
        elemento.appendChild(miXML.createTextNode(clinica.mascota))
        nodo.appendChild(elemento)
        docRoot.appendChild(nodo)

    pf = open("listas/listaTrabajos.xml", 'w')
    pf.write(miXML.toprettyxml())
    pf.close()


# endregion

# region Listado de datos -- done
def listarClinicas(menu):
    contador = 0
    if len(globals()["clinicas"]) > 0:
        for clinica in globals()["clinicas"]:
            contador += 1
            print("{} -> Código: {} \t Direccion: {} \t Telefono: {} \t Email: {} \t Titular: {}".format(contador,
                                                                                                         clinica.codigo,
                                                                                                         clinica.direccion,
                                                                                                         clinica.telefono,
                                                                                                         clinica.email,
                                                                                                         clinica.titular))
    else:
        print("No hay clinicas registrados")
    if menu is not None:
        globals()[menu]()


def listarVeterinarios(menu):
    contador = 0
    if len(globals()["veterinarios"]) > 0:
        for veterinario in globals()["veterinarios"]:
            contador += 1
            print("{} -> DNI: {} \t Dirección: {} \t Colegiado: {} \t Especialidad: {} \t Clinica: {}".format(contador,
                                                                                                              veterinario.dni,
                                                                                                              veterinario.direccion,
                                                                                                              veterinario.colegiado,
                                                                                                              veterinario.especialidad,
                                                                                                              veterinario.clinica))
    else:
        print("No hay veterinarios registrados")
    if menu is not None:
        globals()[menu]()


def listarPropietarios(menu):
    contador = 0
    if len(globals()["propietarios"]) > 0:
        for propietario in globals()["propietarios"]:
            contador += 1
            print(
                "{} -> DNI: {} \t Dirección: {} \t Telefono: {} \t Email: {} \t Ha tenido Mascota: {} \t Cono. Adiest: {}".format(
                    contador,
                    propietario.dni, propietario.direccion, propietario.telefono, propietario.email,
                    propietario.haTenidoMascota, propietario.conocAdiestramiento))
    else:
        print("No hay propietarios registrados")
    if menu is not None:
        globals()[menu]()


def listarGatos(menu):
    contador = 0
    if len(globals()["gatos"]) > 0:
        for gato in globals()["gatos"]:
            contador += 1
            print(
                "{} -> Código: {} \t Nombre: {} \t Nacimiento: {} \t Registro: {} \t Disponible: {} Tiempo en el refugio: {}".format(
                    contador, gato.codigo, gato.nombre, gato.fecNacimiento, gato.fecRegistro, gato.disponible,
                    obtenerTiempoEnRefugio(gato.codigo)
                ))
    else:
        print("No hay gatos registrados")
    if menu is not None:
        globals()[menu]()


def listarPerros(menu):
    contador = 0
    if len(globals()["perros"]) > 0:
        for perro in globals()["perro"]:
            contador += 1
            print(
                "{} -> Código: {} \t Nombre: {} \t Nacimiento: {} \t Registro: {} \t Disponible: {}".format(
                    contador, perro.codigo, perro.nombre, perro.fecNacimiento, perro.fecRegistro, perro.disponible))
    else:
        print("No hay perros registrados")
    if menu is not None:
        globals()[menu]()


def listarAdopciones(menu):
    contador = 0
    if len(globals()["adopciones"]) > 0:
        for adopcion in globals()["adopciones"]:
            contador += 1
            print(
                "{} -> Mascota: {} \t Propietario: {} \t Fecha: {}".format(contador, adopcion.mascota,
                                                                           adopcion.propietario, adopcion.fecha))
    else:
        print("No hay perros registrados")
    if menu is not None:
        globals()[menu]()


def listarColaboradores(menu):
    contador = 0
    if len(globals()["colaboradores"]) > 0:
        for veterinario in globals()["colaboradores"]:
            contador += 1
            print(
                "{} -> Código: {} \t DNI: {} \t Dirección: {} \t Habilidades: {} \t Disposición: {} ".format(
                    contador,
                    veterinario.codigo,
                    veterinario.dni,
                    veterinario.direccion,
                    veterinario.habilidades,
                    veterinario.disposicion))
    else:
        print("No hay colaboradores registrados")
    if menu is not None:
        globals()[menu]()


def listarVeterinariosCol(menu):
    contador = 0
    if len(globals()["veterinariosCol"]) > 0:
        for veterinario in globals()["veterinariosCol"]:
            contador += 1
            print(
                "{} -> Código: {} \t DNI: {} \t Dirección: {} \t Habilidades: {} \t Colegiado: {} ".format(
                    contador,
                    veterinario.codigo,
                    veterinario.dni,
                    veterinario.direccion,
                    veterinario.habilidades,
                    veterinario.colegiado))
    else:
        print("No hay veterinarios col. registrados")
    if menu is not None:
        globals()[menu]()


def listarTrabajos():
    try:
        eleccion = int(
            input("¿De qué desea consultar los trabajos?\n\t1.- Colaboradores\n\t2.- Veterinarios Colaboradores"))
    except ValueError:
        print("Debe introducir 1 o 2")
        eleccion = 3
    if eleccion == 1:
        listarTrabajosColaboradoresHTML()
    elif eleccion == 2:
        listarTrabajosVeterinariosHTML()
    else:
        print("Debe introducir un valor válido")
    globals()["menuTrabajos"]()


def listarVacunas():
    try:
        eleccion = int(
            input("¿De qué desea ver las vacuna?\n\t1.- Gato\n\t2.- Perro"))
    except ValueError:
        print("Debe introducir 1 o 2")
    if eleccion == 1:
        listarGatos(None)
        if len(globals()["gatos"]) > 0:
            try:
                eleccion2 = int(input("¿De qué gato desea ver las vacunas?"))
                if 0 > eleccion > len(globals()["gatos"]):
                    print("No existe ese gato")
                else:
                    listarVacunasHTML(globals()["gatos"][eleccion - 1])
            except ValueError:
                print("Debe introducir un número")
    elif eleccion == 2:
        listarPerros(None)
        if len(globals()["perros"]) > 0:
            try:
                eleccion2 = int(input("¿De qué perro desea ver las vacunas?"))
                if 0 > eleccion > len(globals()["perros"]):
                    print("No existe ese perro")
                else:
                    listarVacunasHTML(globals()["perros"][eleccion - 1])
            except ValueError:
                print("Debe introducir un número")
    globals()["menuVacunas"]()


# endregion

# region Agregación de datos -- done
def agregarClinica():
    direccion = input("Introduzca la direccion: ")
    telefono = input("Introduzca el telefono: ")
    email = input("Introduzca el email: ")
    titular = input("Introduzca el titular: ")

    globals()["clinicas"].append(Clinica(direccion, telefono, email, titular, None))
    globals()["guardarClinicas"]()
    globals()["menuClinicas"]()


def agregarPropietario():
    valido = False
    valido2 = False
    dni = input("Introduzca el dni: ")
    direccion = input("Introduzca la direccion: ")
    telefono = input("Introduzca el telefono: ")
    email = input("Introduzca el email: ")
    intereses = input("Introduzca los intereses: ")
    while not valido:
        try:
            mascota = int(input("¿Ha tenido mascota?\n\t1.- Sí\n\t2.- No"))
        except ValueError:
            print("Debe introducir un número")
        if mascota == 1 or mascota == 2:
            valido = True
    if mascota == 1:
        haTenidoMascota = True
    else:
        haTenidoMascota = False

    while not valido2:
        try:
            adiestramiento = int(input("¿Tiene conocimientos de adiestramiento?\n\t1.- Sí\n\t2.- No"))
        except ValueError:
            print("Debe introducir un número")
        if adiestramiento == 1 or adiestramiento == 2:
            valido2 = True
    if adiestramiento == 1:
        haTenidoAdiestramiento = True
    else:
        haTenidoAdiestramiento = False

    globals()["propietarios"].append(
        Propietario(dni, direccion, telefono, email, intereses, haTenidoMascota, haTenidoAdiestramiento))
    globals()["guardarPropietarios"]()
    globals()["menuPropietarios"]()


def agregarVeterinario():
    valido = False
    dni = input("Introduzca el dni: ")
    direccion = input("Introduzca la direccion: ")
    telefono = input("Introduzca el telefono: ")
    email = input("Introduzca el email: ")
    intereses = input("Introduzca los intereses: ")
    colegiado = input("Introduzca el numero de colegiado: ")
    especialidad = input("Introduzca la especialidad: ")

    while not valido:
        try:
            clinica = int(input("¿Procede de una clínica?\n\t1.- Sí\n\t2.- No"))
            if clinica == 1 or clinica == 2:
                valido = True
        except ValueError:
            print("Debe introducir un número")

    if clinica == 1:
        codClinica = obtenerCodClinicaParaVet()
    else:
        codClinica = "Voluntario"

    globals()["veterinarios"].append(
        Veterinario(dni, direccion, telefono, email, intereses, colegiado, especialidad, codClinica))
    globals()["guardarVeterinarios"]()
    globals()["menuVeterinarios"]()


def agregarPerro():
    nombre = input("Introduce el nombre: ")
    fecNacimiento = input("Introduce la fecha de nacimiento: ")
    fecRegistro = datetime.now()
    disponible = True
    raza = input("Introduce la raza: ")
    habilidades = input("Introduce las habilidades: ")

    globals()["perros"].append(Perro(nombre, fecNacimiento, fecRegistro, disponible, raza, habilidades))
    globals()["guardarPerros"]()
    globals()["menuPerros"]()


def agregarGato():
    valido = False
    nombre = input("Introduce el nombre: ")
    fecNacimiento = input("Introduce la fecha de nacimiento: ")
    fecRegistro = datetime.now()
    disponible = True
    pelaje = input("Introduce el tipo de pelaje: ")

    while not valido:
        try:
            sociable = int(input("¿Es sociable?\n\t1.- Sí\n\t2.- No"))
        except ValueError:
            print("Debe introducir un número")
        if sociable == 1 or sociable == 2:
            valido = True
        else:
            print("Numero fuera de rango")
    if sociable == 1:
        isSociable = True
    else:
        isSociable = False

    globals()["gatos"].append(Gato(nombre, fecNacimiento, fecRegistro, disponible, pelaje, isSociable))
    globals()["guardarGatos"]()
    globals()["menuGatos"]()


def agregarAdopcion():
    valido = False
    valido2 = False
    valido3 = False
    opcion = -1

    while not valido or 0 > opcion > 2:
        try:
            opcion = int(input("¿De qué desea hacer la adopción?\n\t1.- Gato\n\t2.- Perro"))
            valido = True
        except ValueError:
            print("Debe introducir un numero valido")
        if 0 > opcion > 2:
            print("Numero no valido")

    if opcion == 1:
        if len(globals()["gatos"]) > 0:
            listarGatos(None)
            while not valido2:
                try:
                    gato = int(input("¿De qué gato desea hacer la adopción?"))
                except ValueError:
                    print("Debe introducir un numero valido")
                if 0 > gato > len(globals()["gatos"]):
                    print("Debe introducir un numero valido")
                else:
                    valido2 = True
                    if globals()["gatos"][gato - 1].disponible:
                        if len(globals()["propietarios"]) > 0:
                            listarPropietarios(None)
                            while not valido3:
                                try:
                                    propietario = int(input("¿Qué propietario?"))
                                except ValueError:
                                    print("Debe introducir un numero")
                                if 0 > propietario > len(globals()["propietarios"]):
                                    print("Debe introducir un numero valido")
                                else:
                                    valido3 = True
                                    if puedeAdoptar(globals()["propietarios"][propietario - 1]):
                                        globals()["adopciones"].append(Adopcion(globals()["gatos"][gato - 1].codigo,
                                                                                globals()["propietarios"][
                                                                                    propietario - 1].dni,
                                                                                str(datetime.now())))
                                        globals()["gatos"][gato - 1].disponible = False
                                        print("Adopcion realizada correctamente")
                                        globals()["guardarAdopciones"]()
                                        globals()["menuAdopciones"]()
                                    else:
                                        print("Este propietario ya tiene 5 adopciones")
                        else:
                            print("No hay propietarios para hacer la adopción")

                    else:
                        print("Gato no disponible")
        else:
            print("No hay gatos que adoptar")
    else:
        if len(globals()["perros"]) > 0:
            listarPerros(None)
            while not valido2:
                try:
                    perro = int(input("¿De qué perro desea hacer la adopción?"))
                except ValueError:
                    print("Debe introducir un numero valido")
                if 0 > perro > len(globals()["perros"]):
                    print("Debe introducir un numero valido")
                else:
                    valido = True
                    if globals()["perros"][perro - 1].disponible:
                        if len(globals()["propietarios"]) > 0:
                            listarPropietarios(None)
                            while not valido3:
                                try:
                                    propietario = int(input("¿Qué propietario?"))
                                except ValueError:
                                    print("Debe introducir un numero")
                                if 0 > propietario > len(globals()["propietarios"]):
                                    print("Debe introducir un numero valido")
                                else:
                                    valido3 = True
                                    if puedeAdoptar(globals()["propietarios"][propietario - 1]):
                                        globals()["adopciones"].append(
                                            Adopcion(globals()["perros"][perro - 1].codigo,
                                                     globals()["propietarios"][
                                                         propietario - 1].dni,
                                                     str(datetime.now())))
                                        globals()["perros"][perro - 1].disponible = False
                                        print("Adopcion realizada correctamente")
                                        globals()["guardarAdopciones"]()
                                        globals()["menuAdopciones"]()
                                    else:
                                        print("Este propietario ya tiene 5 adopciones")
                        else:
                            print("No hay propietarios para hacer la adopción")

                    else:
                        print("Perro no disponible")
        else:
            print("No hay perros que adoptar")


def agregarColaborador():
    dni = input("Introduzca el dni: ")
    direccion = input("Introduzca la direccion: ")
    telefono = input("Introduzca el telefono: ")
    email = input("Introduzca el email: ")
    intereses = input("Introduzca los intereses: ")
    habilidades = input("Introduzca las habilidades: ")
    poblacion = input("Introduzca la poblacion: ")
    disponibilidad = input("Introduzca la disponibilidad: ")

    globals()["colaboradores"].append(
        Colaborador(dni, direccion, telefono, email, intereses, habilidades, poblacion, disponibilidad, None))
    globals()["guardarColaboradores"]()
    globals()["menuColaboradores"]()


def agregarVeterinarioCol():
    dni = input("Introduzca el dni: ")
    direccion = input("Introduzca la direccion: ")
    telefono = input("Introduzca el telefono: ")
    email = input("Introduzca el email: ")
    intereses = input("Introduzca los intereses: ")
    habilidades = input("Introduzca las habilidades: ")
    colegiado = input("Introduzca el numero de colegiado: ")

    globals()["veterinariosCol"].append(
        VeterinarioCol(dni, direccion, telefono, email, intereses, habilidades, colegiado, None))
    globals()["guardarVeterinariosCol"]()
    globals()["menuVetCol"]()


def agregarTrabajoFinal(codigo, descripcion, mascota):
    globals()["trabajos"].append(Trabajo(codigo, descripcion, mascota))
    globals()["guardarTrabajos"]()


def agregarTrabajo():
    try:
        eleccion = int(input("¿A qué desea agregarle un trabajo?\n\t1.- Colaborador\t\n2.- Veterinario Col"))
    except ValueError:
        print("Debe introducir un numero")
    if 1 > eleccion > 2:
        print("Numero no valido")
    else:
        if eleccion == 1:
            listarColaboradores(None)
            if len(globals()["colaboradores"]) > 0:
                try:
                    eleccion2 = int(input("A que colaborador desea asignarle el trabajo"))
                except ValueError:
                    print("Debe introducir un numero")
                    eleccion2 = -1
                if 0 > eleccion2 > len(globals()["colaboradores"]):
                    print("No existe ese colaborador")
                else:
                    codigo = globals()["colaboradores"][eleccion2 - 1].codigo
                    descripcion = input("Introduzca la descripción del trabajo: ")
                    try:
                        eleccion3 = int(input("¿Tiene que ver con una mascota?\n\t1.- Si\n\t2.- No"))
                        if eleccion3 == 2:
                            mascota = "-"
                            agregarTrabajoFinal(codigo, descripcion, mascota)
                        elif eleccion3 == 1:
                            eleccion4 = int(input("1.- Gato\n2.- Perro"))
                            if 0 > eleccion4 > 2:
                                print("Numero invalido")
                            else:
                                if eleccion4 == 1:
                                    listarGatos(None)
                                    if len(globals()["gatos"]) > 0:
                                        eleccion5 = int(input("A que gato?"))
                                        if 0 > eleccion5 > len(globals()["gatos"]):
                                            print("numero invalido")
                                        else:
                                            mascota = globals()["gatos"][eleccion5 - 1].codigo
                                            agregarTrabajoFinal(codigo, descripcion, mascota)
                                else:
                                    listarPerros(None)
                                    if len(globals()["perros"]) > 0:
                                        eleccion5 = int(input("A que perro?"))
                                        if 0 > eleccion5 > len(globals()["perros"]):
                                            print("numero invalido")
                                        else:
                                            mascota = globals()["perros"][eleccion5 - 1].codigo
                                            agregarTrabajoFinal(codigo, descripcion, mascota)
                        else:
                            print("Numero invalido")
                    except ValueError:
                        print("Debe introducir un numero")
        else:
            listarVeterinariosCol(None)
            if len(globals()["veterinariosCol"]) > 0:
                try:
                    eleccion2 = int(input("A que veterinario desea asignarle el trabajo"))
                except ValueError:
                    print("Debe introducir un numero")
                    eleccion2 = -1
                if 0 > eleccion2 > len(globals()["veterinariosCol"]):
                    print("No existe ese veterinario")
                else:
                    codigo = globals()["veterinariosCol"][eleccion2 - 1].codigo
                    descripcion = input("Introduzca la descripción del trabajo: ")
                    try:
                        eleccion4 = int(input("1.- Gato\n2.- Perro"))
                        if 0 > eleccion4 > 2:
                            print("Numero invalido")
                        else:
                            if eleccion4 == 1:
                                listarGatos(None)
                                if len(globals()["gatos"]) > 0:
                                    eleccion5 = int(input("A que gato?"))
                                    if 0 > eleccion5 > len(globals()["gatos"]):
                                        print("numero invalido")
                                    else:
                                        mascota = globals()["gatos"][eleccion5 - 1].codigo
                                        agregarTrabajoFinal(codigo, descripcion, mascota)
                            else:
                                listarPerros(None)
                                if len(globals()["perros"]) > 0:
                                    eleccion5 = int(input("A que perro?"))
                                    if 0 > eleccion5 > len(globals()["perros"]):
                                        print("numero invalido")
                                    else:
                                        mascota = globals()["perros"][eleccion5 - 1].codigo
                                        agregarTrabajoFinal(codigo, descripcion, mascota)
                    except ValueError:
                        print("Debe introducir un numero")

    globals()["menuTrabajos"]()


def agregarVacunaFinal(veterinario, nombre, mascota, fecha):
    globals()["vacunas"].append(Vacuna(veterinario, mascota, nombre, fecha))
    globals()["guardarVacunas"]()


def agregarVacuna():
    try:
        listarVeterinariosCol(None)
        if len(globals()["veterinariosCol"]) > 0:
            veterinario = int(input("A que veterinario desesa asignarle la vacuna?"))
            eleccion2 = int(input("1.- A un gato\n2.- A un perro"))
            if 1 > eleccion2 > 2:
                print("Numero invalido")
            else:
                if eleccion2 == 1:
                    listarGatos(None)
                    if len(globals()["gatos"]) > 0:
                        eleccion3 = int(input("A que gato?"))
                        if 1 > eleccion3 > len(globals()["gatos"]):
                            print("Numero invalido")
                        else:
                            mascota = globals()["gatos"][eleccion3 - 1].codigo
                            nombre = input("Introduce el nombre de la vacuna: ")
                            fecha = datetime.now()
                            agregarVacunaFinal(globals()["veterinariosCol"][veterinario-1].codigo, nombre, mascota, fecha)
                else:
                    listarPerros(None)
                    if len(globals()["perros"]) > 0:
                        eleccion3 = int(input("A que erro?"))
                        if 1 > eleccion3 > len(globals()["perros"]):
                            print("Numero invalido")
                        else:
                            mascota = globals()["perros"][eleccion3 - 1].codigo
                            nombre = input("Introduce el nombre de la vacuna: ")
                            fecha = datetime.now()
                            agregarVacunaFinal(globals["veterinariosCol"][veterinario-1].codigo, nombre, mascota, fecha)
    except ValueError:
        print("Debe introducir un numero")

    globals()["menuVacunas"]()


# endregion

# region Eliminación de datos -- done
def eliminarClinica():
    if tieneRegistros(globals()["clinicas"]):
        listarClinicas(None)
        valido = False

        while not valido:
            try:
                eliminado = int(input("¿Qué clinica desea eliminar? (Para salir introduzca -1): "))
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
                globals()["clinicas"].pop(eliminado - 1)
                print("Eliminado correctamente")
                globals()["guardarClinicas"]()
    else:
        print("No hay Clinicas para eliminar")
    globals()["menuClinicas"]()


def eliminarVeterinario():
    if tieneRegistros(globals()["veterinarios"]):
        listarVeterinarios(None)
        valido = False

        while not valido:
            try:
                eliminado = int(input("¿Qué veterinario desea eliminar? (Para salir introduzca -1): "))
                valido = True
            except ValueError:
                print("Debe introducir un número")
                valido = False

        if 0 > eliminado > len(globals()["veterinarios"]):
            print("Número inválido")
        else:
            if eliminado == -1:
                print("Eliminación cancelada")
            else:
                globals()["veterinarios"].pop(eliminado - 1)
                print("Eliminado correctamente")
                globals()["guardarVeterinarios"]()
    else:
        print("No hay veterinarios para eliminar")
    globals()["menuVeterinarios"]()


def eliminarPropietarios():
    if tieneRegistros(globals()["propietarios"]):
        listarPropietarios(None)
        valido = False

        while not valido:
            try:
                eliminado = int(input("¿Qué propietario desea eliminar? (Para salir introduzca -1): "))
                valido = True
            except ValueError:
                print("Debe introducir un número")
                valido = False

        if 0 > eliminado > len(globals()["propietarios"]):
            print("Número inválido")
        else:
            if eliminado == -1:
                print("Eliminación cancelada")
            else:
                eliminarAdopcionesPorPropietario(globals()["propietarios"][eliminado - 1].dni)
                globals()["propietarios"].pop(eliminado - 1)
                print("Eliminado correctamente")
                globals()["guardarPropietarios"]()
    else:
        print("No hay Clinicas para eliminar")
    globals()["menuPropietarios"]()


def eliminarGato():
    if tieneRegistros(globals()["gatos"]):
        listarGatos(None)
        valido = False

        while not valido:
            try:
                eliminado = int(input("¿Qué gato desea eliminar? (Para salir introduzca -1): "))
                valido = True
            except ValueError:
                print("Debe introducir un número")
                valido = False

        if 0 > eliminado > len(globals()["propietarios"]):
            print("Número inválido")
        else:
            if eliminado == -1:
                print("Eliminación cancelada")
            else:
                eliminarAdopcionesPorMascota(globals()["gatos"][eliminado - 1].codigo)
                globals()["gatos"].pop(eliminado - 1)
                print("Eliminado correctamente")
                globals()["guardarGatos"]()
    else:
        print("No hay gatos para eliminar")
    globals()["menuGatos"]()


def eliminarPerro():
    if tieneRegistros(globals()["perros"]):
        listarPerros(None)
        valido = False

        while not valido:
            try:
                eliminado = int(input("¿Qué perro desea eliminar? (Para salir introduzca -1): "))
                valido = True
            except ValueError:
                print("Debe introducir un número")
                valido = False

        if 0 > eliminado > len(globals()["perros"]):
            print("Número inválido")
        else:
            if eliminado == -1:
                print("Eliminación cancelada")
            else:
                eliminarAdopcionesPorMascota(globals()["perros"][eliminado - 1].codigo)
                globals()["perros"].pop(eliminado - 1)
                print("Eliminado correctamente")
                globals()["guardarPerros"]()
    else:
        print("No hay perros para eliminar")
    globals()["menuPerros"]()


def eliminarColaborador():
    listarColaboradores(None)
    if tieneRegistros(globals()["colaboradores"]):
        try:
            eliminado = int(input("A cual desea eliminar?"))
            if 1 > eliminado > len(globals()["colaboradores"]):
                print("numero invalido")
            else:
                globals["colaboradores"].pop(eliminado - 1)
                globals()["guardarColaboradores"]()
        except ValueError:
            print("Debe introducir un numero")
    globals()["menuColaboradores"]()


def eliminarVeterinarioCol():
    listarVeterinariosCol(None)
    if tieneRegistros(globals()["veterinariosCol"]):
        try:
            eliminado = int(input("A cual desea eliminar?"))
            if 1 > eliminado > len(globals()["veterinariosCol"]):
                print("numero invalido")
            else:
                globals["veterinariosCol"].pop(eliminado - 1)
                globals()["guardarVeterinariosCol"]()
        except ValueError:
            print("Debe introducir un numero")
    globals()["menuVeterinariosCol"]()


# endregion

# region HTML
def mostrarAdopcionesHTML():
    f = open('html/listado.html', 'w')
    contador = 1

    mensaje = "<html><body><h1><b>Adopciones</bZ</h1><table border='1'><th>Numero Adopción</th><th>Mascota</th><th>Propietario</th><th>Fecha adopcion</th>"
    for adopcion in globals()["adopciones"]:
        mensaje += "<tr><td>" + contador + "</td>"
        mensaje += "<td>" + adopcion.mascota + "</td>"
        mensaje += "<td>" + adopcion.propietario + "</td>"
        mensaje += "<td>" + adopcion.fecha + "</td></tr>"

    mensaje += "</table></body></html>"

    f.write(mensaje)
    f.close()

    webbrowser.open_new_tab('html/listado.html')
    globals()["menuHTML"]()


def mostrarClinicasHTML():
    f = open('html/listado.html', 'w')

    mensaje = "<html><body><h1><b>Clinicas</bZ</h1><table border='1'><th>Codigo</th><th>Calle</th><th>Titular</th>"

    for clinica in globals()["clinicas"]:
        mensaje += "<tr><td>" + clinica.codigo + "</td>"
        mensaje += "<td>" + clinica.direccion + "</td>"
        mensaje += "<td>" + clinica.titular + "</td></tr>"
        for veterinario in globals()["veterinarios"]:
            if veterinario.clinica == clinica.codigo:
                mensaje += "<tr>" + veterinario.dni + "</tr>"

    mensaje += "</table></body></html>"

    f.write(mensaje)
    f.close()

    webbrowser.open_new_tab('html/listado.html')
    globals()["menuHTML"]()


def mostrarMascotasHTML():
    f = open('html/listado.html', 'w')

    mensaje = "<html><body><h1><b>Mascotas</bZ</h1><table border='1'><th>Codigo</th><th>Nombre</th><th>Disponible</th>"

    for perro in globals()["perros"]:
        mensaje += "<tr><td>" + perro.codigo + "</td>"
        mensaje += "<td>" + perro.nombre + "</td>"
        mensaje += "<td>" + perro.disponible + "</td></tr>"

    for gato in globals()["gatos"]:
        mensaje += "<tr><td>" + gato.codigo + "</td>"
        mensaje += "<td>" + gato.nombre + "</td>"
        mensaje += "<td>" + gato.disponible + "</td></tr>"

    mensaje += "</table>"

    mensaje = "<h1><b>Propietarios</bZ</h1><table border='1'><th>DNI</th><th>Nombre</th><th>Telefono</th>"

    for propietario in globals()["propietarios"]:
        mensaje += "<tr><td>" + propietario.dni + "</td>"
        mensaje += "<td>" + propietario.nombre + "</td>"
        mensaje += "<td>" + propietario.telefono + "</td></tr>"

    mensaje += "</table></body></html>"

    f.write(mensaje)
    f.close()

    webbrowser.open_new_tab('html/listado.html')
    globals()["menuHTML"]()


def listarVacunasHTML(mascota):
    if mascota.codigo.startswith("GAT"):
        tipo = 1
    else:
        tipo = 2

    f = open('html/listado.html', 'w')

    mensaje = "<html><head><link rel='stylesheet' type='text/css' href= 'css\estilos-vacunas.css' media='screen' />" \
              "</head><body>"

    mensaje += "<h1>Nombre mascota: " + mascota.nombre + "</h1>"

    mensaje += "<div id='datos'><div id='izquierda'><p>Tipo de mascota: " + "Gato" if tipo == 1 else "Perro" + "</p><p>Fecha de nacimiento: " + str(mascota.fecNacimiento) + "</p><p>Fecha de registro: " + str(mascota.fecRegistro) + "</p></div>"

    mensaje += "<div id='derecha'><p>Disponible: " + "Si" if mascota.disponible else "No" + "</p>"

    if tipo == 2:
        mensaje += "<p>Raza: " + mascota.raza + "</p><p>Habilidades: " + mascota.habilidades + "</p></div>"
    else:
        mensaje += "<p>Pelaje: " + mascota.pelaje + "</p><p>Sociable: " + "Si" if mascota.sociable else "No" + "</p></div>"

    mensaje += "</div><table><tr><th>Vacuna</th><th>Fecha</th><th>Veterinario</th><tr>"

    for vacuna in globals()["vacunas"]:
        if vacuna.mascota == mascota.codigo:
            mensaje += "<tr><td>" + vacuna.nombre + "</td><td>" + str(vacuna.fecha) + "</td><td>" + vacuna.veterinario + "</td></tr>"

    mensaje += "</body></html>"

    f.write(mensaje)
    f.close()

    webbrowser.open_new_tab('html/listado.html')
    globals()["menuVacunas"]()


def listarTrabajosColaboradoresHTML():

    f = open('html/listado.html', 'w')

    mensaje = "<html><head><link rel='stylesheet' type='text/css' href= 'css\estilos-colaborador.css' media='screen' />" \
              "</head><body>"

    for colaborador in globals()["colaboradores"]:
        mensaje += "<div id='colaborador'><p>" + colaborador.dni + "</p><div id='trabajos'><table><tr><th>Tarea Realizadas</th><th>Mascota</th></tr>"

        for tarea in globals()["trabajos"]:
            if tarea.codigo == colaborador.codigo:
                mensaje += "<td>" + tarea.descripcion + "</td><td>" + "-" if not tarea.mascota else tarea.mascota + "</td></tr>"

        mensaje += "</table></div></div>"

    mensaje += "</body></html>"

    f.write(mensaje)
    f.close()

    webbrowser.open_new_tab('html/listado.html')
    globals()["menuTrabajos"]()


def listarTrabajosVeterinariosHTML():

    f = open('html/listado.html', 'w')

    mensaje = "<html><head><link rel='stylesheet' type='text/css' href= 'css\estilos-veterinarios.css' media='screen' />" \
              "</head><body>"

    for colaborador in globals()["veterinariosCol"]:
        mensaje += "<div id='veterinario'><p>" + colaborador.dni + "</p><div id='trabajos'><table><tr><th>Tarea Realizadas</th><th>Mascota</th></tr>"

        for tarea in globals()["trabajos"]:
            if tarea.codigo == colaborador.codigo:
                mensaje += "<td>" + tarea.descripcion + "</td><td>" + "-" if not tarea.mascota else tarea.mascota + "/td></tr>"

        mensaje += "</div></div>"

    mensaje += "<table></body></html>"

    f.write(mensaje)
    f.close()

    webbrowser.open_new_tab('html/listado.html')
    globals()["menuTrabajos"]()


# endregion

# region Otras funciones
def obtenerCodClinicaParaVet():
    if len(globals()["clinicas"]) > 0:
        try:
            listarClinicas(None)
            clinica = int(input("¿De qué clínica procede? "))
            if 0 > clinica > len(globals()["clinicas"]):
                print("Clínica errónea, se le asignará Voluntario")
                codClinica = "Voluntario"
            else:
                codClinica = globals()["clinicas"][clinica - 1].codigo
        except ValueError:
            print("Clínica errónea, se le asignará Voluntario")
            codClinica = "Voluntario"
    else:
        print("No hay clínicas, se le asignará voluntario")
        codClinica = "Voluntario"

    return codClinica


def puedeAdoptar(dni):
    puede = False
    contador = 0
    for adopcion in globals()["adopciones"]:
        if adopcion.propietario == dni:
            contador += 1
    if contador < 5:
        puede = True

    return puede


def tieneRegistros(lista):
    if len(lista) > 0:
        valido = True
    else:
        valido = False
    return valido


def eliminarAdopcionesPorPropietario(dni):
    contador = 0
    for adopcion in globals()["adopciones"]:
        if adopcion.propietario == dni:
            codigo = globals()["adopciones"][contador].mascota
            if codigo.startswith("GAT"):
                for gato in globals()["gatos"]:
                    if gato.codigo == codigo:
                        gato.disponible = True
            else:
                for perro in globals()["perros"]:
                    if perro.codigo == codigo:
                        perro.disponible = True
        contador += 1


def eliminarAdopcionesPorMascota(codigo):
    contador = 0
    for adopcion in globals()["adopciones"]:
        if adopcion.codigo == codigo:
            globals()["adopciones"].pop(contador)


def preguntarMenu(verbo, opciones):
    while 1 > globals()["opcion"] or globals()["opcion"] > opciones:
        try:
            globals()["opcion"] = int(input("¿Qué desesa " + verbo + "?"))
        except ValueError:
            globals()["opcion"] = -1
            print("Debe introducir un número.")
        if globals()["opcion"] < 1 or globals()["opcion"] > opciones:
            print("Número inválido.")


def obtenerTiempoEnRefugio(codigo):
    if codigo.startswith("GAT"):
        for gato in globals()["gatos"]:
            if gato.codigo == codigo:
                tiempoGato = datetime.strptime(gato.fecRegistro, "%Y-%m-%d %H:%M:%S.%f")
                tiempo = datetime.now() - tiempoGato
    else:
        for perro in globals()["perros"]:
            if perro.codigo == codigo:
                tiempoPerro = datetime.strptime(perro.fecRegistro, "%Y-%m-%d %H:%M:%S.%f")
                tiempo = datetime.now() - tiempoPerro

    return tiempo


def Salir():
    exit(0)


# endregion

# Main
cargarDatos()
menuPrincipal()
