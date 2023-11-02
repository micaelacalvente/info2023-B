# DEFINIR CLASE/MOLDE (ESTRUCTURA)
class Estudiante:
    #definir atributos/constructor
    def __init__(self, nombre, edad, comision="seis"):
        self.nombre = nombre
        self.edad = edad
        self.comision = comision
    
    #definir metodos
    def saludar(self):
        return f"Hola! mi nombre es {self.nombre} tengo {self.edad}"

e1 = Estudiante("Micaela", 25)
print(e1.saludar())
print(e1.nombre)
print(e1.edad)
print(e1.comision)


print(isinstance(e1, Estudiante))

'''# METODO 2

# CREANDO LOS OBJETOS POR PANTALLA
class Estudiante:
    #definir atributos/constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #definir metodos
    def saludar(self):
        return f"Hola! mi nombre es {self.nombre} tengo {self.edad}"

# crear una lista para almacenar estudiantes
estudiantes = []

#solicitar num de estudiantes que queres guardar
num_estudiantes = int(input("Ingrese el numero de estudiantes: "))

# utilizamos un bucle para agregar objetos
for e in range(num_estudiantes):
    nombre = input(f"Ingrese el nombre del estudiante {e + 1}: ")
    edad = int(input(f"Ingrese la edad del estudiante {e + 1}: "))
    estudiante = Estudiante(nombre, edad)
    estudiantes.append(estudiante)

#muestro los nombres de los objetos
nombres_estudiantes = [estudiante.nombre for estudiante in estudiantes]
print(nombres_estudiantes)'''