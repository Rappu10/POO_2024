from conexionBD import *

class Clientes:
    def __init__(self, nif, nombre, direccion, ciudad, telefono):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono

    def agregarCliente(self):
        try:
            cursor.execute(
                "INSERT INTO agencia_autos_datos_clientes VALUES (%s, %s, %s, %s, %s)",
                (self.nif, self.nombre, self.direccion, self.ciudad, self.telefono)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear cliente: {e}")
            return False

    @staticmethod
    def mostrarClientes():
        try:
            cursor.execute("SELECT * FROM agencia_autos_datos_clientes")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar clientes: {e}")
            return []

    @staticmethod
    def actualizarCliente(nif, nombre, direccion, ciudad, telefono):
        try:
            cursor.execute(
                "UPDATE agencia_autos_datos_clientes SET nombre=%s, direccion=%s, ciudad=%s, tel=%s WHERE nif=%s",
                (nombre, direccion, ciudad, telefono, nif)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False

    @staticmethod
    def eliminarCliente(nif):
        try:
            cursor.execute(
                "DELETE FROM agencia_autos_datos_clientes WHERE nif=%s",
                (nif,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False