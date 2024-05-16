#Ciclo  for Estructura  iterativa   que se ejecuta  x veces

# sintaxis 
# for variable in elemento iterable 
#bloque de instrucciones

#Ejemplo 1 

contador=1

for contador in range(1,6):
    print('@')
 

# ejemplo 2 que imprima llos numeros de 1 al 10 y despues los sume
    contador=1
    suma=0
for contador in range(1,11):
    print(contador)     
    suma+=contador
    print(f"la suma es: {suma}")

# ejemplo 3 que imprima la tabla de multiplicar
tabla=int(input("ingresa un numero para calcular su tabla:"))

i=1
multi=0

for i in range(1,11):
    multi=i*tabla
    print(f"{tabla}{multi}")




  