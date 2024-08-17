import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1205',
        database='agencia_autos'
    )
    cursor = conexion.cursor(buffered=True)
    print("Conexión exitosa a la base de datos")

except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")