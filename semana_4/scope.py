# AMBITO // SCOPE

# Global Scope / Ambito Global / Variable Global
x = 0
def funcion():
    # Enclosed Scope
    x = 1
    def funcion_interna():
        # Local Scope / Ambito Local / Variable Local
        x = 2
        print(f"Local x={x}")
    funcion_interna()
    print(f"Enclosed x={x}")

funcion()
print(f"Global x={x}")

# LOCALS() devuelve un diccionario que contiene todas las variables locales

def ejemplo_locals():
    x = 12 
    y = "mica"
    locals_var = locals()
    return locals_var

print(ejemplo_locals())

# GLOBALS() devuelve un diccionario que contiene todas las variables globales

x = True
y = "info"

def ejemplo_globals():
    globals_var = globals()
    return globals_var

print(ejemplo_globals())