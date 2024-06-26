class Coches:
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    atributo_publico = "Soy un Atributo Publico"
    __atributo_privado = "Soy un Atributo Privado"

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def getCaballaje(self):
        return self.caballaje

    def setCaballaje(self, caballaje):
        self.caballaje = caballaje

    def getPlazas(self):
        return self.plazas

    def setPlazas(self, plazas):
        self.plazas = plazas

    def getInfo(self):
        print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp")

    def getAtributoPublico(self):
        return self.atributo_publico

    def getAtributoPrivado(self):
        return self.__atributo_privado


coche1 = Coches("VW Blanco", "VW", "2020", 202, 150, 5)
coche2 = Coches("Nissan Azul", "Nissan", "2020", 280, 150, 6)

print("Objeto 1")
coche1.getInfo()
print(coche1.getAtributoPublico())
print(coche1.getAtributoPrivado())

print("\nObjeto 2")
coche2.getInfo()
print(coche2.getAtributoPublico())
print(coche2.getAtributoPrivado())