#Ejercicio 3
#“Agenda de Turnos con Nombres (sin listas)”
#Se solicita ingresar nombre del operador:
operador = input ("Ingrese el nombre del operador: ")
#En el siguiente paso se valida si contiene solo letras (de la A a la Z) y si tiene al menos un carácter. Si no, se solicita nuevamente.
while not(operador.isalpha()):
    operador = input ("Error, solo se aceptan letras. Por favor, ingrese su nombre: ")
#Creo el menú que se debe repetir. Inicializo la variable opcion en cero para que al menos haga un ciclo.
opcion = 0
#Inicializo variables de reserva de turno para lunes (4 turnos) y Martes (3 turnos)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
#Creo el menú con While
while opcion != 5:
    print("Ingrese una opción: ")
    print("1. Reservar turno")
    print("2. Cancelar turno (por nombre)")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Salir ")
    print()
    opcion = input("Opción: ")
    #Compruebo que ingresa opción válida
    while not(opcion.isdigit()) or int(opcion) < 1 or int(opcion) > 5:
        opcion = input ("Error, solo se aceptan números entre 1 y 4. Por favor, ingrese una opción: ")
    opcion = int(opcion)
    match opcion:
        case 1:
            dia = input("Elija el día en que quiere su reserva (1= Lunes, 2= Martes): ")
            #Compruebo que ingresa día válido
            while not(dia.isdigit()) or (int(dia) != 1 and int(dia) != 2):
                dia = input ("Error, solo se aceptan números: 1 para lunes y 2 para Martes. Por favor, ingrese una opción: ")
            #Compruebo que el paciente no está agendado en uno de los turnos del lunes y si es verdadero le asigno un turno.
            if int(dia) == 1:
                paciente = input("Ingrese nombre de paciente: ")
                while not(paciente.isalpha()):
                    paciente = input ("Error, solo se aceptan letras. Por favor, ingrese el nombre del paciente: ")
                if paciente != lunes1 and paciente != lunes2 and paciente != lunes3 and paciente != lunes4:
                    if lunes1 == "":
                        lunes1 = paciente
                    elif lunes2 == "":
                        lunes2 = paciente
                    elif lunes3 == "":
                        lunes3 = paciente
                    elif lunes4 == "":
                        lunes4 = paciente
                    else:
                        print("No hay turnos disponibles el día Lunes.\n")
                else:
                    print ("El paciente ya posee un turno el día lunes.\n")
            #y sino compruebo que el paciente no está agendado en uno de los turnos del Martes y si es verdadero le asigno un turno.
            elif int(dia) == 2:
                paciente = input("Ingrese nombre de paciente: ")
                while not(paciente.isalpha()):
                    paciente = input ("Error, solo se aceptan letras. Por favor, ingrese el nombre del paciente: ")
                if paciente != martes1 and paciente != martes2 and paciente != martes3:
                    if martes1 == "":
                        martes1 = paciente
                    elif martes2 == "":
                        martes2 = paciente
                    elif martes3 == "":
                        martes3 = paciente
                    else:
                        print("No hay turnos disponibles el día martes.\n")
                else:
                    print ("El paciente ya posee un turno el día martes.\n")
        case 2:
            paciente = input("Ingrese nombre del paciente para cancelar la reserva: ")
            while not(paciente.isalpha()):
                paciente = input ("Error, solo se aceptan letras. Por favor, ingrese el nombre del paciente: ")
            #Compruebo si hay reserva para ese paciente, si hay, cargo vacío el turno
            if paciente != lunes1 and paciente != lunes2 and paciente != lunes3 and paciente != lunes4 and paciente != martes1 and paciente != martes2 and paciente != martes3:
                print(f"El paciente {paciente} no tiene turno reservado.")
            else:
                if lunes1 == paciente:
                    lunes1 = ""
                elif lunes2 == paciente:
                    lunes2 = ""
                elif lunes3 == paciente:
                    lunes3 = ""
                elif lunes4 == paciente:
                    lunes4 = ""
                elif martes1 == paciente:
                    martes1 = ""
                elif martes2 == paciente:
                    martes2 = ""
                elif martes3 == paciente:
                    martes3 = ""
                print("Se ha cancelado el turno exitosamente\n")
        case 3:
            dia_agenda = input("Elija el día del que quiere ver la agenda (1= Lunes, 2= Martes): ")
            #Compruebo que ingresa día válido
            while not(dia_agenda.isdigit()) or (int(dia_agenda) != 1 and int(dia_agenda) != 2):
                dia_agenda = input ("Error, solo se aceptan números: 1 para lunes y 2 para Martes. Por favor, ingrese una opción: ")
            #Compruebo que el paciente no está agendado en uno de los turnos del lunes y si es verdadero le asigno un turno.
            if int(dia_agenda) == 1:
                print("\nLos turnos del día lunes son:")
                if lunes1 == "":
                    print("\n1. Lunes = Libre")
                else:
                    print(f"\n1. Lunes = {lunes1}")
                if lunes2 == "":
                    print("2. Lunes = Libre")
                else:
                    print(f"2. Lunes = {lunes2}")
                if lunes3 == "":
                    print("3. Lunes = Libre")
                else:
                    print(f"3. Lunes = {lunes3}")
                if lunes4 == "":
                    print("4. Lunes = Libre\n")
                else:
                    print(f"4. Lunes = {lunes4}\n")
            elif int(dia_agenda) == 2:
                print("\nLos turnos del día Martes son:")
                if martes1 == "":
                    print("\n1. Martes = Libre")
                else:
                    print(f"\n1. Martes = {martes1}")
                if martes2 == "":
                    print("2. Martes = Libre")
                else:
                    print(f"2. Martes = {martes2}")
                if martes3 == "":
                    print("3. Martes = Libre\n")
                else:
                    print(f"3. Martes = {martes3}\n")
        case 4:
            ocupados_lunes = 0
            ocupados_martes = 0
            #Definidas dos variables para contar, utilizo if para sumar 1 cuando el turno no esté vacío
            if lunes1 != "":
                ocupados_lunes += 1
            if lunes2 != "":
                ocupados_lunes += 1
            if lunes3 != "":
                ocupados_lunes += 1
            if lunes4 != "":
                ocupados_lunes += 1
            if martes1 != "":
                ocupados_martes += 1
            if martes2 != "":
                ocupados_martes += 1
            if martes3 != "":
                ocupados_martes += 1
            #Luego imprimo en pantalla lo que se solicita
            if ocupados_lunes > ocupados_martes:
                print ("\nEl lunes hay mas turnos ocupados que el martes")
            elif ocupados_lunes < ocupados_martes:
                print ("\nEl martes hay mas turnos ocupados que el lunes")
            else:
                print ("\nLos días tiene la misma canridad de turnos ocupados")
            print(f"Turnos ocupados el Lunes: {ocupados_lunes} turnos y disponibles: {4-ocupados_lunes} turnos")
            print(f"Turnos ocupados el Martes: {ocupados_martes} turnos y disponibles: {4-ocupados_martes} turnos\n")
        case 5:
            print("Gracias por usar el sistema\n")