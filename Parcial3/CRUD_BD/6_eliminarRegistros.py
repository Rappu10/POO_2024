from conexionBD import * 

try:
    micursor=conexion.cursor() 
    sql="select * from clientes"

    micursor.execute(sql)
    
    resultado=micursor.fetchall
    
    for fila in resultado:
        print(f"id:{fila[0]}| Nombre: {fila[1]} | Direccion: {fila[2]} | Telefono: {fila[3]} ")
        
except:
    print("Error al crear la tabla... Intente mas tarde")
else:
    print("Tabla creada con exito")