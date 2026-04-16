#Ejercicio 1 — “Caja del Kiosco”
# Se solicita ingresar nombre de cliente
nombre_cliente = input ("Ingrese su nombre: ")
#En el siguiente paso se valida si contiene solo letras (de la A a la Z) y si tiene al menos un carácter. Si no, se solicita nuevamente.
while not(nombre_cliente.isalpha()):
    nombre_cliente = input ("Error, solo se aceptan letras. Por favor, ingrese su nombre: ")
#Ahora se solicita la cantidad de productos
cantidad_prod = input("Ingrese la cantidad de productos: ")
#En el siguiente paso se valida si contiene solo letras (de la A a la Z), si tiene al menos un carácter y que no sea 0. Si no, se solicita nuevamente.
while not(cantidad_prod.isdigit()) or cantidad_prod == "0":
    cantidad_prod = input ("Error, solo se aceptan numeros enteros positivos. Por favor, ingrese la cantidad de productos: ")
cantidad_prod = int(cantidad_prod)
#Inicializacion de variables para acumular la suma total y con descuentos
suma = 0
precio = 0
total = 0
datos_guardados = ""
#Ciclo for para ingresar productos
for cont in range(1,cantidad_prod+1):
    precio = input("Ingrese precio de producto " + str(cont) + ": ")
    #Validación de precio (es entero y positivo)
    while not(precio.isdigit()):
        precio = input ("Error, solo se aceptan numeros enteros positivos. Por favor, ingrese precio de producto " + str(cont) + ": ")
    precio = int(precio)
    total = total + precio
    tiene_descuento = input("El producto " + str(cont) + " tiene descuento? (S: SI/ N: No) ")
    #Validación de Respuesta S o N
    while not(tiene_descuento == "S" or tiene_descuento == "s" or tiene_descuento == "N" or tiene_descuento == "n"):
        tiene_descuento = input("Error. Ingrese S: SI/ N: No. El producto " + str(cont) + " tiene descuento? ")
    if tiene_descuento.lower() == "s":
        precio_descuento = precio * 0.9
        suma = suma + precio_descuento
    else:
        suma = suma + precio
#Para no perder los precios individuales porque debo imprimir, los guardo en una cadena
    datos_guardados = datos_guardados + "\n" + "Producto " + str(cont) + " - Precio: $" + str(precio) + "   Descuento (S/N):" + str(tiene_descuento)
print() #Imprimo una linea vacía para mejorar la legibilidad
print("Cliente:",nombre_cliente)
print("Cantidad de productos:",cantidad_prod)
print(datos_guardados)
print(f"Total sin descuentos: ${total:.2f}")
print(f"Total con descuentos: ${suma:.2f}")
print()
print(f"Ahorro: ${total - suma:.2f}")
print(f"Promedio por producto: ${suma / cantidad_prod:.2f}")