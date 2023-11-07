class ClasePadre():
    def hola(self):
        print("hola soy la clase padre")

class ClaseHijaUno(ClasePadre):
    def hola(self):
        print("hola soy la clase hija 1")

class ClaseHijaDos(ClasePadre):
    def hola(self):
        print("hola soy la clase hija 2")

a = ClaseHijaUno()
b = ClaseHijaDos()

a.hola()