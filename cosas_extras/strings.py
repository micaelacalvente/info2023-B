# Concatenación: se puede concatenar (unir) cadenas utilizando el operador +.
nombre = "Mica"
comision = 6
mensaje = "Mi nombre es " + nombre + " y estoy en la comision " + str(comision)
print(mensaje)

# % (estilo antiguo)
nombre = "Mica"
comision = 6
mensaje = "Mi nombre es %s y estoy en la comision %s " % (nombre, comision)
print(mensaje)

# str.format(): formatea cadenas y reemplaza marcadores de posición por valores.
nombre = "Mica"
comision = 6
mensaje = "Mi nombre es {} y estoy en la comision {} ".format(nombre, comision)
print(mensaje)

# str.format() con nombres de argumentos:
nombre = "Mica"
comision = 6
mensaje = "Mi nombre es {nombre} y estoy en la comision {comision}".format(nombre=nombre, comision=comision)
print(mensaje)

# f-strings (de los mas nuevitos y usados)
nombre = "Mica"
comision = 6
mensaje = f"Mi nombre es {nombre} y estoy en la comision {comision}"
print(mensaje)

# podes incluso formatear cosas mas complejas, .2f indica que el número tenga exactamente dos lugares decimales despues del punto.
precio = 19.33333
mensaje = f"El precio es {precio:.2f} pesos."
print(mensaje)

# str.join() podes unir una lista de strings en uno solo
nombres = ["Mica", "Gera", "Eliseo"]
lista_nombres = ", ".join(nombres)
print(f"Los profes son: {lista_nombres}")


