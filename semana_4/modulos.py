# # # MODULO RANDOM
import random
# Genera un número aleatorio entre 1 y 10
random_number = random.randint(1, 10)
print(random_number)

# Lista de palabras
palabras = ["manzana", "banana", "naranja", "pera", "uva"]

# Selecciona una palabra al azar
palabra_elegida = random.choice(palabras)

# Imprime la palabra elegida
print("La palabra elegida es:", palabra_elegida)

# # # MODULO TIME
import time
# Imprime la hora actual en formato legible
current_time = time.strftime("%H:%M:%S")
print("Hora actual:", current_time)

# Espera 2 segundos antes de continuar
time.sleep(2)

# # # MODULO MATH
import math
# Calcula el seno de 30 grados
sin_30_degrees = math.sin(math.radians(30))
print(sin_30_degrees)

# # # MODULO CALENDAR
import calendar

# Imprime el calendario de un mes y año específicos
cal = calendar.month(2023, 10)
print(cal)

# # # MODULO OS
import os

current_directory = os.getcwd()  # Obtiene el directorio de trabajo actual
print(current_directory)

# # # MODULO DATETIME   
from datetime import datetime
now = datetime.now()
print(now)

# Obtener la descripción de un método o función específico
help(math.sin)  # Reemplaza "math.sin" con el nombre del método que desees conocer

# Otra opción es utilizar la función "pydoc" en la línea de comandos
# Ejemplo: pydoc math.sin

# lista de métodos y atributos
print(dir(math))
