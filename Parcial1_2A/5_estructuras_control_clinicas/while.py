#Ciclo while Estructura  iterativa   que se ejecuta  x veces 
#sienpre y cuando la condicion se cumpla y se seguira ejecutando hasta un False
# sintaxis 
# while condicion
#bloque de instrucciones

#Ejemplo 1 
contador=1
while contador <=5:
    print('@')
    contador+=1
 

# ejemplo 2 que imprima llos numeros de 1 al 10 y despues los sume

    contador=1
    suma=0
while contador <=5:
    print(contador)     
    suma+=contador
contador+=1

print(f"la suma es: {suma}")

# ejemplo 3 que imprima la tabla de multiplicar
tabla=int(input("ingresa un numero para calcular su tabla:"))

i=1
multi=0

while i <=10:
    print(f"{tabla} x {i} = {multi}")
i+=1
    