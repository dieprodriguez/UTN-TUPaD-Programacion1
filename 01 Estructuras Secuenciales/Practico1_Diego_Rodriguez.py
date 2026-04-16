import math
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")
#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre = input("Ingrese su nombre: ")
print (f"Hola {nombre}!")
#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_de_residencia = input("Ingrese su lugar de residencia: ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")
#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = float(input("Ingrese el valor del radio del círculo: "))
area = math.pi * radio ** 2 
perimetro = 2 * math.pi * radio
print(f"El área del circulo de radio {radio} es: {area} y su perímetro es: {perimetro}")
#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese la cantidad de segundos para calcular el equivalente en hs: "))
hora = segundos/3600
print(f"{segundos} segundos equivalen a {hora} horas")
#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingrese un número entero para ver su tabla de multiplicar: "))
print(f"{numero} x 1: {numero*1}")
print(f"{numero} x 2: {numero*2}")
print(f"{numero} x 3: {numero*3}")
print(f"{numero} x 4: {numero*4}")
print(f"{numero} x 5: {numero*5}")
print(f"{numero} x 6: {numero*6}")
print(f"{numero} x 7: {numero*7}")
print(f"{numero} x 8: {numero*8}")
print(f"{numero} x 9: {numero*9}")
print(f"{numero} x 10: {numero*10}")
#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero_7a = int(input("Ingrese un número distinto de cero para operar: "))
numero_7b = int(input("Ingrese otro número distinto de cero para operar: "))
print(f"El resultado de sumar {numero_7a} y {numero_7b} es: {numero_7a + numero_7b}")
print(f"El resultado de restar {numero_7a} y {numero_7b} es: {numero_7a - numero_7b}")
print(f"El resultado de multiplicar {numero_7a} y {numero_7b} es: {numero_7a * numero_7b}")
print(f"El resultado de dividir {numero_7a} por {numero_7b} es: {numero_7a / numero_7b}")
#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"El resultado de su indice de masa corporal (IMC) es: {peso/(altura**2)}")
#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
t_celsius = float(input("Ingrese la temperatura en grados celsuis: "))
print(f"la temperatura {t_celsius} °C es equivalente a: {9/5 * t_celsius + 32} °F")
#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
numero_10a = float(input("Ingrese un número para operar: "))
numero_10b = float(input("Ingrese otro número para operar: "))
numero_10c = float(input("Ingrese otro número para operar: "))
print(f"El promedio de {numero_10a}, {numero_10b} y {numero_10c} es: {(numero_10a + numero_10b + numero_10c)/3}")