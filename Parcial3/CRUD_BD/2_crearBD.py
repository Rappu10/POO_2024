import mysql.connector

#Conexion con la BD de MySQL
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='ramona'  
    )

    #Crear un objeo nuevo de tipo cursor para ejecutar SQL
    micursor=conexion.cursor()
    sql="create database bd_python"
    micursor.execute(sql)


except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e)._name_}")
    print(f"Ocurrió un error por favor vuelva inentar más tarde")

else:
#verificar si la conexion es correcto
    print(f"Se creo la base de datos exitosamente")
    micursor.execute("show databases")
    for x in micursor:
        print(x)