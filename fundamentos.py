# Variables y tipos de datos

# Asignación/solicitud de los valores de las variables
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura: "))
eres_estudiante = input("¿Eres estudiante? (1=Sí/Otro=No): ")
es_estudiante = "Sí" if eres_estudiante == "1" else "No"

# Imprimir el contenido de las variables
print("Mi nombre es", nombre)
print("Tengo", edad, "años")
print("Mi altura es", altura, "metros")
print("¿Soy estudiante?", es_estudiante)

# Estructuras de control: condicionales

if edad >= 18:  # Si la edad es mayor o igual a 18
    print("Soy mayor de edad")
else:
    print("Soy menor de edad")

# Estructuras de control: bucles

# Bucle while
iteraciones =  = int(input("Ingresa el número de iteraciones: "))
contador = 0
while contador < iteraciones:
    print("El contador es", contador)
    contador += 1

# Bucle for
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta comer", fruta)

# Funciones

# Definición de una función
def calcular_area_rectangulo(base, altura):
    area = base * altura / 2
    return area

# Llamada a la función
base_rectangulo = int(input("Ingresa la base del rectángulo: "))
altura_rectangulo = int(input("Ingresa la altura del rectángulo: "))
area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
print("El área del rectángulo es:", area_rectangulo)

a = int(input("Ingresa la base del rectángulo: "))
b = int(input("Ingresa la altura del rectángulo: "))
area2 = calcular_area_rectangulo(a, b)
print("El área del rectángulo es:", area2)

# Módulos

# Importar el módulo math
import math

# Utilizar una función del módulo math
valor = int(input("Ingresa el número a calcular su raíz cuadrada: "))
raiz_cuadrada = math.sqrt(valor)
print("La raíz cuadrada de 25 es:", raiz_cuadrada)
