from datetime import datetime
from conexionBD import insertar_datos, insertar_cita

class Mascota:
    def __init__(self, nombre, tipo, peso):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso

class Procedimiento:
    TARIFA_BASE = 50
    precios_accesorios = {
        1: 95,
        2: 150,
        3: 55,
        4: 230,
        5: 150
    }

    @staticmethod
    def obtener_costo(procedimiento, opcion=None, cantidad_accesorios=1):
        tarifas = {
            1: [0, 500, 300, 650, 1200, 800, 1500],
            2: Procedimiento.TARIFA_BASE * 1.5,
            3: Procedimiento.TARIFA_BASE,
            4: Procedimiento.precios_accesorios.get(opcion, 0) * cantidad_accesorios
        }

        if procedimiento in tarifas:
            if procedimiento == 1 and opcion is not None and 1 <= opcion <= 6:
                return tarifas[1][opcion]
            return tarifas[procedimiento]
        return 0

class Cita:
    def __init__(self, mascota, fecha, hora, procedimiento=None, opcion=None, cantidad_accesorios=1):
        self.mascota = mascota
        self.fecha = fecha
        self.hora = hora
        self.procedimiento = procedimiento
        self.opcion = opcion
        self.cantidad_accesorios = cantidad_accesorios

class Veterinaria:
    def __init__(self):
        self.acumulador_ingresos = 0
        self.contador_mascotas = 0
        self.acumulador_nombres = ""

    def registrar_mascota(self, mascota, procedimiento, opcion=None, cantidad_accesorios=1):
        costo = Procedimiento.obtener_costo(procedimiento, opcion, cantidad_accesorios)
        self.acumulador_ingresos += costo
        self.contador_mascotas += 1
        self.acumulador_nombres += mascota.nombre + " "
        print(f"El costo final del procedimiento para {mascota.nombre} es de ${costo}")
        insertar_datos(mascota, procedimiento, opcion, cantidad_accesorios, costo)

    def agendar_cita(self, cita):
        insertar_cita(cita)
        print(f"Cita agendada para {cita.mascota.nombre} el {cita.fecha} a las {cita.hora}")

    def mostrar_resultados(self):
        print("      Resultados")
        print("Total de mascotas registradas: ", self.contador_mascotas)
        print("Ingresos totales: $ ", self.acumulador_ingresos)
        print("Nombres de las mascotas ingresadas: ", self.acumulador_nombres.strip())

# Código principal
def main():
    veterinaria = Veterinaria()

    print("                   .::SISTEMA DE GESTION DE LA VETERINARIA::.")
    print("                Bienvenido al sistema de registro de la veterinaria ")

    while True:
        print("1. Registrar mascota y procedimiento")
        print("2. Agendar cita")
        opcion_menu = int(input("Seleccione una opción (1-2): "))

        if opcion_menu == 1:
            nombre_mascota = input("Ingrese el nombre de la mascota: ")
            tipo_mascota = input("Ingrese el tipo de mascota: ")
            peso_mascota = float(input("Ingrese el peso de la mascota en kg: "))

            mascota = Mascota(nombre_mascota, tipo_mascota, peso_mascota)

            while True:
                print("      Procedimientos disponibles")
                print("   1. Cirugías y/o procesos")
                print("   2. Vacunación")
                print("   3. Consulta")
                print("   4. Accesorios")
                procedimiento = int(input("Elija una opción (1-4): "))

                opcion = None
                cantidad_accesorios = 1

                if procedimiento == 1:
                    print("Cirugías y/o procesos disponibles:  ")
                    print("   1. Esterilización")
                    print("   2. Baño para eliminar bichos")
                    print("   3. Eutanasia")
                    print("   4. Parto")
                    print("   5. Tratamiento de huesos rotos")
                    print("   6. Prótesis")
                    opcion = int(input("Elija una opción (1-6): "))

                elif procedimiento == 4:
                    print("Accesorios disponibles:  ")
                    print("   1. Correa")
                    print("   2. Chaleco/ropa")
                    print("   3. Collar")
                    print("   4. Perfumes")
                    print("   5. Arenas")
                    opcion = int(input("Elija una opción (1-5): "))
                    cantidad_accesorios = int(input("¿Cuántos productos desea comprar? "))

                veterinaria.registrar_mascota(mascota, procedimiento, opcion, cantidad_accesorios)

                otro_procedimiento = input("¿Desea agregar otro procedimiento para la misma mascota? (SI/NO): ").strip().lower()
                if otro_procedimiento != "si":
                    break

        elif opcion_menu == 2:
            nombre_mascota = input("Ingrese el nombre de la mascota: ")
            fecha_cita = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
            hora_cita = input("Ingrese la hora de la cita (HH:MM:SS): ")

            mascota = Mascota(nombre_mascota, "", 0)  
            cita = Cita(mascota, fecha_cita, hora_cita)
            veterinaria.agendar_cita(cita)

        seguir_ingresando = input("¿Deseas realizar otra operación? (SI/NO): ").strip().lower()
        if seguir_ingresando != "si":
            break

    veterinaria.mostrar_resultados()

if __name__ == "__main__":
    main()
