#funciones globales locale ejemplos
# 1. Crear un diccionario que almacene la información de una persona:
#   - clave: nombre
#   - clave: edad
#   - clave: dirección
persona = {
    "nombre": "Juan",
    "edad": 25,
    "dirección": "Calle 123"
    }
print(persona)
# 2. Agregar una clave adicional al diccionario que almacene la información
#   de una persona:
persona["teléfono"] = "123456789"
print(persona)
# 3. Modificar el valor de una clave existente en el diccionario que
#   almacena la información de una persona:
persona["edad"] = 30
print(persona)
# 4. Eliminar una clave del diccionario que almacena la información de
#   una persona:
del persona["dirección"]
print(persona)
# 5. Crear un diccionario que almacene la información de varias personas
personas = {
    "persona1": {
        "nombre": "Juan",
        "edad": 25,
        "dirección": "Calle 123"
        },
        "persona2": {
            "nombre": "María",
            "edad": 30,
            "dirección": "Calle 456"
            }
            }
print(personas)
# 6. Acceder a una clave específica de un diccionario anidado
print(personas["persona1"]["nombre"])
# 7. Iterar sobre un diccionario y mostrar sus claves y valores
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
    # 8. Iterar sobre un diccionario anidado y mostrar sus claves y
    #    valores
    for clave, valor in personas.items():
        print(f"Persona {clave}:")
        for clave_interna, valor_interno in valor.items():
            print(f"  {clave_interna}: {valor_interno}")
