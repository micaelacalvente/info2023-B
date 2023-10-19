a = int(input("ingrese el primer numero:  "))
b = int(input("ingrese el segundo numero:  "))

operacion = int(input("que tipo de operacion desea hacer? \n1-SUMA\n2-MULTIPLICACION\n3-RESTA\n4-DIVISION\n"))

if operacion == 1:
    print(a+b)
elif operacion == 2:
    print(a*b)
elif operacion == 3:
    print(a-b)
elif operacion == 4:
    print(a//b)
else:
    print("Numero ingresado no válido")