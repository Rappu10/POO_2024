#manejo de errores es la forma en la que tiene los lenguajes de programacion para evitar que sucedan errores en el tiempo de ejecucion


#ejemplo 1 error cuando una variable nose genera
try: 
  nombre=input("dame el nombre")

  if len(nombre)>1:
    nombre_usuario="El nombre es "+ nombre
    
  print(nombre_usuario)
except:
    print("Es necesario Introducir un  nombre de usuario")


#Ejemplo 2 cuando se solicita un numerony se introduce una letra
try:
  numero=int(input("Dame un Numero"))

  if numero>0:
    print("El numero es positivo")
  else:
    print("El numero es negativo")

except:
    print("Es necesario Introducir un Numero")
    
#Ejemplo 3 Multiples excepciones

try:
  numero+int(input("Dame un numero:"))
  print("El cuadrado es "+str(numero*numero))
  
except ValueError:
 print("Es necesario Introducir un Numero")
except TypeError
 print("No se puede realizar la operacion")
      

1