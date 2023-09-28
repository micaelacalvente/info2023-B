'''11-Crear una lista con los nombres de tres animales y agregar una cuarta animal
al principio de la lista. Mostrar la lista resultante.'''

animales = ["perro", "gato", "aguara guazu"]
# inserta un animal al principio de la lista
animales.insert(0, "carpincho")
# inserta un animal al final de la lista
animales.append("chancho")
print(animales)
# ordena los animales de menor a mayor
animales.sort()
print(animales)