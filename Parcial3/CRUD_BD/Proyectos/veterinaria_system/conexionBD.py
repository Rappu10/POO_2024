import mysql.connector

#Conexion con la BD de MySQL
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='1205',
        database='bd_notas'  
    )
except Exception as e:
    print(f"Ocurrió un error por favor vuelva inentar más tarde")