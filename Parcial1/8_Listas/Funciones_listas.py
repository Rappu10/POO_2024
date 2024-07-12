from tkinter import W


paises=["Mexico","USA","Brasil","China"]
numeros=[100,80,3.1416,75]
varios=["UTD",True,100,0.100]


#Orden las listas
print(paises)
paises.sort()
print(paises)



print(numeros)
numeros.sort()
print(numeros)

# print(varios)
# varios.sort()
# print(varios)

#Agregar elementos 
print(numeros)
numeros.appel(100)
print(numeros)
numeros.insert(len(numeros),200)
print(numeros)


#Remover elementos 
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(5)
print(numeros)

print(varios)
varios.reverse
print(varios)

#buscar valor dentro de una lista
encontro="Brasil" in varios
print(encontro)

print(paises)
paises.clear()
print(paises)

print(varios)
varios.extend(numeros)
print(numeros)

