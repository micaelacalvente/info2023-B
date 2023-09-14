# Crea un programa que pida al usuario el radio de un círculo y muestre su
# diámetro, su circunferencia y su área.
# Supón que pi es aproximadamente 3.14159.

radio = float(input("Introduce el valor del radio: "))
diametro = radio * 2
pi = 3.14159
circunferencia = 2 * pi * radio
area = pi * radio**2
print("el diametro es", diametro)
print("la circunferencia es", circunferencia)
print("el área es", area)