"""19-Escribe un programa que solicite al usuario un número decimal y luego
imprima la parte entera y decimal por separado."""

# solucion 1
decimal = float(input("ingrese un numero decimal: "))
parte_int = int(decimal)
parte_float = decimal - parte_int

print(f"parte entera {parte_int} y parte decimal {parte_float}")

# solucion 2
numero = float(input("ingresa un num: "))
numero_str = str(numero).split('.')
print(f'El numero {numero} esta compuesto por {numero_str[0]} un punto y {numero_str[1]} ')

