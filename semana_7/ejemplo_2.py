# ejemplo de una clase
class Perro:
    #atributos/constructor
    def __init__(self, raza, tamaño, n):
        self.raza = raza
        self.tamaño = tamaño
        self.nombre = n #se puede poner un nombre distinto
    
    #metodos
    def ladrar(self):
        print("¡Guau guau!")
    
    def romper(self):
        print(f"{self.nombre} te esta rompiendo un almohadon :)")

# crear una instancia/objeto de la clase Perro

p1 = Perro("caniche", "pequeño", "copito")
p2 = Perro("pastor aleman","grande","firulais")

# llamo los distintos metodos
p1.romper()
p1.ladrar()

# imprimir atributos
print(f"te gusta mi perro? se llama {p1.nombre}")
print(f"ah que bien, mi perro se llama {p2.nombre}")
