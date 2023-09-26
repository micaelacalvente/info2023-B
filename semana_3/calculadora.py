print("Bienvenida")

seguir = "SI"
while seguir == "SI":
    print("Elija una opcion:")
    print("1-SUMA")
    print("2-RESTA")
    print("3-MULTIPLICAR")
    print("4-DIVIDIR")
    print("5-SALIR")
    op = int(input())

    if op == 5:
        seguir == "NO"
    else:
        n1 = int(input("Ingrese el primer numero: "))
        n2 = int(input("Ingrese el segundo numero: "))

    if op == 1:
        resultado = n1 + n2
    elif op == 2:
        resultado = n1 - n2
    elif op == 3:
        resultado = n1 * n2
    elif op == 4:
        resultado = n1 // n2
    else:
        resultado = 0
    print(f"el resultado es: {resultado} ")
    seguir = input("queres seguir? SI/NO\n").upper()

print("Gracias por usar la calcu :)")