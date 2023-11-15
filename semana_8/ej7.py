class Almacen():
    def __init__(self):
        self.lista_bebidas = []

    def agregar_bebida(self, bebida):
        if not isinstance(bebida, (Agua, Gaseosa)):
            print("Valor incorrecto, solo se admiten bebidas")
            return

        for b in self.lista_bebidas:
            if b.id == bebida.id:
                print("ID ya existente")
                return

        self.lista_bebidas.append(bebida)
        print("Bebida agregada correctamente")

    def eliminar_bebida(self, id):
        for b in self.lista_bebidas:
            if b.id == id:
                self.lista_bebidas.remove(b)
                print("Bebida eliminada correctamente")
                return
        print("No se encontró la bebida con el ID especificado")

    def obtener_total(self, marca=None):
        total = 0
        for b in self.lista_bebidas:
            if marca is None or (marca is not None and b.marca == marca):
                total += b.get_precio()
        return total

    def ver_info(self):
        for b in self.lista_bebidas:
            b.ver_info()
            print("-" * 30)

class Bebida():
    def __init__(self, id, litros, precio, marca):
        self.id = id
        self.litros = litros
        self.precio = precio
        self.marca = marca

    def get_precio(self):
        return self.precio

    def ver_info(self):
        print(f"ID: {self.id}")
        print(f"LITROS: {self.litros}")
        print(f"PRECIO: {self.precio}")
        print(f"MARCA: {self.marca}")

class Agua(Bebida):
    def __init__(self, id, litros, precio, marca, origen):
        super().__init__(id, litros, precio, marca)
        self.origen = origen

    def ver_info(self):
        super().ver_info()
        print(f"ORIGEN: {self.origen}")

class Gaseosa(Bebida):
    def __init__(self, id, litros, precio, marca, p_azucar, promocion):
        super().__init__(id, litros, precio, marca)
        self.p_azucar = p_azucar
        self.promocion = promocion
        self.descuento = 0.1

    def get_precio(self):
        if self.promocion:
            return self.precio * (1 - self.descuento)
        return self.precio

    def ver_info(self):
        super().ver_info()
        print(f"PORCENTAJE DE AZUCAR: {self.p_azucar} %")
        print(f"TIENE DESCUENTO: {'Si' if self.promocion else 'No'}")
        print(f"DESCUENTO: {self.descuento} %")

# Instancia/Objeto del almacén
a = Almacen()

# Inicio del programa
while True:
    print("\n--- Menú ---")
    print("1. Agregar producto")
    print("2. Calcular precio de todas las bebidas")
    print("3. Calcular precio total de una marca de bebida")
    print("4. Eliminar un producto")
    print("5. Mostrar información")
    print("0. Salir")

    opcion = input("Ingrese el número de la opción que desea ejecutar: ")
    print()
    if opcion == "1":
        tipo_bebida = input("Ingrese el tipo de bebida (agua/gaseosa): ")
        id = input("Ingrese el ID de la bebida: ")
        litros = float(input("Ingrese la cantidad de litros: "))
        marca = input("Ingrese la marca: ")
        precio = float(input("Ingrese el precio: "))

        if tipo_bebida == "agua":
            origen = input("Ingrese el origen del agua mineral: ")
            bebida = Agua(id, litros, precio, marca, origen)
        elif tipo_bebida == "gaseosa":
            p_azucar = float(input("Ingrese el porcentaje de azúcar: "))
            promocion = input("Tiene descuento (si/no): ")
            bebida = Gaseosa(id, litros, precio, marca, p_azucar, promocion.lower() == "si")
        else:
            print("Tipo de bebida no válido")
            continue

        a.agregar_bebida(bebida)

    elif opcion == "2":
        total = a.obtener_total()
        print(f"El precio total de todas las bebidas en el almacén es: {total:.2f}")

    elif opcion == "3":
        marca = input("Ingrese la marca de la bebida: ")
        total = a.obtener_total(marca)
        print(f"El precio total de las bebidas de la marca {marca} es: {total:.2f}")

    elif opcion == "4":
        id = input("Ingrese el ID del producto que desea eliminar: ")
        a.eliminar_bebida(id)

    elif opcion == "5":
        a.ver_info()

    elif opcion == "0":
        print("Nos vemos! :)")
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
