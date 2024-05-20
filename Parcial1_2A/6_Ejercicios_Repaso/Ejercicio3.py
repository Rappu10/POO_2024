 # Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for
print("Cuadrados de los 60 primeros números naturales:")
print("Con while:")
i = 0
while i <= 60:
    print(f"El cuadrado de {i} es {i**2}")
    i += 1
    print("Con for:")
    for i in range(61):
     print(f"El cuadrado de {i} es {i**2}")



    