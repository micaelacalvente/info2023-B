# WHILE // MIENTRAS

# while (mientras) [condicion/condiciones] es verdadera:
       # ACCION

#este codigo se ejecuta repetitivamente hasta que la condicion sea false

tope = int(input("ingrese un numero: "))
i = 2 # acumulador
#loop infinito
while (i < tope):
    print(i)
    break #romper

# uso de contador
while (i < tope):
    print(i)
    i += 1 #i = i + 1

c = 0
while c <= 5:
    c += 1
    print("c vale", c)
else:
    print("se ha completado la iteracion")

# parametro end
# # sino por defecto hace un salto de linea
print(1, end="-")
print(2, end="-")
print(3, end="-")

seguir = "SI"
#primer bucle
while (seguir == "SI"):
    tope = int(input("ingrese un numero: "))
    
    i = 1
    # segundo bucle
    while (i <= tope):
        print(i, end=" ")
        i += 1
    print("\nFIN") #\n new line/nueva linea # \t tabulacion
    seguir = input("quieres seguir de nuevo? SI/NO ").upper()

print("chau")



