
##ejemplo 4-Crear un programa que permita Gestionar 
#(Administrar)-peliculas, colocar un menu de opciones 
#para agregar, remover, consultar peliculas..
#Notas:
#1.- Utilizar funciones y mandar llamar desde otro archivo 
#-2.--Utilizar listas para almacenar los nombres de peliculas

def agregar_pelicula(pelicula, lista_peliculas):
    lista_peliculas.append(pelicula)
    print(f'La película "{pelicula}" ha sido agregada correctamente.')

def remover_pelicula(pelicula, lista_peliculas):
    if pelicula in lista_peliculas:
        lista_peliculas.remove(pelicula)
        print(f'La película "{pelicula}" ha sido eliminada correctamente.')
    else:
        print(f'La película "{pelicula}" no se encuentra en la lista.')

def consultar_peliculas(lista_peliculas):
    if lista_peliculas:
        print("Lista de películas:")
        for pelicula in lista_peliculas:
            print(pelicula)
    else:
        print("La lista de películas está vacía.")

def menu():
    lista_peliculas = []

    while True:
        print("\nMenu de opciones:")
        print("1. Agregar película")
        print("2. Remover película")
        print("3. Actualizar películas")
        print("4. Consultar películas")
        print("5. Buscar")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_pelicula = input("Ingrese el nombre de la película a agregar: ")
            agregar_pelicula(nombre_pelicula, lista_peliculas)
        elif opcion == "2":
            nombre_pelicula = input("Ingrese el nombre de la película a remover: ")
            remover_pelicula(nombre_pelicula, lista_peliculas)
        elif opcion == "3":
            Actualizar_peliculas = ("Cual pelicula desea Actualizar")
        elif opcion == "4":
            Actualizar_peliculas(lista_peliculas)
        elif opcion == "5":
            buscar_pelicula = input("Ingrese el nombre de la película a buscar: ")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu()
