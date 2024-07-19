import mysql.connector
from mysql.connector import Error

try:
    # Establecer la conexión con MySQL
    connection = mysql.connector.connect(
        host='localhost',    # Nombre del servidor MySQL
        database='nombre_de_tu_base_de_datos',  # Nombre de tu base de datos
        user='usuario_de_mysql',     # Nombre de usuario de MySQL
        password='contraseña_de_mysql'  # Contraseña de usuario de MySQL
    )
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado al servidor MySQL versión ", db_Info)
        
        # Ejecutar una consulta SQL de ejemplo
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Conectado a la base de datos ", record)
        
        # Ejecutar más consultas SQL según tus necesidades
        
except Error as e:
    print("Error al conectar con MySQL: ", e)

finally:
    # Cerrar la conexión con MySQL al finalizar
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("Conexión con MySQL cerrada")
