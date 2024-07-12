from calculadora import suma, resta, multiplicacion, division, potencia, raiz

def main():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    
    opcion = input("Seleccione una operación (1/2/3/4/5/6): ")
    num1 = float(input("Ingrese el primer número: "))
    
    if opcion in ['1', '2', '3', '4']:
        num2 = float(input("Ingrese el segundo número: "))
    
    if opcion == '1':
        print(f"Resultado: {suma(num1, num2)}")
    elif opcion == '2':
        print(f"Resultado: {resta(num1, num2)}")
    elif opcion == '3':
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif opcion == '4':
        print(f"Resultado: {division(num1, num2)}")
    elif opcion == '5':
        exponente = float(input("Ingrese el exponente: "))
        print(f"Resultado: {potencia(num1, exponente)}")
    elif opcion == '6':
        print(f"Resultado: {raiz(num1)}")
    else:
        print("Opción no válida")
        
if __name__ == "__main__":
    main()
    
    