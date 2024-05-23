#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

def main():
    calificaciones = []
    total_alumnos = 15
    calificacion_aprobatoria = 60
    for i in range(total_alumnos):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación del alumno {i+1}: "))
                if 0 <= calificacion <= 100:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("Por favor, ingrese una calificación válida (entre 0 y 100).")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
    
    aprobados = sum(1 for calificacion in calificaciones if calificacion >= calificacion_aprobatoria)
    no_aprobados = total_alumnos - aprobados

    print(f"Alumnos aprobados: {aprobados}")
    print(f"Alumnos no aprobados: {no_aprobados}")
if __name__ == "__main__":
    main()
    