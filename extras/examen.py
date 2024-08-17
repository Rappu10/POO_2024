import mysql.connector

class Cliente:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1205',
            database='Clientes'
        )
        self.cursor = self.connection.cursor()

    def insertar(self, nombre, apellido, telefono, email):
        sql = "INSERT INTO Clientes (nombre, apellido, telefono, email) VALUES (%s, %s, %s, %s)"
        valores = (nombre, apellido, telefono, email)
        self.cursor.execute(sql, valores)
        self.connection.commit()
        print("Cliente insertado exitosamente.")

    def consultar(self, id_cliente=None):
        if id_cliente:
            sql = "SELECT * FROM Clientes WHERE id = %s"
            self.cursor.execute(sql, (id_cliente,))
        else:
            sql = "SELECT * FROM Clientes"
            self.cursor.execute(sql)
        
        resultados = self.cursor.fetchall()
        for cliente in resultados:
            print(cliente)

    def actualizar(self, id_cliente, nombre=None, apellido=None, telefono=None, email=None):
        campos = []
        valores = []
        
        if nombre:
            campos.append("nombre = %s")
            valores.append(nombre)
        if apellido:
            campos.append("apellido = %s")
            valores.append(apellido)
        if telefono:
            campos.append("telefono = %s")
            valores.append(telefono)
        if email:
            campos.append("email = %s")
            valores.append(email)
        
        valores.append(id_cliente)
        
        sql = f"UPDATE Clientes SET {', '.join(campos)} WHERE id = %s"
        self.cursor.execute(sql, tuple(valores))
        self.connection.commit()
        print("Cliente actualizado exitosamente.")

    def eliminar(self, id_cliente):
        sql = "DELETE FROM Clientes WHERE id = %s"
        self.cursor.execute(sql, (id_cliente,))
        self.connection.commit()
        print("Cliente eliminado exitosamente.")

    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()

def menu():
    cliente_db = Cliente()
    
    while True:
        print("\nMenú de Opciones:")
        print("1. Insertar Cliente")
        print("2. Consultar Cliente")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            cliente_db.insertar(nombre, apellido, telefono, email)

        elif opcion == '2':
            id_cliente = input("Ingresa el ID del cliente (o deja en blanco para consultar todos): ")
            if id_cliente:
                cliente_db.consultar(int(id_cliente))
            else:
                cliente_db.consultar()

        elif opcion == '3':
            id_cliente = int(input("ID del Cliente a actualizar: "))
            nombre = input("Nuevo Nombre (deja en blanco para no cambiar): ")
            apellido = input("Nuevo Apellido (deja en blanco para no cambiar): ")
            telefono = input("Nuevo Teléfono (deja en blanco para no cambiar): ")
            email = input("Nuevo Email (deja en blanco para no cambiar): ")
            cliente_db.actualizar(id_cliente, nombre, apellido, telefono, email)

        elif opcion == '4':
            id_cliente = int(input("ID del Cliente a eliminar: "))
            cliente_db.eliminar(id_cliente)

        elif opcion == '5':
            cliente_db.cerrar_conexion()
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
