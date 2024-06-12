#4-Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

def imprimir_tipo_de_dato(variable):
    if isinstance(variable, list):
        print("La variable es una lista")
    elif isinstance(variable, str):
        print("La variable es una cadena")
    elif isinstance(variable, int):
        print("La variable es un entero")
    elif isinstance(variable, bool):
        print("La variable es un booleano")

lista = [1, 2, 3, 4, 5]
cadena = "Hola, mundo!"
entero = 10
logico = True

imprimir_tipo_de_dato(lista)
imprimir_tipo_de_dato(cadena)
imprimir_tipo_de_dato(entero)
imprimir_tipo_de_dato(logico)
