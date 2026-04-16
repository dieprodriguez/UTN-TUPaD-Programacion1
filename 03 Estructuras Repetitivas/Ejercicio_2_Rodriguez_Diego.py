#Ejercicio 2 — “Acceso al Campus y Menú Seguro”
#Se definen credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 1
#Se solicita ingresar nombre de usuario y clave:
#Se crea un ciclo de 3 intentos que se corta si se validan usuario y contraseña
while intentos <= 3:
    usuario = input ("Ingrese su nombre de usuario: ")
    clave = input ("Ingrese clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Intento "+str(intentos)+"/3 - Usuario: " + str(usuario))
        print("Clave: ", clave)
        print("Acceso concedido.") 
        print()
        break
    else:
        print("Intento "+str(intentos)+"/3 - Usuario: " + str(usuario))
        print("Clave: ", clave)
        print("Error. Credenciales inválidas.")
        print()
        intentos += 1
#Para mostrar el menú compruebo: si cumple el ciclo while es porque intentó 3 veces o fue acceso concedido
if intentos-1 == 3:
    print("Cuenta Bloqueada")
else:
    #Inicializo la variable opcion en cero para que al menos haga un ciclo
    opcion = 0
    while opcion != 4:
        print("Ingrese una opción: ")
        print("1. Ver estado de inscripción ")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir ")
        print()
        opcion = input("Opción: ")
        while not(opcion.isdigit()) or int(opcion) < 1 or int(opcion) > 4:
            opcion = input ("Error, solo se aceptan números entre 1 y 4. Por favor, ingrese una opción: ")
        opcion = int(opcion)
        match opcion:
            case 1:
                print("Inscripto.")
            case 2:
                #Inicializo las variables para que inicie el while
                nueva_clave = 0
                nueva_clave_conf = 1
                #El ciclo repetirá mientras las claves sean diferentes
                while nueva_clave != nueva_clave_conf:
                    nueva_clave = input ("Ingrese una nueva clave (debe tener 6 caracteres): ")
                    nueva_clave_conf = input ("Confirme su neva clave: ")
                    #Compruebo con condicional que las claves sean iguales y su longitud
                    if nueva_clave == nueva_clave_conf and len(nueva_clave) == 6:
                        clave = nueva_clave
                    elif (nueva_clave == nueva_clave_conf and len(nueva_clave) != 6):
                        print("La nueva clave debe tener 6 dígitos.")
                        nueva_clave = 0 #Me aseguro que sean diferentes
                        nueva_clave_conf = 1
                    elif (nueva_clave != nueva_clave_conf):
                        print ("Las claves deben coincidir.")
            case 3:
                print("No eres responsable de la programación que recibiste en el pasado, pero eres el único responsable de actualizar tu código hoy para construir el sistema que quieres ser mañana.")
            case 4:
                print("Gracias por usar el sistema")