#Nombre del Paciente
#Tipo de sangre
#preguntar deseas otra captura

while True:
    nombre = input("Ingrese el nombre: ")
    tipo_sangre = input("Ingrese el tipo de sangre: ")
    
    sistolica_total = 0
    diastolica_total = 0

    for i in range(3):
        sistolica = int(input(f"Ingrese la presión sistólica {i+1}: "))
        diastolica = int(input(f"Ingrese la presión diastólica {i+1}: "))
        sistolica_total += sistolica
        diastolica_total += diastolica
    
    sistolica_final = int(input("Ingrese la presión sistólica final: "))
    diastolica_final = int(input("Ingrese la presión diastólica final: "))
    
    promedio_sistolica = sistolica_total / 3
    promedio_diastolica = diastolica_total / 3
    
    print(f"\nResultados para {nombre} (Tipo de sangre: {tipo_sangre}):")
    print(f"Promedio de la presión sistólica: {promedio_sistolica:.2f}")
    print(f"Promedio de la presión diastólica: {promedio_diastolica:.2f}")
    print(f"Presión Final (sistólica/diastólica): {sistolica_final}/{diastolica_final}")
    
    if sistolica_final <= 120 and diastolica_final <= 80:
        print("Presenta una presión normal")
    else:
        print("No presenta una presión normal")
    
    continuar = input("\n¿Desea otra captura? (si/no): ").strip().lower()
    if continuar != 'si':
        break