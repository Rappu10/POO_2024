#Mostrar todas las tablas del 1 al 10. 
#Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10 
print("TABLAS DE MULTIPLICAR DEL 1 AL 10")
for i in range(1,11):
    print(f"TABLA DEL {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
        print("\n") 