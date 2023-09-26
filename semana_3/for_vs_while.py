# DETERMINAR EL NUMERO MAYOR A 3 NUMEROS INGRESADOS

# # # WHILE
tope = 4
i = 1 # contador
maximo = 0 #acumulador

while (i < tope):
    numero = int(input(f"Ingrese el {i} numero: "))
    if numero > maximo:
        maximo = numero
    
    i+=1
print(f"el valor mas grande ingresado es {maximo}")

# # # FOR
tope = 4
maximo = 0

for i in range(1, tope):
    numero = int(input(f"Ingrese el {i} numero: "))
    if numero > maximo:
        maximo = numero
print(f"el valor mas grande ingresado es {maximo}")
