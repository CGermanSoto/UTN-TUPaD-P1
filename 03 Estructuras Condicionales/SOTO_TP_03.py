# 1) Solicitar la edad del usuario. Si el usuario es mayor de 18 años, mostrar “Es mayor de edad”.
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

# 2) Solicitar la nota del usuario. Si la nota es mayor o igual a 6, mostrar “Aprobado”; en caso contrario “Desaprobado”.
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Permitir ingresar solo números pares. Si el usuario ingresa un número par, imprimir "Ha ingresado un número par"; 
# en caso contrario, imprimir "Por favor, ingrese un número par".
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

import random
import statistics

# 4) Solicitar al usuario su edad e imprimir a qué categoría pertenece.
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("4) Niño/a")
elif 12 <= edad < 18:
    print("4) Adolescente")
elif 18 <= edad < 30:
    print("4) Adulto/a joven")
else:
    print("4) Adulto/a")

# 5) Solicitar una contraseña y validar que tenga entre 8 y 14 caracteres.
contrasena = input("Ingrese una contraseña (8 a 14 caracteres): ")
if 8 <= len(contrasena) <= 14:
    print("5) Ha ingresado una contraseña correcta")
else:
    print("5) Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Generar una lista con 50 números aleatorios entre 1 y 100 y comparar su moda, mediana y media.
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

try:
    moda = statistics.mode(numeros_aleatorios)
except statistics.StatisticsError:
    moda = "No existe una moda única"  # En caso de empate
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)

print("6) Números aleatorios:", numeros_aleatorios)
print("6) Moda:", moda)
print("6) Mediana:", mediana)
print("6) Media:", media)

# Comparar para determinar sesgo.
# Se asume: si la secuencia es: moda < mediana < media  => sesgo positivo;
# si la secuencia es: media < mediana < moda => sesgo negativo;
# en otro caso, se considera sin sesgo.
if isinstance(moda, int):  # Solo se compara si hay un único valor de moda.
    if moda < mediana < media:
        print("6) Sesgo positivo")
    elif media < mediana < moda:
        print("6) Sesgo negativo")
    else:
        print("6) No hay sesgo")
else:
    print("6) No se puede determinar el sesgo de forma única debido a la moda múltiple")

# 7) Solicitar una frase o palabra y, si termina con vocal, añadirle un signo de exclamación.
texto = input("7) Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"
if texto and texto[-1] in vocales:
    texto += "!"
print("7)", texto)

# 8) Solicitar el nombre y una opción numérica para cambiar el formato del nombre.
nombre = input("8) Ingrese su nombre: ")
print("8) Opciones:\n    1. Nombre en MAYÚSCULAS.\n    2. Nombre en minúsculas.\n    3. Nombre con la primera letra en mayúscula.")
opcion = input("8) Ingrese 1, 2 o 3 según su opción: ")
if opcion == "1":
    print("8)", nombre.upper())
elif opcion == "2":
    print("8)", nombre.lower())
elif opcion == "3":
    print("8)", nombre.title())
else:
    print("8) Opción no válida.")

# 9) Solicitar la magnitud de un terremoto y clasificarla según la escala de Richter.
magnitud = float(input("9) Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("9) Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("9) Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("9) Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("9) Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("9) Muy Fuerte (puede causar daños significativos)")
else:
    print("9) Extremo (puede causar graves daños a gran escala)")

# 10) Determinar la estación del año en función del hemisferio, mes y día ingresados.
# Se utilizará la tabla:
# Para hemisferio norte:
#   - 21 dic - 20 mar: Invierno
#   - 21 mar - 20 jun: Primavera
#   - 21 jun - 20 sep: Verano
#   - 21 sep - 20 dic: Otoño
# Para hemisferio sur, las estaciones se invierten:
#   - 21 dic - 20 mar: Verano
#   - 21 mar - 20 jun: Otoño
#   - 21 jun - 20 sep: Invierno
#   - 21 sep - 20 dic: Primavera

hemisferio = input("10) Ingrese el hemisferio (N para norte, S para sur): ").upper()
mes = int(input("10) Ingrese el mes (numérico, 1-12): "))
dia = int(input("10) Ingrese el día: "))

# Convertir mes y día a un número de "día del año" (asumir año no bisiesto)
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dia_del_ano = sum(dias_por_mes[:mes-1]) + dia

# Función para determinar estación en hemisferio norte usando día_del_anio
def estacion_norte(dia_ano):
    # Se usan los siguientes rangos:
    # Invierno: 355 - 365 y 1 - 80 (del 21 dic al 20 mar; 20 mar es día 80)
    # Primavera: 81 - 171 (21 mar a 20 jun)
    # Verano: 172 - 263 (21 jun a 20 sep)
    # Otoño: 264 - 354 (21 sep a 20 dic)
    if dia_ano >= 355 or dia_ano <= 80:
        return "Invierno"
    elif 81 <= dia_ano <= 171:
        return "Primavera"
    elif 172 <= dia_ano <= 263:
        return "Verano"
    else:  # 264 a 354
        return "Otoño"

# Para hemisferio sur, las estaciones son las opuestas
def estacion_sur(estacion_norte_val):
    opposiciones = {
        "Invierno": "Verano",
        "Primavera": "Otoño",
        "Verano": "Invierno",
        "Otoño": "Primavera"
    }
    return opposiciones.get(estacion_norte_val, "Desconocido")

est_norte = estacion_norte(dia_del_ano)
if hemisferio == "N":
    print("10) Estación:", est_norte)
elif hemisferio == "S":
    print("10) Estación:", estacion_sur(est_norte))
else:
    print("10) Hemisferio no reconocido.")
