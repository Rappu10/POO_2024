from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self._largo = largo
        self._ancho = ancho
    
    @property
    def largo(self):
        return self._largo
    
    @largo.setter
    def largo(self, value):
        self._largo = value
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, value):
        self._ancho = value
    
    def calcular_area(self):
        return self._largo * self._ancho

class Circulo(Figura):
    def __init__(self, radio):
        self._radio = radio
    
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, value):
        self._radio = value
    
    def calcular_area(self):
        import math
        return math.pi * (self._radio ** 2)

class Triangulo(Figura):
    def __init__(self, altura, ancho):
        self._altura = altura
        self._ancho = ancho
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, value):
        self._altura = value
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, value):
        self._ancho = value
    
    def calcular_area(self):
        return (self._ancho * self._altura) / 2
