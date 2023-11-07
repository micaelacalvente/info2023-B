# Dentro de una función se pueden crear más funciones
# Las funciones pueden retornar funciones
# Las funciones se pueden pasar como argumentos a otras funciones

def mi_decorador(funcion):
    def nueva_funcion(a,b):
        print("Funcion suma ingresa")
        c = funcion(a, b)
        print(f"Resultado suma: {c}")
        print("Funcion suma sale")
        return c
    return nueva_funcion

@mi_decorador
def suma(a,b):
    return a + b

suma(2, 3)