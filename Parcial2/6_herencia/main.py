
from coches import *

#Crear un objetos o instanciar la clase
print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
coche1.getInfo()

#Crear otro objeto e imprimir los valores
print("Objeto 2")
coche2=Coches("Azul","Nissan","2020",180,150,6)
coche2.getInfo()

#Crear los objetos o instancias de las clases camiones y camionetas
print("Objeto 3")
camion1=Camiones("Negro","Dina","2020",180,300,12,8,2500)
camion1.getInfo()

print("Objeto 4")
camion1=Camiones("Azul","Star","2019",150,300,14,6,2000)
camion1.getInfo()

print("Objeto 5")
camioneta1=Camionetas("Amarillo","Renault","2025",240,250,8,"Delantera",True)
camioneta1.getInfo()

print("Objeto 6")
camioneta1=Camionetas("Blanca","Nissan","2020",180,150,6,"Trasera",False)
camioneta1.getInfo()

