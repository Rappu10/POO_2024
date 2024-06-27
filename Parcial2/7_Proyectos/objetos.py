from clases import Rectangulo, Circulo, Triangulo

rectangulo = Rectangulo(largo=5.0, ancho=3.0)
print(f"Área del rectángulo: {rectangulo.calcular_area()}")

circulo = Circulo(radio=4.0)
print(f"Área del círculo: {circulo.calcular_area()}")

triangulo = Triangulo(altura=6.0, ancho=4.0)
print(f"Área del triángulo: {triangulo.calcular_area()}")
