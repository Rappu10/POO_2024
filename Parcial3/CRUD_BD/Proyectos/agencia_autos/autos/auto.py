from conexionBD import *

class Autos:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif

    def agregarAuto(self):
        try:
            cursor.execute(
                "INSERT INTO agencia_autos_datos_autos VALUES (%s, %s, %s, %s, %s)",
                (self.matricula, self.marca, self.modelo, self.color, self.nif)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear auto: {e}")
            return False

    @staticmethod
    def mostrarAutos():
        try:
            cursor.execute("SELECT * FROM agencia_autos_datos_autos")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar autos: {e}")
            return []

    @staticmethod
    def actualizarAuto(matricula, marca, modelo, color, nif):
        try:
            cursor.execute(
                "UPDATE agencia_autos_datos_autos SET marca=%s, modelo=%s, color=%s, nif=%s WHERE matricula=%s",
                (marca, modelo, color, nif, matricula)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar auto: {e}")
            return False

    @staticmethod
    def eliminarAuto(matricula):
        try:
            cursor.execute(
                "DELETE FROM agencia_autos_datos_autos WHERE matricula=%s",
                (matricula,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar auto: {e}")
            return False