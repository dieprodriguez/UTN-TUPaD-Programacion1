#Ejercicio 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga 
# “Es mayor de edad”.
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
#Ejercicio 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga 
# “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
#Ejercicio 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje 
# "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
num_par = int(input("Ingrese un número par: "))
if num_par % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
#Ejercicio 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# (Niño/a: menor de 12 años; Adolescente: mayor o igual que 12 años y menor que 18 años; 
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años; Adulto/a: mayor o igual que 30 años)
edad_categoria = int(input("Ingrese su edad: "))
if edad_categoria < 12:
    print("Usted es niño/a")
elif edad_categoria >= 12 and edad_categoria < 18:
    print("Usted es adolescente")
elif edad_categoria >= 18 and edad_categoria < 30:
    print("Usted es adulto/a joven")
elif edad_categoria >= 30:
    print("Usted es adulto/a")
#Ejercicio 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"
clave = input("Ingrese su contraseña: ")
if len(clave) >= 8 and len(clave) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#Ejercicio 6) Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en kilovatios (kWh) e indique la categoría 
# del consumo según el siguiente criterio (Menor que 150 kWh: “Consumo bajo”; Entre 150 y 300 kWh (inclusive): “Consumo medio”; 
# Mayor que 300 kWh: “Consumo alto”) Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga: 
# “Considere medidas de ahorro energético”. El programa debe imprimir por pantalla la categoría correspondiente.
consumo = int(input("Ingrese su consumo mensual de energía eléctrica. Por favor, en kilovatios (kwh): "))
if consumo < 150:
    print("Consumo bajo.")
elif consumo >= 150 and consumo <= 300:
    print("Consumo medio.")
elif consumo >= 300 and consumo <= 500:
    print("Consumo alto.")
elif consumo > 500:
    print("Consumo alto.")
    print("Considere medidas de ahorro energético.")
#Ejercicio 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, 
# dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase = input ("Ingrese una frase o palabra: ")
es_vocal = frase[-1].lower()
if es_vocal == "a" or es_vocal == "e" or es_vocal == "i" or es_vocal == "o" or es_vocal == "u" or es_vocal == "á" or es_vocal == "é" or es_vocal == "í" or es_vocal == "ó" or es_vocal == "ú":
    print(f"{frase}!")
else:
    print(f"{frase}")
#Ejercicio 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
nombre_ej8 = input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opción según desee que:\n1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro."))
match opcion:
    case 1:
        print(f"{nombre_ej8.upper()}")
    case 2:
        print(f"{nombre_ej8.lower()}")
    case 3:
        print(f"{nombre_ej8.title()}")
#Ejercicio 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías
#según la escala de Richter e imprima el resultado por pantalla.
magnitud_terremoto = float(input("Ingrese la magnitud de un terremoto: "))
if magnitud_terremoto < 3:
    print("El terremoto es Muy leve (imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("El terremoto es Leve (ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("El terremoto es Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("El terremoto es Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("El terremoto es Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("El terremoto es Extremo (puede causar graves daños a gran escala)")
#Ejercicio 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input ("Indique en que hemisferio se encuentra. Usando N para norte y S para sur: ")
mes = int(input ("Indique, con formato número, que mes del año es: "))
dia = int(input ("Indique día del año es: "))
if hemisferio.lower() == "n":
    if (mes == 12 and dia >= 21 and dia <=31) or (mes == 1 and dia >= 1 and dia <=31) or (mes == 2 and dia >= 1 and dia <=29) or (mes == 3 and dia >= 1 and dia <=20):
        print("Ud se encuentra en Invierno")
    elif (mes == 3 and dia >= 21 and dia <=31) or (mes == 4 and dia >= 1 and dia <=30) or (mes == 5 and dia >= 1 and dia <=31) or (mes == 6 and dia >= 1 and dia <=20):
        print("Ud se encuentra en Primavera")
    elif (mes == 6 and dia >= 21 and dia <=31) or (mes == 7 and dia >= 1 and dia <=31) or (mes == 8 and dia >= 1 and dia <=31) or (mes == 9 and dia >= 1 and dia <=20):
        print("Ud se encuentra en Verano")
    elif (mes == 9 and dia >= 21 and dia <=30) or (mes == 10 and dia >= 1 and dia <=31) or (mes == 11 and dia >= 1 and dia <=31) or (mes == 12 and dia >= 1 and dia <=20):
        print("Ud se encuentra en Otoño")
elif  hemisferio.lower() == "s":
    if (mes == 12 and dia >= 21 and dia <=31) or (mes == 1 and dia >= 1 and dia <=31) or (mes == 2 and dia >= 1 and dia <=29) or (mes == 3 and dia >= 1 and dia <=20):
        print("Ud se encuentra en Verano")
    elif (mes == 3 and dia >= 21 and dia <=31) or (mes == 4 and dia >= 1 and dia <=30) or (mes == 5 and dia >= 1 and dia <=31) or (mes == 6 and dia >= 1 and dia <=20):
        print("Ud se encuentra en Otoño")
    elif (mes == 6 and dia >= 21 and dia <=31) or (mes == 7 and dia >= 1 and dia <=31) or (mes == 8 and dia >= 1 and dia <=31) or (mes == 9 and dia >= 1 and dia <=20):
        print("Ud se encuentra en Invierno")
    elif (mes == 9 and dia >= 21 and dia <=30) or (mes == 10 and dia >= 1 and dia <=31) or (mes == 11 and dia >= 1 and dia <=31) or (mes == 12 and dia >= 1 and dia <=20):
        print("Ud se encuentra en Primavera")