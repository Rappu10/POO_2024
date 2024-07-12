# Hacer un programa que resuelva lo siguiente.
# ¿Cuanto es el X por ciento de X numero?

def calcular_porcentaje(porcentaje, numero):
    resultado = (porcentaje / 100) * numero
    return resultado

porcentaje = float(input("Ingrese el porcentaje (%): "))
numero = float(input("Ingrese el número: "))

resultado = calcular_porcentaje(porcentaje, numero)

print(f"{porcentaje}% de {numero} es {resultado}")

