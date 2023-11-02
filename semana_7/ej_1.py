# creamos superclase / clase padre
class Vehiculo():
    # constructor de atributos
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"Vehiculo color {self.color} con {self.ruedas} ruedas"

# creamos subclase / clase hijo
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f"{super().__str__()} {self.velocidad} km/hr + {self.cilindrada} cc"

v = Vehiculo("azul", 4)
print(v)

c = Coche("negro", 4, 150, 2000)
print(c)