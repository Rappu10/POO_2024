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
        if procedimiento == 1:
            tarifas = [0, 500, 300, 650, 1200, 800, 1500]
            if opcion is not None and 1 <= opcion <= 6:
                return Procedimiento.TARIFA_BASE * (tarifas[opcion] / Procedimiento.TARIFA_BASE)
        elif procedimiento == 2:
            return Procedimiento.TARIFA_BASE * 1.5
        elif procedimiento == 3:
            return Procedimiento.TARIFA_BASE
        elif procedimiento == 4:
            if opcion is not None and 1 <= opcion <= 5:
                return Procedimiento.precios_accesorios[opcion] * cantidad_accesorios
        return 0

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

    def mostrar_resultados(self):
        print("      Resultados")
        print("Total de mascotas registradas: ", self.contador_mascotas)
        print("Ingresos totales: $ ", self.acumulador_ingresos)
        print("Nombres de las mascotas ingresadas: ", self.acumulador_nombres.strip())

# Código principal
veterinaria = Veterinaria()

print("                   .::SISTEMA DE GESTION DE LA VETERINARIA LAS RANAS::.")
print("                Bienvenido al sistema de registro de la veterinaria Las ranas ")

seguir_ingresando = "SI"

while seguir_ingresando.lower() == "si":
    print("                                   Datos de la mascota")
    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    tipo_mascota = input("Ingrese el tipo de mascota: ")
    peso_mascota = float(input("Ingrese el peso de la mascota en kg: "))

    mascota = Mascota(nombre_mascota, tipo_mascota, peso_mascota)

    print("      Procedimientos disponibles")
    print("Ingrese el procedimiento a realizar:  ")
    print("   1. cirugias y/o procesos")
    print("   2. vacunacion")
    print("   3. consulta")
    print("   4. accesorios")
    procedimiento = int(input("Elija una opción (1-4): "))

    opcion = None
    cantidad_accesorios = 1

    if procedimiento == 1:
        print("Cirugias y/o procesos disponibles:  ")
        print("   1. Esterilizacion")
        print("   2. Baño para eliminar bichos")
        print("   3. Eutanasia")
        print("   4. Parto")
        print("   5. Tratamiento de huesos rotos")
        print("   6. Protesis")
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
    seguir_ingresando = input("¿Deseas agregar otra mascota? (SI/NO): ")

veterinaria.mostrar_resultados()
