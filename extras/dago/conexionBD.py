import mysql.connector
from mysql.connector import Error

def insertar_datos(mascota, procedimiento, opcion, cantidad_accesorios, costo):
    try:
        # Establecer la conexión con MySQL
        connection = mysql.connector.connect(
            host='localhost',
            database='SistVeterinaria',
            user='root',
            password='1205'
        )
        
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Conectado al servidor MySQL versión ", db_Info)
            
            # Crear un cursor para ejecutar comandos SQL
            cursor = connection.cursor()

            # Verificar si la mascota ya está registrada
            cursor.execute("SELECT id FROM Mascotas WHERE nombre = %s", (mascota.nombre,))
            result = cursor.fetchone()
            
            if result:
                # Si la mascota ya existe, obtener su ID
                mascota_id = result[0]
            else:
                # Insertar datos en la tabla Mascotas si no está registrada
                insert_mascota_query = """
                INSERT INTO Mascotas (nombre, tipo, peso)
                VALUES (%s, %s, %s)
                """
                mascota_data = (mascota.nombre, mascota.tipo, mascota.peso)
                cursor.execute(insert_mascota_query, mascota_data)
                connection.commit()
                print("Datos insertados en Mascotas")
                
                # Obtener el ID de la nueva inserción en Mascotas
                cursor.execute("SELECT LAST_INSERT_ID()")
                mascota_id = cursor.fetchone()[0]
            
            # Insertar datos en la tabla Procedimientos
            insert_procedimiento_query = """
            INSERT INTO Procedimientos (tipo, opcion, cantidad_accesorios)
            VALUES (%s, %s, %s)
            """
            procedimiento_data = (procedimiento, opcion, cantidad_accesorios)
            cursor.execute(insert_procedimiento_query, procedimiento_data)
            connection.commit()
            print("Datos insertados en Procedimientos")
            
            # Obtener el ID de la última inserción en Procedimientos
            cursor.execute("SELECT LAST_INSERT_ID()")
            procedimiento_id = cursor.fetchone()[0]
            
            # Insertar datos en la tabla Registros
            insert_registro_query = """
            INSERT INTO Registros (mascota_id, procedimiento_id, costo)
            VALUES (%s, %s, %s)
            """
            registro_data = (mascota_id, procedimiento_id, costo)
            cursor.execute(insert_registro_query, registro_data)
            connection.commit()
            print("Datos insertados en Registros")

    except Error as e:
        print("Error al conectar con MySQL o insertar datos: ", e)

    finally:
        # Cerrar la conexión con MySQL al finalizar
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión con MySQL cerrada")

def insertar_cita(cita):
    try:
        # Establecer la conexión con MySQL
        connection = mysql.connector.connect(
            host='localhost',
            database='SistVeterinaria',
            user='root',
            password='1205'
        )
        
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Conectado al servidor MySQL versión ", db_Info)
            
            # Crear un cursor para ejecutar comandos SQL
            cursor = connection.cursor()

            # Verificar si la mascota ya está registrada
            cursor.execute("SELECT id FROM Mascotas WHERE nombre = %s", (cita.mascota.nombre,))
            result = cursor.fetchone()
            
            if result:
                mascota_id = result[0]
            else:
                print(f"La mascota {cita.mascota.nombre} no está registrada. Primero debe registrarse.")
                return

            # Insertar la cita en la tabla Citas
            insert_cita_query = """
            INSERT INTO Citas (fecha, hora, mascota_id, procedimiento_id, opcion, cantidad_accesorios)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cita_data = (
                cita.fecha,
                cita.hora,
                mascota_id,
                cita.procedimiento,
                cita.opcion,
                cita.cantidad_accesorios
            )
            cursor.execute(insert_cita_query, cita_data)
            connection.commit()
            print("Cita agendada en la base de datos")

    except Error as e:
        print("Error al conectar con MySQL o insertar datos: ", e)

    finally:
        # Cerrar la conexión con MySQL al finalizar
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión con MySQL cerrada")
