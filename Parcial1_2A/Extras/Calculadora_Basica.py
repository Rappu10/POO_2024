def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def imprimir_operacion(operacion, num1, num2, resultado):
    print(f"{num1} {operacion} {num2} = {resultado}")
    
print("..::/CALCULADORA BASICA\::.. ")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")

opcion = input("Elige una opción: ").upper()

if opcion == "1" or opcion == "+" or opcion == "SUMA":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = suma(num1, num2)
    imprimir_operacion("+", num1, num2, resultado)

elif opcion == "2" or opcion == "-" or opcion == "RESTA":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = resta(num1, num2)
    imprimir_operacion("-", num1, num2, resultado)

elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = multiplicacion(num1, num2)
    imprimir_operacion("*", num1, num2, resultado)

elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = division(num1, num2)
    imprimir_operacion("/", num1, num2, resultado)

else:
    print("Gracias por utilizar el sistema BD")
