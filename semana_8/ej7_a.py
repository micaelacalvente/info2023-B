class Bebida:
    def __init__(self, id, marca, precio, litros):
        self.id = id
        self.marca = marca
        self.precio = precio
        self.litros = litros

class AguaMineral(Bebida):
    def __init__(self, id, marca, precio, litros, origen):
        super().__init__(id, marca, precio, litros)
        self.origen = origen

class Gaseosa(Bebida):
    def __init__(self, id, marca, precio, litros, porcentaje_azucar, promocion=False):
        super().__init__(id, marca, precio, litros)
        self.porcentaje_azucar = porcentaje_azucar
        self.promocion = promocion
        if self.promocion:
            self.precio -= self.precio * 0.10 # Aplicar descuento del 10% si hay promoción

class Almacen:
    def __init__(self):
        self.bebidas = []

    def calcular_precio_total(self):
        return sum(bebida.precio for bebida in self.bebidas)

    def calcular_precio_total_marca(self, marca):
        return sum(bebida.precio for bebida in self.bebidas if bebida.marca == marca)

    def agregar_producto(self, bebida):
        if bebida.id not in [b.id for b in self.bebidas]:
            self.bebidas.append(bebida)
            print("Producto agregado con éxito.")
        else:
            print("El identificador ya existe. No se pudo agregar el producto.")

    def eliminar_producto(self, id):
        self.bebidas = [bebida for bebida in self.bebidas if bebida.id != id]
        print("Producto eliminado con éxito.")

    def mostrar_informacion(self):
        for bebida in self.bebidas:
            if isinstance(bebida, AguaMineral):
                print(f"ID: {bebida.id}, Marca: {bebida.marca}, Precio: {bebida.precio}, Litros: {bebida.litros}, Origen: {bebida.origen}")
            elif isinstance(bebida, Gaseosa):
                print(f"ID: {bebida.id}, Marca: {bebida.marca}, Precio: {bebida.precio}, Litros: {bebida.litros}, Porcentaje de Azúcar: {bebida.porcentaje_azucar}%, Promoción: {'Sí' if bebida.promocion else 'No'}")
            else:
                print(f"ID: {bebida.id}, Marca: {bebida.marca}, Precio: {bebida.precio}, Litros: {bebida.litros}")

# Ejemplo de uso
almacen = Almacen()

agua_mineral = AguaMineral(id=1, marca="Natura", precio=1.5, litros=0.5, origen="Manantial")
gaseosa = Gaseosa(id=2, marca="Coca Cola", precio=2.0, litros=0.75, porcentaje_azucar=10, promocion=True)

almacen.agregar_producto(agua_mineral)
almacen.agregar_producto(gaseosa)

almacen.mostrar_informacion()

print("Precio total:", almacen.calcular_precio_total())
print("Precio total de Coca Cola:", almacen.calcular_precio_total_marca("Coca Cola"))

almacen.eliminar_producto(1)

almacen.mostrar_informacion()