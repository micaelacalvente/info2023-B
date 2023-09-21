# TUPLAS ( )
tupla = (1, 2, 1, 1, "no", True, 1.2, 2, 3)

#empaquetar
tupla1 = (1, 2, 3)

#desempaquetar
uno, dos, tres = tupla1
print(uno, dos, tres)

# indexacion
tupla[2:3]

numeros = (1,1,1,1,0,0,0)
#retorna el indice mas pequeño del elemento x
numeros.index(0)

#cuenta el numero de veces que aparece el elemento en la tupla
numeros.count(0)

# conversion de tupla a lista
t = ("hola", "como", "estas")
lista_nueva = list(t)

# conversion de lista a tupla
tupla_denuevo = tuple(lista_nueva)