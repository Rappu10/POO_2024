import mysql.connector

# Conexión con la BD de MySQL
try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1205'
    )

    # Crear un objeto nuevo de tipo cursor para ejecutar SQL
    micursor = conexion.cursor()
    sql = "CREATE DATABASE bd_python"
    micursor.execute(sql)

except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrió un error, por favor vuelva a intentar más tarde")

else:
    # Verificar si la conexión es correcta
    print(f"Se creó la base de datos exitosamente")
    micursor.execute("SHOW DATABASES")
    for x in micursor:
        print(x)
finally:
    if 'conexion' in locals() and conexion.is_connected():
        micursor.close()
        conexion.close()
