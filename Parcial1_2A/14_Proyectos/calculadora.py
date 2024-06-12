import math
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(a, b):
    return a * b

def raiz(a):
    if a < 0:
        return "Error: No se puede calcular la raíz de un número negativo"
    return math.sqrt(a)
