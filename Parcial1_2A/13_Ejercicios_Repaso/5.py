#5.-Crear una lista y un diccionario con el contenido de esta tabla: 
#ACCION              TERROR        DEPORTES
# MAXIMA VELOCIDAD    LA MONJA       ESPN
# ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
# RAPIDO Y FURIOSO I  LA MALDICION   ACCION

tabla_lista = [
    ["ACCION", "TERROR", "DEPORTES"],
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

tabla_diccionario = {
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}

print("Tabla en lista:")
for fila in tabla_lista:
    print(fila)
    print("\nTabla en diccionario:")
    for clave, valor in tabla_diccionario.items():
        print(f"{clave}: {valor}")
        