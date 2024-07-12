#import conexionBD
from conexionBD import *

try:
    micursor=conexion.cursor() 
    sql="create table clientes (id int primary key auto_increment, nombre varcahar(60),direccion varchar(120),tel varchar (10)"

    micursor.execute(sql)
except:
    print("Error al crear la tabla... Intente mas tarde")
else:
    print("Tabla creada con exito")