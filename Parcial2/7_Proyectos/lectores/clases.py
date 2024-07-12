class Lectores:
    def __init__(self, nombre, direccion,tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel
        def reservar(self):
            print(f"Esta reservado el libro por : {self.getnombre()} su dirrecion es {self.getdireccion} y su numero de telefono es{self.gettel}")
        def entregar(self):
            print( f" el libro fue entregado por :{self.setnombre()} su dirrecion es {self.setdireccion} y su numero de telefono es{self.settel}")
    def getnombre(self):
        return self.nombre
    def getdireccion(self):
        return self.direccion
    def gettel(self):
        return self.tel
    def setnombre(self, nombre):
        self.nombre = nombre
    def setdireccion(self, direccion):
        self.direccion = direccion
    def settel(self, tel):
        self.tel = tel

class Estudiantes(Lectores):
   def _init_(self,nombre,direccion,tel,carrera,matricula):
     super()._init_(nombre,direccion,tel)
     self._carrera=carrera
     self._matricula=matricula

   def reservar(self):
        print(f"El estudiante: {self.getNombre()} reservo un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

   def entregar(self):
        print(f"El estudiante: {self.getNombre()} entrego un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

   def getCarrera(self):
      return self._carrera
   def getMatricula(self):
      return self._matricula
   
   def setCarrera(self,carrera):
      self._carrera=carrera
   def setMatricula(self,matricula):
      self._matricula=matricula   

class Docentes(Lectores):
   def _init_(self,nombre,direccion,tel,modalidad,num_empleado):
     super()._init_(nombre,direccion,tel)
     self.__modalidad=modalidad
     self.__num_empleado=num_empleado

   def reservar(self):
        print(f"El docente: {self.getNombre()} reservo un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

   def entregar(self):
        print(f"El docente: {self.getNombre()} entrego un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

   def getModalidad(self):
      return self.__modalidad
   def getNum_empleado(self):
      return self.__num_empleado
   
   def setModalidad(self,modalidad):
      self.__modalidad=modalidad
   def setMatricula(self,num_empleado):
      self.__num_empleado=num_empleado
