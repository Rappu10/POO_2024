
from conexionBD import * 

try:
    micursor=conexion.cursor() 
    sql="INSERT INTO (id,nombre,direccion,tel)VALUES (NULL,'Juan Polainas','Col. del Valle','6181234567')"

    micursor.execute(sql)
    #es necesario ejecutar el comit para que finalize el sql con exito
    conexion.commit()
    print("Se inserto correctamente")
except:
    print("Error al crear la tabla... Intente mas tarde")
else:
    print("Tabla creada con exito")
