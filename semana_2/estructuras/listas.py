# LISTAS [ ]
lista = ["Info", 6, 2023, True, False, 3.14]
#imprimir todos los elementos de una lista
print(lista)

#acceder a elemento de una lista
print(lista[0])
print(lista[5])
#acceder a elementos de una lista en un rango
print(lista[1:4])
print(lista[:4])
print(lista[0:])

#acceder al ultimo elemento
print(lista[5])
print(lista[-1])

#modificar elementos de una lista
lista[0] = "info"

#agregar un elemento a la lista
lista.append(6)

#eliminar elemento de la lista
lista.remove(6)

#agregar un elemento en una posición especifica
lista.insert(2, "hola")

#agrega elementos al final de la lista
lista.extend(["nuevo", "elemento"])

#elimina un elemento de la lista en una posicion especifica y lo devuelve
print(lista.pop(3))

#elimina todos los elementos de la lista
print(lista.clear())

#devuelve la posicion de la primera aparicion de un elemento en una lista en un rango indicado
# tambien sirve con strings
numeros = [1, 2, 6, 8, 9, 6, 6, 5]
print(numeros.index(6, 3, 8))
#nombre_lista.index(numero que busco, donde empiezo a buscar, donde termina la busqueda)

# devuelve cuantas veces aparece el elemento en la lista
print(numeros.count(6))

# ordena los elementos de menor a mayor
texto = ["a", "d", "c", "b"]
texto.sort()
texto.sort(reverse=True) #reverse=True ordena de mayor a menor



