#Ejercicio 5
#“Escape Room:"La Arena del Gladiador"
#Se solicita ingresar nombre del gladiador. El programa valida que solo use letras, sin símbolos ni espacios vacíos:
gladiador = input ("Ingrese el nombre del Gladiador: ")
while not(gladiador.isalpha()):
    gladiador = input ("Error: solo se permiten letras")
#Inicializo las estadísticas de juego.
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
danio_ataque_pesado = 15
danio_base_enemigo = 12
turno_gladiador = True
while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"Los puntos de vida del gladiador {gladiador} son {vida_gladiador} y tiene {pociones_vida} pociones disponibles.")
    print(f"Los puntos de vida del enemigo son {vida_enemigo}")
    print("\nIngrese una opción: ")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar\n")
    opcion = input("Opción: \n")
    #Compruebo que ingresa opción válida
    while not(opcion.isdigit()) or int(opcion) < 1 or int(opcion) > 3:
        opcion = input ("Error, solo se aceptan números entre 1 y 3. Por favor, ingrese una opción: ")
    opcion = int(opcion)
    match opcion:
        case 1:
            if vida_enemigo < 20:
                vida_enemigo -= (danio_ataque_pesado * 1.5)
                print(f"¡Atacaste al enemigo por {(danio_ataque_pesado*1.5):.2f} puntos de daño!")
            else:
                vida_enemigo -= danio_ataque_pesado
                print(f"¡Atacaste al enemigo por {danio_ataque_pesado} puntos de daño!")
        case 2:
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")
        case 3:
            if pociones_vida > 0:
                vida_gladiador += 30
                pociones_vida -= 1
            else:
                print("¡No quedan pociones!")
    if vida_enemigo > 0:
        vida_gladiador -= danio_base_enemigo
        print("Ahora es turno de tu enemigo:\n")
        print("¡El enemigo te atacó por 12 puntos de daño!\n")
        print("===+++ NUEVO TURNO +++===")
    else:
        print("Le has quitado la vida a tu enemigo\n")
print("---+++ FIN DEL JUEGO +++---")