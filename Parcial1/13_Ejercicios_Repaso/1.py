#1.-Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
#a.- Recorrer la lista y mostrarla
#b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#c.- ordenarla y mostrarla
#d.- mostrar su longitud
#e.- buscar algun elemento que el usuario pida por teclado
# a. Recorrer la lista y mostrarla
numeros = [1, 20, 83, 14, 45, 68, 67, 89]
print("Lista original:")
for num in numeros:
    print(num)

def lista_a_string(lista):
    return ", ".join(str(x) for x in lista)

print("\nLista como string:", lista_a_string(numeros))

numeros.sort()
print("\nLista ordenada:")
for num in numeros:
    print(num)

print("\nLongitud de la lista:", len(numeros))

busqueda = int(input("\nIngrese un número para buscar: "))
if busqueda in numeros:
    print(f"El número {busqueda} se encuentra en la lista.")
else:
    print(f"El número {busqueda} no se encuentra en la lista.")
