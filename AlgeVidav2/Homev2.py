from datetime import datetime
from xml.dom import minidom

from AlgeVidav2.clases.Adopcion import Adopcion
from AlgeVidav2.clases.Clinica import Clinica
from AlgeVidav2.clases.Gato import Gato
from AlgeVidav2.clases.Perro import Perro
from AlgeVidav2.clases.Veterinario import Veterinario
from AlgeVidav2.clases.Propietario import Propietario

# region Variables


funcionesMenuPrincipal = (
    "menuClinicas", "menuVeterinarios", "menuPropietarios", "menuMascotas", "menuAdopciones", "menuHTML", "Salir")
funcionesMenuClinicas = ("listarClinicas", "agregarClinica", "eliminarClinica", "menuPrincipal")
funcionesMenuVeterinarios = (
    "listarVeterinarios", "agregarVeterinario", "eliminarVeterinario", "menuPrincipal")
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
    print("/*             6.- HTML                  *\\")
    print("/*             7.- Salir                 *\\")
    print("/*                                       *\\")
    print("/*****************************************\\")

    preguntarMenu("consultar", 8)

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


# endregion

# region Carga de datos -- done
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
                                                                                    propietario - 1].dni, str(datetime.now())))
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
                                        globals()["adopciones"].append(Adopcion(globals()["perros"][perro - 1].codigo,
                                                                                globals()["propietarios"][
                                                                                    propietario - 1].dni, str(datetime.now())))
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
