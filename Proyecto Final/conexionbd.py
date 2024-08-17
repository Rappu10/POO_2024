import mysql.connector
from mysql.connector import Error

class ConexionBD:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                database='SistVeterinaria',
                user='root',
                password='1205'
            )
            if self.conn.is_connected():
                print('Conexión exitosa a la base de datos.')
        except Error as e:
            print(f'Error de conexión: {e}')
            self.conn = None

    def ejecutar_consulta(self, consulta, parametros):
        if self.conn is not None:
            try:
                cursor = self.conn.cursor()
                cursor.execute(consulta, parametros)
                self.conn.commit()
                print('Consulta ejecutada exitosamente.')
            except Error as e:
                print(f'Error al ejecutar la consulta: {e}')
            finally:
                cursor.close()
        else:
            print('No hay conexión a la base de datos.')

    def cerrar_conexion(self):
        if self.conn.is_connected():
            self.conn.close()
            print('Conexión cerrada.')

# Para probar la conexión directamente
if __name__ == "__main__":
    db = ConexionBD()
    db.cerrar_conexion()
