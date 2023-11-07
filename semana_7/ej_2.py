# creamos superclase / clase padre
class Vehiculo():
    # constructor de atributos
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"Vehiculo color {self.color} con {self.ruedas} ruedas"
    
# creamos subclases / clases hijos
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f"{super().__str__()} {self.velocidad} km/hr + {self.cilindrada} cc"
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return f"{super().__str__()} de tipo: {self.tipo}"

# creamos hijos de los hijos
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def __str__(self):
        return f"{super().__str__()} con {self.carga} kg de carga"

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return f"{super().__str__()} con {self.velocidad} km/hr + {self.cilindrada} cc"

# FUNCION 1 / PRIMERA VERSION DE CATALOGAR / PUNTO 2
'''def catalogar(lista):
    for vehiculo in lista:
        print(f"Clase: {vehiculo.__class__.__name__} ")
        print(f"Atributos: {vehiculo}")'''

# FUNCION 2 / SEGUNDA VERSION DE CATALOGAR / PUNTO 3
def catalogar(lista, ruedas=None):
    if ruedas != None:
        vehiculos_filtro = [vehiculo for vehiculo in lista if vehiculo.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtro)} vehículos con {ruedas} ruedas")
    else:
        for vehiculo in lista:
            print(f"Clase: {vehiculo.__class__.__name__} ")
            print(f"Atributos: {vehiculo}")


# crear lista de vehiculos
vehiculos = [
    Coche("azul", 4, 220, 2000),
    Bicicleta("rojo", 2, "urbana"),
    Camioneta("blanco", 4, 250, 2500, 50),
    Motocicleta("amarillo", 2, "urbana", 150, 1500),
    Motocicleta("verde", 2, "urbana", 150, 1500)
]

catalogar(vehiculos, 0)

print(Motocicleta.mro())