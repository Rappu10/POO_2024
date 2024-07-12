# #Los tipos de datos más comunes en python son:
# primitivos o primarios
# int "Entero"
# float "real"
# bool "logico"

# Estructurados
# str "cadena"
# list   "Lista"
# tuple  
# dict   "como un objeto"

#Ejemplo de Primitivos
entero=80
real=3.1416
caracter='@'
logico=False

#Ejemplo de estructurados
palabra="hola"
lista=[10,20,30,40]
lista2=["hola",True,'@',30,1.8]
tupla=("Hola","como","estas?")
diccionario={
    "nombre":"Daniel",
    "apellidos":"Contreras Ramirez",
    "especialidad":"TI",
    "edad":20
}
#Mostrar los tipos de datos
print(type(entero))
print(type(real))
print(type(caracter))
print(type(logico))
print(type(palabra))
print(type(lista))
print(type(tupla))
print(type(diccionario))