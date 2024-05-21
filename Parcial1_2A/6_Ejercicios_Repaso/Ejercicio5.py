# Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario


n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))


if n1 < n2:
  
    contador = n1

    while contador <= n2:
        print(contador)

        contador += 1

else:
    n1, n2 = n2, n1
    contador = n1

    while contador <= n2:
        print(contador)
        contador += 1

















