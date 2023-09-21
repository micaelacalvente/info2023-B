"""10-Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la
lista. Mostrar la lista resultante."""

# metodo 1
frutas = ["Banana", "Pera", "Manzana"]
del frutas[1]
print(frutas)

# metodo 2
frutas2 = ["Banana", "Pera", "Manzana"]
frutas2.remove("Pera")
print(frutas2)

# metodo 3
frutas3 = ["Banana", "Pera", "Manzana"]
frutas3.pop(1)
print(frutas3)