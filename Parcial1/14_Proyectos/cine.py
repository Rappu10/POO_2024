def agregar_pelicula(peliculas, peliculas_info):
    nombre = input("Ingrese el nombre de la película: ")
    if nombre in peliculas:
        print("La película ya existe.")
    else:
        año = input("Ingrese el año de estreno: ")
        
        peliculas.append(nombre)
        peliculas_info[nombre] = {
            "año": año,
        }
        print(f"Película '{nombre}' agregada con éxito.")

def remover_pelicula(peliculas, peliculas_info):
    nombre = input("Ingrese el nombre de la película a remover: ")
    if nombre in peliculas:
        peliculas.remove(nombre)
        del peliculas_info[nombre]
        print(f"Película '{nombre}' removida con éxito.")
    else:
        print("La película no existe.")

def consultar_peliculas(peliculas, peliculas_info):
    if peliculas:
        for nombre in peliculas:
            info = peliculas_info[nombre]
            print(f"Nombre: {nombre}")
            print(f"  Director: {info['director']}")
            print(f"  Año: {info['año']}")
            print(f"  Género: {info['género']}")
            print("")
    else:
        print("No hay películas registradas.")

def actualizar_pelicula(peliculas, peliculas_info):
    nombre = input("Ingrese el nombre de la película a actualizar: ")
    if nombre in peliculas:
        director = input(f"Nuevo director (anterior: {peliculas_info[nombre]['director']}): ")
        año = input(f"Nuevo año de estreno (anterior: {peliculas_info[nombre]['año']}): ")
        genero = input(f"Nuevo género (anterior: {peliculas_info[nombre]['género']}): ")

        peliculas_info[nombre] = {
            "director": director,
            "año": año,
            "género": genero
        }
        print(f"Película '{nombre}' actualizada con éxito.")
    else:
        print("La película no existe.")

def buscar_pelicula(peliculas, peliculas_info):
    nombre = input("Ingrese el nombre de la película a buscar: ")
    if nombre in peliculas:
        info = peliculas_info[nombre]
        print(f"Nombre: {nombre}")
        print(f"  Director: {info['director']}")
        print(f"  Año: {info['año']}")
        print(f"  Género: {info['género']}")
    else:
        print("La película no existe.")
        
def vaciar(peliculas, peliculas_info):
    peliculas.clear()
    peliculas_info.clear()
    print("Lista de películas vaciada correctamente.")
    