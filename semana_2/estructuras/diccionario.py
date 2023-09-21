# profes { }

profes = {"Micaela": "profe", "Gera": "mentor", "Eliseo": "mentor"}
# clave = unica : valor = cualquier tipo de dato
print(profes)

#imprimir el valor de una clave
print(profes["Micaela"])

#cambiar valor de clave
profes["Micaela"] = 25

print(profes.keys())
print(profes.values())
print(profes.items())

#elimina el ultimo item
profes.popitem()
print(profes)

#elimina un item en especifico
profes.pop("Micaela")
print(profes)