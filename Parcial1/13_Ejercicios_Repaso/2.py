#2.- Escribir un programa  que añada valores a una lista mientras que su longitud 
# sea menor a 120, y luego mostrar la lista: Usar un while y for

mi_lista = []

i = 0
while len(mi_lista) < 121:
    mi_lista.append(i)
    i += 1
print("Lista completa:")
for elemento in mi_lista:
    print(elemento)