# Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa 
    # mas pequeño que cumple una funcion especifica.
    # La funcion se puede reutilizar con el simple hecho de invocarla es decir mandarla a llamar
    
    # Sintaxis:
        
    #     def nombredeMifuncion(Parametros):
    #         Bloque o conjunto de instrucciones
            
    # nombredeMifuncion(Parametros)
    
    # Las funciones pueden ser de 4 tipos 
    # 1.-Funcion que no recibe parametros y no regresa valor
    #2.-Funcion que no recibe parametros y regresa valor
    #3.-Funcion que recibe parametros y no regresa valor
    #4.-Funcion que recibe parametros y regresa valor

    #1.-Funcion que no recibe parametros y regresa valor

def sumaNumeros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    suma = num1 + num2
    print(f"{num1}+{num2}={suma}")

sumaNumeros()

#Funcion que no recibe paramatros y regresa valor
def sumaNumeros2():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    suma = num1 + num2
    return(f"{num1}+{num2}={suma}")

print(sumaNumeros2())

#Funcion 3 que no recibe paramatros y regresa valor
def sumaNumeros3(num1,num2):
    suma = num1 + num2
    print(f"{num1}+{num2}={suma}")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
(sumaNumeros3(num1,num2))




#Funcion 4 que  recibe paramatros y regresa valor
def sumaNumeros4(num1,num2):
    suma = num1 + num2
    return f"{num1}+{num2}={suma}"

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
(sumaNumeros4(num1,num2))

 
#Ejemplo 6 Crear un programa que solicite a travez de una funcion la siguente informacion
#nombre del paciente, edad, estatutra, tipo de sangre
#utilizar los cuatro tipos de funiones
def paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    estatura = float(input("Ingrese la estatura del paciente (en metros): "))
    tipoSangre = input("Ingrese el tipo de sangre del paciente: ")
    return f"Nombre: {nombre}\nEdad: {edad} años\nEstatura
    {estatura} metros\nTipo de sangre: {tipoSangre}"
print(paciente())


