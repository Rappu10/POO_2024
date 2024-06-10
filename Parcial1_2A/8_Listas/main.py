
##ejemplo 4-Crear un programa que permita Gestionar 
#(Administrar)-peliculas, colocar un menu de opciones 
#para agregar, remover, consultar peliculas..
#Notas:
#1.- Utilizar funciones y mandar llamar desde otro archivo 
#-2.--Utilizar listas para almacenar los nombres de peliculas

from functions import agregar_pelicula, remover_pelicula, consultar_peliculas, actualizar_pelicula, buscar_pelicula

peliculas = []
peliculas_info = {}

def mostrar_menu():
    print("  ..::/Dagopolis\::..")
    print("Menú de opciones:")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Actualizar película")
    print("5. Buscar película")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_pelicula(peliculas, peliculas_info)
        elif opcion == "2":
            remover_pelicula(peliculas, peliculas_info)
        elif opcion == "3":
            consultar_peliculas(peliculas, peliculas_info)
        elif opcion == "4":
            actualizar_pelicula(peliculas, peliculas_info)
        elif opcion == "5":
            buscar_pelicula(peliculas, peliculas_info)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()