'''Ejercicio 3: Triángulo
Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos, imprimir el
valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero,
isósceles o escaleno).'''

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def mayor(self):
        print("El valor del lado mayor es: ")
        print(max(self.lado1, self.lado2, self.lado3))
    
    def tipo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es un triangulo equilatero")
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:
            print("Es un triangulo escaleno")
        else:
            print("Es un triangulo isoceles")

'''t = Triangulo(2, 1, 3)
t.mayor()
t.tipo()'''

print("Fabrica de triangulos :)")
lado1 = int(input("Ingresa el primer lado: "))
lado2 = int(input("Ingresa el segundo lado: "))
lado3 = int(input("Ingresa el tercer lado: "))

t = Triangulo(lado1, lado2, lado3)
t.mayor()
t.tipo()