from conexionBD import *

class Revisiones:
    def __init__(self, no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
        self.no_revision = no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiofrenos
        self.otros = otros
        self.matricula = matricula

    def agregarServicio(self):
        try:
            cursor.execute(
                "INSERT INTO agencia_autos_datos_revisiones VALUES (%s, %s, %s, %s, %s, %s)",
                (self.no_revision, self.cambiofiltro, self.cambioaceite, self.cambiofrenos, self.otros, self.matricula)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al agregar servicio: {e}")
            return False

    @staticmethod
    def mostrarServicios():
        try:
            cursor.execute("SELECT * FROM agencia_autos_datos_revisiones")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar Servicios: {e}")
            return []

    @staticmethod
    def actualizarServicio(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
        try:
            cursor.execute(
                "UPDATE agencia_autos_datos_revisiones SET no_revision=%s, cambiofiltro=%s, cambioaceite=%s, cambiofrenos=%s, otros=%s WHERE matricula=%s",
                (cambiofiltro, cambioaceite, cambiofrenos, otros, matricula, no_revision)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar servicio: {e}")
            return False

    @staticmethod
    def eliminarServicio(no_revision):
        try:
            cursor.execute(
                "DELETE FROM agencia_autos_datos_revisiones WHERE no_revision=%s",
                (no_revision,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar servicio: {e}")
            return False