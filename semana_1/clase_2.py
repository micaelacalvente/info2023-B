###### CONCEPTOS TEORICOS ######
# con el numeral escribo comentarios

# # # TIPOS DE DATOS

# entero - int - integrer
numero_entero = 5
print(type(numero_entero))

# decimal - float - flotante
numero_decimal = 5.2
#imprime el tipo de dato que esta almacenado en la variable numero_decimal
print(type(numero_decimal))

# cadena de caracteres / string / str
#van con comillas
nombre = 'Micaela'
print(type(nombre))

# logico / booleano
bool_v = True #verdadero
bool_f = False #falso
print(f'La variable bool_f contiene el valor: {bool_f} y es del tipo {type(bool_f)}')
print('La variable bool_f contiene el valor:', bool_f, 'y es del tipo', type(bool_f))


# # # OPERADORES MATEMATICOS
n1 = int(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
# int() transforma todo lo que hay entre parentesis en un numero entero

suma = n1 + n2
resta = n1 + n2
multiplicacion = n1 * n2
division = n1 / n2 # n1 / n2 devuelve como resultado un float y n1 // n2 devuelve un int
modulo = n1 % n2 # retorna el resto de la division
potencia = n1 ** n2

# # # OPERADORES DE COMPARACION
# retornan un valor logico (True / False)
v1 = n1 > n2 # mayor que
v2 = n1 >= n2 # mayor o igual que
v3 = n1 < n2 # menor que
v4 = n1 <= n2 # menor o igual que
v5 = n1 == n2 # igual
v6 = n1 != n2 #distinto
#actuan sobre cualquier tipo de dato y retornan un valor logico (V/F)


# # # OPERADORES LOGICOS
logica1 = True
logica2 = False

logica1 and logica2 #resultado = False
logica1 or logica2 #resultado = True
not logica1 #resultado = False

#actuan sobre valores logicos y retornan un valor logico (V/F)