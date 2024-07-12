#Concatenar cadenas de caracteres con contenido de variables

nombre="Francisco Cervantes Diaz"
especialidad="Area de Desarroello de Sotfware"
Carrera="Ingeniero en gestion y desarollo de sw"
print ("\n")
#primer forma de concatenar
print("Minombre es: " + nombre+ " estoy en la especialidad de " + especialidad)

print ("\n")
#2da forma de concatenar
print("Minombre es: " ,nombre, " estoy en la especialidad de " , especialidad,)


print ("\n")
#3ra forma de concatenar
print(f"Mi nombre es:{ nombre} estoy en la especialidad de {especialidad} en la carrera de {Carrera}")



print("\n")
#4ta forma de concatenar
print("Mi nombre es:{} estoy en la especialidad de {} en la carrera de {}". 
      format(nombre,especialidad,Carrera))


