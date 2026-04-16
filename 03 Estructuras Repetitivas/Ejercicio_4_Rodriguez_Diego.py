#Ejercicio 4
#“Escape Room: La Bóveda”
#Definimos las variables que se proponen como iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0 
alarma = False
codigo_parcial = ""
#Se solicita ingresar nombre del agente:
agente = input ("Ingrese el nombre del agente: ")
#En el siguiente paso se valida si contiene solo letras (de la A a la Z) y si tiene al menos un carácter. Si no, se solicita nuevamente.
while not(agente.isalpha()):
    agente = input ("Error, solo se aceptan letras. Por favor, ingrese el nombre del agente: ")
#Inicializo las variables que voy a usar para contar las veces que fuerza la cerradura
veces1 = 0
veces2 = 0
veces3 = 0
#Creo el menú que se debe repetir.
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if not(alarma == True and tiempo <= 3):
        print("\nIngrese una opción: ")
        print("1. Forzar cerradura (costo: -20 energía, -2 tiempo)")
        print("2. Hackear panel (costo: -10 energía, -3 tiempo)")
        print("3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)")
        print()
        opcion = input("Opción: \n")
        #Compruebo que ingresa opción válida
        while not(opcion.isdigit()) or int(opcion) < 1 or int(opcion) > 3:
            opcion = input ("Error, solo se aceptan números entre 1 y 3. Por favor, ingrese una opción: ")
        opcion = int(opcion)
        match opcion:
            case 1:
                veces1 += 1
                if veces1 == 3 and veces2 == 0 and veces3 == 0:
                    energia -= 20
                    tiempo -= 2
                    alarma = True
                    print ("Ha activado la alarma! La cerradura se trabó por querer forzarla 3 veces seguidas")
                    veces1 = 0
                else:
                    if energia < 40 and alarma == False:
                        print ("Su energía es baja. Hay riesgo de sonar la alarma. Debe elegir un número entre 1 y 3")
                        num_alarma = input()
                        while not(num_alarma.isdigit()) or int(num_alarma) < 1 or int(num_alarma) > 3:
                            num_alarma = input ("Error, solo se aceptan números entre 1 y 3. Por favor, ingrese una opción: ")
                        num_alarma = int(num_alarma)
                        if num_alarma == 3:
                            alarma = True
                            print ("Ha activado la ALARMA!!")
                    energia -= 20
                    tiempo -=2
                    cerraduras_abiertas += 1
                    print ("Ha forzado una cerradura!")
            case 2:
                veces2 += 1
                for i in range (4):
                    print ("Intentando hackear panel...")
                codigo_parcial = codigo_parcial + "A"
                if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    print("Ha logrado hackear el panel! Se abrió una cerradura")
                else:
                    print("No se pudo hackear el panel!")
                energia -= 10
                tiempo -= 3
            case 3:
                veces3 += 1
                if energia < 100 and alarma == False:
                    energia += 15
                    if energia > 100:
                        energia = 100
                    tiempo -= 1
                elif energia < 100 and alarma == True:
                    energia += 5
                    if energia > 100:
                        energia = 100
                    tiempo -= 1
                else:
                    print ("No es necesario descansar. Ha perdido tiempo.")
        print (f"{agente} su energía es {energia}, le queda {tiempo} tiempo y logró abrir {cerraduras_abiertas} cerraduras")
    else:
        tiempo = 0
        print ("\nHa sonado la alarma, ya no hay tiempo. El sistema se ha BLOQUEADO. FIN DEL JUEGO")
    if cerraduras_abiertas == 3:
        print(f"{agente} ha logrado abrir la Bóveda!")