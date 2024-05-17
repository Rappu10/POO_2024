5
# Calcular o imprimir el precio a pagar por un artículo
# El precio a pagar incluye el IVA. El programa deberá funcionar x veces según el deseo del usuario.


veces = int(input("Ingrese la cantidad de veces que desea calcular el precio: "))

#
contador = 1

while contador <= veces:

    precio = float(input("Ingrese el precio del artículo sin IVA: "))


    iva = precio * 0.16

   
    precio_a_pagar = precio + iva

    print(f"El precio a pagar es: {precio_a_pagar}")


    contador += 1
