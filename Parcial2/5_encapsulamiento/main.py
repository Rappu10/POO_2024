class Coches:
    def __init__(self, marca, plazas, modelo, velocidad, potencia):
        self.marca = marca
        self.plazas = plazas
        self.modelo = modelo
        self.velocidad = velocidad
        self.potencia = potencia
        self.atributo_publico = "Soy un Atributo Publico"

    def __str__(self):
        return f"Marca: {self.marca}, numeros de plazas: {self.plazas} \nModelo: {self.modelo} con una velocidad de {self.velocidad} Km/h y un potencia de {self.potencia} hp"

coche1 = Coches("VW Blanco", 5, "2020", 202, 150)
coche2 = Coches("Nissan Azul", 6, "2020", 280, 150)

print("Objeto 1")
print(coche1)
print(coche1.atributo_publico)

print("\nObjeto 2")
print(coche2)
print(coche2.atributo_publico)