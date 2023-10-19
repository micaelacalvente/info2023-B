# Crear un diccionario para almacenar la planificación de vuelos por día de la semana
planificacion_vuelos = {
    "Lunes": [],
    "Martes": [],
    "Miércoles": [],
    "Jueves": [],
    "Viernes": [],
    "Sábado": [],
    "Domingo": []
}

# Agregar vuelos a la planificación
vuelo1 = {
    "horario": "08:00",
    "compania": "Aerolínea X",
    "duracion_estimada": "2 horas",
    "tipo_avion": "Boeing 737"
}

vuelo2 = {
    "horario": "12:30",
    "compania": "Aerolínea Y",
    "duracion_estimada": "3 horas",
    "tipo_avion": "Airbus A320"
}

# Agregar vuelos a días específicos
planificacion_vuelos["Lunes"].append(vuelo1)
planificacion_vuelos["Lunes"].append(vuelo2)
planificacion_vuelos["Martes"].append(vuelo1)
planificacion_vuelos["Miércoles"].append(vuelo2)

# Imprimir la planificación de vuelos para un día específico
print("Planificación de vuelos para el Lunes:")
for vuelo in planificacion_vuelos["Lunes"]:
    print(vuelo)