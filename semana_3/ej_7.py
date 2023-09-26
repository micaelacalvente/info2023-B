'''7-Escribe un programa que pida al usuario una palabra y determine si es un
palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
izquierda).'''

palabra = input("ingresa una palabra: ").lower()
es_palindromo = True

for letra in range(len(palabra)):
    if palabra[letra] != palabra[-letra-1]:
        es_palindromo = False
        break

if es_palindromo:
    print(palabra, "es palindromo")
else:
    print(palabra, "no es palindromo")