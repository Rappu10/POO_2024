#Existe una estructrura  de condicion llamada if
#la cual evalua una condicion 














#Ejemplo 1 if simple
color=input("ingresa el color")

if color=="rojo":
    print("soy el color rojo")

#Ejemplo 2 if compuesto
color=input("ingresa el color")

if color=="rojo":
    print("soy el color rojo")
else:
    print("No soy el color rojo")



 #Ejemplo 3 if aninado
color=input("ingresa el color")

if color=="rojo":
    print("soy el color rojo")
else:
    print("No soy el color rojo")   






 #Ejemplo 4 if - elif
color=input("ingresa el color")

if color=="rojo":
    print("soy el color rojo")
elif color=="amarillo":
    print("soy el color amarillo")
elif color=="azul":
    print("soy el color azul")
elif color=="mora":
    print("soy el color mora")
else:
    print("No soy ningun color")

#Crear un programa que solicite el numero de la semana e imprima en pantalla el dia que le corresponde
dias=input("ingresa un dia de la semana")

if dias=="1":
    print("Lunes")
elif dias=="2":
    print("Martes")
elif dias=="3":
    print("Miercoles")
elif dias=="4":
    print("Jueves")
elif dias=="5":
    print("Viernes")
elif dias=="6":
    print("Sabado")
elif dias=="7":
    print("Domingo")
else:
    print("No soy ningun dia de la semana")
