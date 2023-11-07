class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular de la cuenta: {self.titular}")
        print(f"Saldo de la cuenta: {self.cantidad:.2f} euros")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

# Ejemplo de uso
cuenta = Cuenta("Juan Pérez", 1000.0)
cuenta.mostrar()
'''print()
print("Me pagaron el sueldo :)")
cuenta.ingresar(500.0)
cuenta.mostrar()
print()
print("Tuve que pagar el alquiler :(")
cuenta.retirar(200.0)
cuenta.mostrar()'''

print()
print("Me pagaron el sueldo :)")
ing = float(input("Ingresa el monto a depositar: "))
cuenta.ingresar(ing)
cuenta.mostrar()

print()
print("Aumento el alquiler :(")
ret = float(input("Ingresa el monto a retirar: "))
cuenta.retirar(ret)
cuenta.mostrar()
