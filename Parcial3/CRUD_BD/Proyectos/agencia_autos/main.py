import os
from funciones import *
from autos.auto import *
from clientes.cliente import *
from revisiones.revision import *
from usuarios.usuario import *
import getpass
from datetime import datetime

def borrarPantalla():
    os.system('clear')  # Limpia la pantalla en sistemas Linux/Unix

def esperarTecla():
    input("\nPresione cualquier tecla para continuar...")

def menu_principal():
    while True:
        usuario_correcto = False
        borrarPantalla()
        print(f"..:: BIENVENIDO AL SISTEMA DE GESTION DEL SISTEMA DE AUTOS ::..")
        print(f"1.- LOGIN ")
        print(f"2.- REGISTRO ")
        opcion = input("INGRESE UNA OPCIÓN: ")
        if opcion == "1":
            usuario = int(input("Ingrese su número de usuario: "))
            contrasena = getpass.getpass("Ingrese su contraseña: ")
            inicio_sesion = Usuarios.iniciarSesion(usuario, contrasena)
            if inicio_sesion:
                usuario_correcto = True
                while usuario_correcto:
                    borrarPantalla()
                    print(f"..:: MENÚ GERENTES ::..")
                    print(f"1.- ADMINISTRAR CLIENTES ")
                    print(f"2.- ADMINISTRAR USUARIOS ")
                    print(f"3.- ADMINISTRAR AUTOS ")
                    print(f"4.- ADMINISTRAR REVISIONES")
                    print(f"5.- SALIR")
                    opcion = input("INGRESE UNA OPCIÓN: ")
                    if opcion == "1":
                        administrar_clientes()
                    elif opcion == "2":
                        administrar_usuarios()
                    elif opcion == "3":
                        administrar_autos()
                    elif opcion == "4":
                        administrar_revisiones()
                    elif opcion == "5":
                        print("Cerrando sesión...")
                        esperarTecla()
                        usuario_correcto = False
            else:
                print("Usuario o contraseña incorrectos.")
                esperarTecla()

        elif opcion == "2":
            borrarPantalla()
            print(f"..:: REGISTRO DE USUARIO ::..")
            nif = input("Ingrese su pin: ")
            nombre = input("Ingrese su nombre: ")
            direccion = input("Ingrese su direccion: ")
            ciudad = input("Ingrese su ciudad: ")
            tel = input("Ingrese su teléfono: ")
            contrasena = getpass.getpass("Ingrese su contraseña: ")
            resultado = Clientes(nif, nombre, direccion, ciudad, tel).agregarCliente()
            if resultado:
                print(f"Usuario registrado correctamente.")
            else:
                print(f"Error al registrar el usuario.")
            esperarTecla()
        else:
            print("Opción inválida. Inténtalo de nuevo.")
            esperarTecla()

def administrar_clientes():
    while True:
        borrarPantalla()
        print(f" ADMINISTRAR CLIENTES")
        print(f"1.- Agregar Cliente ")
        print(f"2.- Mostrar Clientes ")
        print(f"3.- Actualizar Cliente ")
        print(f"4.- Eliminar Cliente ")
        print(f"5.- Volver al Menú Principal")
        opcion = input("INGRESE UNA OPCIÓN: ")
        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            actualizar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")
            esperarTecla()

def administrar_usuarios():
    while True:
        borrarPantalla()
        print(f" ADMINISTRAR USUARIOS")
        print(f"1.- Agregar usuario ")
        print(f"2.- Mostrar usuarios ")
        print(f"3.- Actualizar usuario ")
        print(f"4.- Eliminar usuario ")
        print(f"5.- Volver al Menú Principal")
        opcion = input("INGRESE UNA OPCIÓN: ")
        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            actualizar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")
            esperarTecla()

def administrar_autos():
    while True:
        borrarPantalla()
        print(f" ADMINISTRAR AUTOS")
        print(f"1.- Agregar auto ")
        print(f"2.- Mostrar autos ")
        print(f"3.- Actualizar auto ")
        print(f"4.- Eliminar auto ")
        print(f"5.- Volver al Menú Principal")
        opcion = input("INGRESE UNA OPCIÓN: ")
        if opcion == "1":
            agregar_auto()
        elif opcion == "2":
            mostrar_autos()
        elif opcion == "3":
            actualizar_auto()
        elif opcion == "4":
            eliminar_auto()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")
            esperarTecla()

def administrar_revisiones():
    while True:
        borrarPantalla()
        print(f" ADMINISTRAR REVISIONES")
        print(f"1.- Agregar revisión ")
        print(f"2.- Mostrar revisiones ")
        print(f"3.- Actualizar revisión ")
        print(f"4.- Eliminar revisión ")
        print(f"5.- Volver al Menú Principal")
        opcion = input("INGRESE UNA OPCIÓN: ")
        if opcion == "1":
            agregar_revision()
        elif opcion == "2":
            mostrar_revisiones()
        elif opcion == "3":
            actualizar_revision()
        elif opcion == "4":
            eliminar_revision()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")
            esperarTecla()

def agregar_cliente():
    borrarPantalla()
    print(f"Agregar Cliente")
    nif = input("Ingrese el pin: ")
    nombre = input("Ingrese el nombre: ")
    direccion = input("Ingrese la direccion: ")
    ciudad = input("Ingrese la ciudad: ")
    tel = input("Ingrese el teléfono: ")
    cliente = Clientes(nif, nombre, direccion, ciudad, tel)
    resultado = cliente.agregarCliente()
    if resultado:
        print("CLIENTE AGREGADO CORRECTAMENTE")
    else:
        print("Error")
    esperarTecla()

def mostrar_clientes():
    borrarPantalla()
    print(f"Mostrar Clientes")
    clientes = Clientes.mostrarClientes()
    if len(clientes) > 0:
        print(f"Lista de clientes: ")
        for i in clientes:
            print(f"Pin: {i[0]}, Nombre: {i[1]}, direccion: {i[2]}, ciudad: {i[3]}, tel: {i[4]}")
    else:
        print(f"No existen clientes registrados...")
    esperarTecla()

def actualizar_cliente():
    borrarPantalla()
    print(f"Actualizar Cliente")
    nif = input("Ingrese el pin: ")
    nombre = input("Ingrese el nombre: ")
    direccion = input("Ingrese la direccion: ")
    ciudad = input("Ingrese la ciudad: ")
    tel = input("Ingrese el teléfono: ")
    resultado = Clientes.actualizarCliente(nif, nombre, direccion, ciudad, tel)
    if resultado:
        print(f"El cliente con pin {nif} se actualizó correctamente.")
    else:
        print(f"Por favor inténtelo de nuevo más tarde")
    esperarTecla()

def eliminar_cliente():
    borrarPantalla()
    print(f"Eliminar Cliente")
    nif = input(f"Pin del cliente a eliminar: ")
    resultado = Clientes.eliminarCliente(nif)
    if resultado:
        print(f"El cliente con {nif} se eliminó correctamente.")
    else:
        print(f"Por favor inténtelo de nuevo más tarde")
    esperarTecla()

def agregar_usuario():
    borrarPantalla()
    print(f"Agregar usuario")
    usuario = input("Ingrese el usuario: ")
    contrasena = getpass.getpass("Ingrese la contraseña: ")
    nombre = input("Ingrese el nombre: ")
    usuarioo = Usuarios(usuario, contrasena, nombre)
    resultado = usuarioo.agregarUsuario()
    if resultado:
        print("USUARIO AGREGADO CORRECTAMENTE")
    else:
        print("Error")
    esperarTecla()

def mostrar_usuarios():
    borrarPantalla()
    print(f"Mostrar Usuarios")
    usuarios = Usuarios.mostrarUsuarios()
    if len(usuarios) > 0:
        print(f"Lista de usuarios: ")
        for i in usuarios:
            print(f"ID: {i[0]}, Usuario: {i[1]}, contraseña: {i[2]}, nombre: {i[3]}")
    else:
        print(f"No existen usuarios registrados...")
    esperarTecla()

def actualizar_usuario():
    borrarPantalla()
    print(f"Actualizar Usuario")
    id = int(input("Ingrese el id del usuario a actualizar: "))
    usuario = input("Ingrese el usuario: ")
    contrasena = getpass.getpass("Ingrese la contraseña: ")
    nombre = input("Ingrese el nombre: ")
    resultado = Usuarios.actualizarUsuario(id, usuario, contrasena, nombre)
    if resultado:
        print(f"El usuario con ID {id} se actualizó correctamente.")
    else:
        print(f"Por favor inténtelo de nuevo más tarde")
    esperarTecla()

def eliminar_usuario():
    borrarPantalla()
    print(f"Eliminar Usuario")
    id = int(input(f"ID del usuario a eliminar: "))
    resultado = Usuarios.eliminarUsuario(id)
    if resultado:
        print(f"El usuario con ID {id} se eliminó correctamente.")
    else:
        print(f"Por favor inténtelo de nuevo más tarde")
    esperarTecla()

def agregar_auto():
    borrarPantalla()
    print(f"Agregar auto")
    patente = input("Ingrese la patente: ")
    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    color = input("Ingrese el color: ")
    auto = Autos(patente, marca, modelo, color)
    resultado = auto.agregarAuto()
    if resultado:
        print("AUTO AGREGADO CORRECTAMENTE")
    else:
        print("Error")
    esperarTecla()

def mostrar_autos():
    borrarPantalla()
    print(f"Mostrar Autos")
    autos = Autos.mostrarAutos()
    if len(autos) > 0:
        print(f"Lista de autos: ")
        for i in autos:
            print(f"Patente: {i[0]}, Marca: {i[1]}, Modelo: {i[2]}, Color: {i[3]}")
    else:
        print(f"No existen autos registrados...")
    esperarTecla()

def actualizar_auto():
    borrarPantalla()
    print(f"Actualizar Auto")
    patente = input("Ingrese la patente del auto a actualizar: ")
    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    color = input("Ingrese el color: ")
    resultado = Autos.actualizarAuto(patente, marca, modelo, color)
    if resultado:
        print(f"El auto con patente {patente} se actualizó correctamente.")
    else:
        print(f"Por favor inténtelo de nuevo más tarde")
    esperarTecla()

def eliminar_auto():
    borrarPantalla()
    print(f"Eliminar Auto")
    patente = input(f"Patente del auto a eliminar: ")
    resultado = Autos.eliminarAuto(patente)
    if resultado:
        print(f"El auto con patente {patente} se eliminó correctamente.")
    else:
        print(f"Por favor inténtelo de nuevo más tarde")
    esperarTecla()

def agregar_revision():
    borrarPantalla()
    print(f"Agregar revisión")
    id_auto = input("Ingrese el ID del auto: ")
    descripcion = input("Ingrese la descripción: ")
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    revision = Revisiones(id_auto, descripcion, fecha)
    resultado = revision.agregarRevision()
    if resultado:
        print("REVISION AGREGADA CORRECTAMENTE")
    else:
        print("Error")
    esperarTecla()

def mostrar_revisiones():
    borrarPantalla()
    print(f"Mostrar Revisiones")
    revisiones = Revisiones.mostrarRevisiones()
    if len(revisiones) > 0:
        print(f"Lista de revisiones: ")
        for i in revisiones:
            print(f"ID Auto: {i[0]}, Descripción: {i[1]}, Fecha: {i[2]}")
    else:
        print(f"No existen revisiones registradas...")
    esperarTecla()

def actualizar_revision():
    borrarPantalla()
    print(f"Actualizar Revisión")
    id_auto = input("Ingrese el ID del auto: ")
    descripcion = input("Ingrese la nueva descripción: ")
    fecha = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
    resultado = Revisiones.actualizarRevision(id_auto, descripcion, fecha)
    if resultado:
        print(f"La revisión del auto con ID {id_auto} se actualizó correctamente.")
    else:
        print(f"Por favor inténtelo de nuevo más tarde")
    esperarTecla()

def eliminar_revision():
    borrarPantalla()
    print(f"Eliminar Revisión")
    id_auto = input(f"ID del auto para eliminar la revisión: ")
    resultado = Revisiones.eliminarRevision(id_auto)
    if resultado:
        print(f"La revisión del auto con ID {id_auto} se eliminó correctamente.")
    else:
        print(f"Por favor inténtelo de nuevo más tarde")
    esperarTecla()

if __name__ == "__main__":
    menu_principal()
