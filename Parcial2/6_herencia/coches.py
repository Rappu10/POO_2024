"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

METODO CONSTRUCTOR.- Este metodo especial dentro de una clase y se utiliza para dar un valor a los atributos del objeto al crearlo, es el primer metodo que se ejecuta al crear el objeto y se manda llamar automaticamente al crearlo, es decir este metodo puede recibir parametros al momento de crear el objeto 

Cuando se crear un metodo constructor se utiliza la funcion init(), para que se llame automáticamente cada vez que se utiliza la clase para crear un nuevo objeto.

El self es un parámetro es una referencia a la instancia actual de la clase y se utiliza para acceder a variables que pertenecen a la clase.

No es necesario que tenga nombre self, puedes llamarlo como quieras, pero tiene que ser el primer parámetro de cualquier función de la clase. Es decir por regla se utiliza en la palabra self pero puede ser llamado con otro nombre por ejemplo: valor, abd, parametro, etc.

"""



#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
     #Metodo constructor

    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas

    #El encapsulamiento o visibilidad es importante que a traves de el es posible que python sepa como va a utilizar y manipular los atributos y metodos de la clase

    #atributo publico 
    atributo_publico="Soy un atributo publico"
    #atributo privado
    __atributo_privado="Soy un atributo privado"

    #Nota 1, para utilizar un atributo privado es necesario usarlo dentro de un metodo publico
    def MetodoPublico(self):
      return self.__atributo_privado

    #Metodo privado
    def __MetodoPrivado(self):
      print("Soy un metodo privado")

    #Nota 2, para utilizar un metodo privado es necesario usuarlo dentro de un metodo publico
    def getMetodoPublico(self):
      self.__MetodoPrivado()
           


    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1


    #Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getColor(self):
      return self.color

    def setColor(self,color):
      self.color=color 

    def getMarca(self):
      return self.marca

    def setMarca(self,marca):
      self.marca=marca 

    def getModelo(self):
      return self.modelo

    def setModelo(self,modelo):
      self.modelo=modelo        

    def getVelocidad(self):
       return self.velocidad

    def setVelocidad(self,velocidad):
      self.velocidad=velocidad 

    def getCaballaje(self):
       return self.caballaje

    def setCaballaje(self,caballaje):
      self.caballaje=caballaje  

    def getPlazas(self):
       return self.plazas

    def setPlazas(self,plazas):
      self.plazas=plazas 

    def getInfo(self):
       print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp")  

#Fin definir clase coches

#Clases Secundarias, SubClases, Hijas
class Camiones(Coches):
   def __init__(self,color,marca,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
    super().__init__(color,marca,modelo,velocidad,caballaje,plazas)
    self.eje=eje
    self.capacidadCarga=capacidadCarga

   __tipo_carga=""

   def cargar(self,tipo_carga):
    self.__tipo_carga=tipo_carga
    return self.__tipo_carga

   def getEje(self):
     return self.eje

   def setEje(self,eje):
      self.eje=eje  

   def getcapacidadCarga(self):
     return self.capacidadCarga

   def setcapacidadCarga(self,capacidadCarga):
      self.capacidadCarga=capacidadCarga 

   def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h, una potencia de {self.getCaballaje()} hp, con {self.getEje()} ejes y una capacidad de carga de {self.getcapacidadCarga()} metros cubicos")       


class Camionetas(Coches):
  def __init__(self,color,marca,modelo,velocidad,caballaje,plazas,trasera,cerrada):
    super().__init__(color,marca,modelo,velocidad,caballaje,plazas)
    self.traccion=trasera
    self.cerrada=cerrada

  __num_pasajeros=0
  def transportar(self,num_pasajeros):
      self.__num_pasajeros=num_pasajeros
      return self.__num_pasajeros

  def setTraccion(self,traccion):
     self.traccion=traccion

  def getTraccion(self):
    return self.traccion

  def setCerrada(self,traccion):
     self.cerrada=cerrada

  def getCerrada(self):
    return self.cerrada

  def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h, una potencia de {self.getCaballaje()} hp, con la tracción {self.getTraccion()} y es cerrada {self.getCerrada()} ")
