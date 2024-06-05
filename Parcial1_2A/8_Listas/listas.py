"""
List (Array)
son colecciones o conjunto de datos/valores bajo 
un mismo nombre, para acceder a los valores se
hace con un índice numérico

Nota: sus valores sí son modificables

La lista es una colección ordenada y modificable. permite miembros
duplicados.


"""

#Ejemplo 1 crear una lista con valores numericos enteros e imprimir la lista
numeros=[23,34]
print(numeros)


#Recorrer la lista con for
for i in numeros:
    print(i)

##Recorrer la lista con un while 
i=0
while i<len(numeros):
    print(numeros][i])
    i=+1

#Ejemplo 2 Crear una lista de palabras, posteriormente ingresar una palabra para buscar la coincidencia en la lista 
#indicar si aparece la palabra y en que posicion en caso contrario indicar una sola vez si no la encontro

palabras=["hola,2024,bob,True"]

palabra_buscar=input("Ingresa la palabra a buscar")
if palabra_buscar in palabras:
    print(f"La palabra {palabra_buscar} se encuentra en la lista en la posición
          {palabras.index(palabra_buscar)}")
else:
  print(f"La palabra {palabra_buscar} no se encuentra en la lista")
