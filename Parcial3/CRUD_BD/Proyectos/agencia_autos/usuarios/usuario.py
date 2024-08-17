from conexionBD import *

class Usuarios:
    def __init__(self, usuario, contrasena, nombre):
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre

    @staticmethod
    def iniciarSesion(usuario,contrasena):
        try:
            cursor.execute(
                "SELECT * FROM usuarios WHERE usuario=%s AND contrasena=%s",
                (usuario, contrasena)
                )
            correcto = cursor.fetchone()
            if correcto:
                return True
            else: 
                return False
        except Exception as e:
            print("Error de inicio de sesión")
            return False

    def agregarUsuario(self):
        try:
            cursor.execute(
                "INSERT INTO usuarios VALUES (NULL, %s, %s, %s)",
                (self.usuario, self.contrasena, self.nombre)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False

    @staticmethod
    def mostrarUsuarios():
        try:
            cursor.execute("SELECT * FROM usuarios")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar usuarios: {e}")
            return []

    @staticmethod
    def actualizarUsuario(id, usuario, contrasena, nombre):
        try:
            cursor.execute(
                "UPDATE usuarios usuario=%s, contrasena=%s, nombre=%s WHERE id=%s",
                (usuario, contrasena, nombre, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False

    @staticmethod
    def eliminarUsuario(id):
        try:
            cursor.execute(
                "DELETE usuarios WHERE id=%s",
                (id,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False