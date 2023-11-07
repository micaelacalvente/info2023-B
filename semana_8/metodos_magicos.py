class MiClase:
    """
    Esta es la documentación de la clase MiClase comision 6.
    """
    
    def __init__(self, valor):
        self.valor = valor

    def __del__(self):
        print(f"Instancia de MiClase con valor {self.valor} está siendo destruida")

    def __str__(self):
        return f"Instancia de MiClase con valor {self.valor}"

    def __repr__(self):
        return f"MiClase({self.valor})"
'''
# Obtener la documentación de la clase
print(MiClase.__doc__)
'''
# Crear una instancia de la clase
obj = MiClase(42)
'''
# Obtener el nombre de la clase
print(obj.__class__.__name__)'''

# Imprimir la representación de la instancia
print(repr(obj))

# Imprimir la instancia (llama a __str__)
print(obj)

'''# Destruir la instancia (llama a __del__)
del obj

# Verificar el módulo al que pertenece la clase
print(MiClase.__module__)'''
