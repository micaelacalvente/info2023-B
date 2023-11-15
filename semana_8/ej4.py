class Tiempo():
    def __init__(self, hora, minuto, segundo):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def __str__(self):
        return f"hora: {self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"
        # 15 : 57 : 23

    def cambiar_hora(self, hora=None, minuto=None, segundo=None):
        if hora is not None:
            self.__hora = hora
        if minuto is not None:
            self.__minuto = minuto
        if segundo is not None:
            self.__segundo = segundo
    
    def prueba_tiempo(self):
        #modificar hora
        while True:
            op = int(input("Eligi una opcion: \n1. Mostrar hora \n2. Modificar hora \n3. Salir \n"))
            print()

            if op == 1:
                print(self)
            elif op == 2:
                hora = int(input("Ingresa la hora: "))
                minuto = int(input("Ingrese los minutos: "))
                segundo = int(input("Ingrese los segundos: "))
                self.cambiar_hora(hora, minuto, segundo)
                print("Hora modificada!")

            elif op == 3:
                print("Adios :)")
                break

# crear una instancia / objeto de Tiempo
tiempo_objeto = Tiempo(2, 6, 8)

tiempo_objeto.prueba_tiempo()