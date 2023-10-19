# definir PIN SECRETO
pin_secreto = '1234'

# inicializar el contador de intentos

intentos = 3

# iniciar bucle
while intentos > 0:
    # solicitar al usuario que ingrese el PIN
    pin_ingresado = input("Ingresa el PIN: ")

    # verificar
    if pin_ingresado == pin_secreto:
        print("login correcto")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"INCORRECTO, te quedan {intentos} intentos")
        else:
            print("LLAMANDO A LA POLICIA")