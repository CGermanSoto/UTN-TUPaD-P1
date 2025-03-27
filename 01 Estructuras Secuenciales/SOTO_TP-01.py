import math

# 1
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

# 3
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
pais = input("Ingrese su país de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}.")

# 4
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
radio = float(input("Ingrese el radio del círculo a calcular: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# 5
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# 6
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
multiplicando = int(input("Ingrese el número a multiplicar: "))
multiplicador = int(input("Ingrese hasta qué número quiere que se multiplique (inicia en 0): "))
for i in range(multiplicador + 1):
    resultado = multiplicando * i
    print(f"{multiplicando} x {i} = {resultado}")

# 7
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero_uno = int(input("Ingrese un número: "))
numero_dos = int(input("Ingrese otro: "))
mult = numero_uno * numero_dos
div = numero_uno / numero_dos
sum = numero_uno + numero_dos
rest = numero_uno - numero_dos
print(f"Multiplicación: {numero_uno} x {numero_dos} = {mult}")
print(f"División: {numero_uno} / {numero_dos} = {div:.0f}")
print(f"Suma: {numero_uno} + {numero_dos} = {sum}")
print(f"Resta: {numero_uno} - {numero_dos} = {rest}")

# 8
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
# 𝐼𝑀𝐶 = peso en kg / (altura en m)²
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura ** 2)
print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")

# 9
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# Temperatura en Fahrenheit = (9/5) * Temperatura en Celsius + 32
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")

# 10
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
num_uno = float(input("Ingrese el primer número: "))
num_dos = float(input("Ingrese el segundo número: "))
num_tres = float(input("Ingrese el tercer número: "))
promedio = (num_uno + num_dos + num_tres) / 3
print(f"El promedio de los tres números es: {promedio:.2f}")
