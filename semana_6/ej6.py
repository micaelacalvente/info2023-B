planificacion = [
    #LUNES
    [
        {"horario": "8:00", "compañia": "A", "duracion": "2 horas", "tipo_avion": "Boeing 737"}
    ],
    #MARTES
    [
        {"horario": "8:00", "compañia": "A", "duracion": "2 horas", "tipo_avion": "Boeing 737"}
    ],
    #MIERCOLES
    [
        {"horario": "8:00", "compañia": "A", "duracion": "2 horas", "tipo_avion": "Boeing 737"}
    ],
    #JUEVES
    [
        {"horario": "8:00", "compañia": "A", "duracion": "2 horas", "tipo_avion": "Boeing 737"}
    ],
    #VIERNES
    [
        {"horario": "8:00", "compañia": "A", "duracion": "2 horas", "tipo_avion": "Boeing 737"}
    ],
]

# funcion para mostrar la informacion al viajante
def mostrar_info(dia):
    if dia >= 1 and dia <= 5:
        print(f"vuelos del {dia}")
        vuelos = planificacion[dia - 1]
        for vuelo in vuelos:
            print(vuelo)
    else:
        print("Aeropuerto cerrado")

dia_semana = int(input("Ingrese el día de la semana\n1-LUNES\n2-MARTES\n3-MIERCOLES\n4-JUEVES\n5-VIERNES\n: "))
mostrar_info(dia_semana)