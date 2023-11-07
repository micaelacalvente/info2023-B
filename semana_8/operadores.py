class MiClase:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, other):
        resultado = self.valor + other.valor
        return MiClase(resultado)

objeto1 = MiClase(5)
objeto2 = MiClase(4)
resultado = objeto1 + objeto2 #llama a objeto1.__add__(objeto2)
print(resultado.valor)