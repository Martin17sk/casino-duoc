import random

opcion_apuesta = 0
OPCIONES_VALIDAS = list(range(1,9))

saldo = 1000

SECUENCIA = list(range(0,37))       # 0 - 36

ROJOS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
NEGROS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

PARES = list(range(0,37,2))
IMPARES = list(range(1,36,2))

FALTA = list(range(1,19))           # 1 - 18
PASA = list(range(19-37))           # 19 - 36

DOCENA_1 = list(range(1,13))        # 1 - 12
DOCENA_2 = list(range(13,25))       # 13 - 24
DOCENA_3 = list(range(25,37))       # 25 - 36

COLUMNA_1 = list(range(1,35,3))
COLUMNA_2 = list(range(2,36,3))
COLUMNA_3 = list(range(3,37,3))

FILA_1 = [1,2,3]
FILA_2 = [4,5,6]
FILA_3 = [7,8,9]
FILA_4 = [10,11,12]
FILA_5 = [13,14,15]
FILA_6 = [16,17,18]
FILA_7 = [19,20,21]
FILA_8 = [22,23,24]
FILA_9 = [25,26,27]
FILA_10 = [28,29,30]
FILA_11 = [31,32,33]
FILA_12 = [34,35,36]

TIPOS_APUESTAS = {                  # Nombre: Multiplicador
    "rojo o negro": 1, 
    "par o impar": 1,
    "falta o pasa": 1,
    "docenas": 2,
    "columnas": 2,
    "pleno": 35,
    "calle": 11
    }

print("---------- Ruleta Europea ----------")
print(f"Saldo: ${saldo}")
while True:
    while True:
        if saldo <= 0:
            break

        print("\n¿Donde quieres apostar?\n")

        print("1. Rojo o Negro (Paga x1)")
        print("2. Par o Impar (Paga x1)")
        print("3. Falta o Pasa (Paga x1)")
        print("4. Docenas (Paga x2)")
        print("5. Columnas (Paga x2)")
        print("6. Pleno (Paga x35)")
        print("7. Calle (Paga x11)")
        print("8. Salir")

        opcion_apuesta = int(input("Selecciona tu opción: "))

        if opcion_apuesta not in OPCIONES_VALIDAS:
            print("Por favor, ingrese una opción válida")
        else:
            break

    if opcion_apuesta == 8 or saldo <= 0:
        break

    while True:
        monto_apuesta = int(input("Ingresa el monto a apostar: $"))
        print("")

        if monto_apuesta > saldo:
            print("No tienes dinero suficiente, ingresa otro monto")
        elif monto_apuesta < 1:
            print("No puede apostar ese monto, ingresa otro monto")
        else:
            break

    num_aleatorio = random.choice(SECUENCIA)            # Se escoge el número aleatorio

    if opcion_apuesta == 1:                             # Rojo o Negro
        multiplicador = TIPOS_APUESTAS.get("rojo o negro")

        while True:
            print("¿A cuál color quieres apostar?")
            print("1. Rojo")
            print("2. Negro\n")

            eleccion_apuesta = int(input("Selecciona tu opción: "))

            if eleccion_apuesta != 1 and eleccion_apuesta != 2:
                print("Por favor, ingresa una opción válida")
            else:
                break
        
        print(50*"-")
        print(f"La bola cayó en {num_aleatorio}")
        print(50*"-")

        if eleccion_apuesta == 1:                       # Escogió rojo
            if num_aleatorio in ROJOS:                      # Ganó
                saldo += monto_apuesta * multiplicador
                print("¡Ganaste!, es rojo")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:                                           # Perdió
                saldo -= monto_apuesta
                print("Perdiste, es negro")
                print(f"Tu nuevo saldo es: ${saldo}")
        else:                                           # Escogió negro
            if num_aleatorio in NEGROS:                     # Ganó
                saldo += monto_apuesta * multiplicador
                print("¡Ganaste!, es negro")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:                                           # Perdió
                saldo -= monto_apuesta
                print("Perdiste, es rojo")
                print(f"Tu nuevo saldo es: ${saldo}")
    elif opcion_apuesta == 2:                           # Par o Impar
        multiplicador = TIPOS_APUESTAS.get("par o impar")

        while True:
            print("¿A cual opción quieres apostar")
            print("1. Par")
            print("2. Impar\n")

            eleccion_apuesta = int(input("Selecciona tu opción: "))

            if eleccion_apuesta != 1 and eleccion_apuesta != 2:
                print("Por favor, selecciona una opción válida")
            else:
                break

        print(50*"-")
        print(f"La bola cayó en {num_aleatorio}")
        print(50*"-")

        if eleccion_apuesta == 1:                       # Escogió par
            if num_aleatorio in PARES:                      # Ganó
                saldo += monto_apuesta * multiplicador
                print(f"{num_aleatorio} es par, ¡Ganaste!")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:                                           # Perdió
                saldo -= monto_apuesta
                print(f"{num_aleatorio} es impar, perdiste")
                print(f"Tu nuevo saldo es: ${saldo}")
        else:                                           # Escogió impar
            if num_aleatorio in IMPARES:                      # Ganó
                saldo += monto_apuesta * multiplicador
                print(f"{num_aleatorio} es par, ¡Ganaste!")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:
                saldo -= monto_apuesta                      # Perdió
                print(f"{num_aleatorio} es impar, perdiste")
                print(f"Tu nuevo saldo es: ${saldo}")
    elif opcion_apuesta == 3:                           # Falta o Pasa
        multiplicador = TIPOS_APUESTAS.get("falta o pasa")

        while True:
            print("¿A cual opción quieres apostar")
            print("1. Falta (1 - 18)")
            print("2. Pasa (19 - 36)\n")

            eleccion_apuesta = int(input("Selecciona tu opción: "))

            if eleccion_apuesta != 1 and eleccion_apuesta != 2:
                print("Por favor, selecciona una opción válida")
            else:
                break

        print(50*"-")
        print(f"La bola cayó en {num_aleatorio}")
        print(50*"-")

        if eleccion_apuesta == 1:                       # Escogió falta
            if num_aleatorio in FALTA:                      # Ganó
                saldo += monto_apuesta * multiplicador
                print(f"{num_aleatorio} está en Falta, ¡Ganaste!")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:                                           # Perdió
                saldo -= monto_apuesta
                print(f"{num_aleatorio} está en Pasa, perdiste")
                print(f"Tu nuevo saldo es: ${saldo}")
        else:                                           # Escogió pasa
            if num_aleatorio in PASA:                      # Ganó
                saldo += monto_apuesta * multiplicador
                print(f"{num_aleatorio} está en Pasa, ¡Ganaste!")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:
                saldo -= monto_apuesta                      # Perdió
                print(f"{num_aleatorio} está en Falta, perdiste")
                print(f"Tu nuevo saldo es: ${saldo}")
    elif opcion_apuesta == 4:                           # Docenas
        multiplicador = TIPOS_APUESTAS.get("docenas")

        while True:
            print("¿A cual opción quieres apostar")
            print("1. 1ra docena (1 - 12)")
            print("2. 2da docena (13 - 24)")
            print("3. 3ra docena (25 - 36)")

            eleccion_apuesta = int(input("Selecciona tu opción: "))

            if eleccion_apuesta != 1 and eleccion_apuesta != 2 and eleccion_apuesta != 3:
                print("Por favor, selecciona una opción válida")
            else:
                break

        print(50*"-")
        print(f"La bola cayó en {num_aleatorio}")
        print(50*"-")

        if eleccion_apuesta == 1:                       # Escogió 1ra docena
            if num_aleatorio in DOCENA_1:                   # Ganó
                saldo += monto_apuesta * multiplicador
                print(f"{num_aleatorio} está en la 1ra docena, ¡Ganaste!")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:                                           # Perdió
                saldo -= monto_apuesta
                print(f"{num_aleatorio} no está la 1ra docena, perdiste")
                print(f"Tu nuevo saldo es: ${saldo}")
        elif eleccion_apuesta == 2:                     # Escogió 2da docena
            if num_aleatorio in DOCENA_2:                   # Ganó
                saldo += monto_apuesta * multiplicador
                print(f"{num_aleatorio} está en la 2da docena, ¡Ganaste!")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:                                           # Perdió
                saldo -= monto_apuesta
                print(f"{num_aleatorio} no está la 2da docena, perdiste")
                print(f"Tu nuevo saldo es: ${saldo}")
        else:                                           # Escogió 3ra docena
            if num_aleatorio in DOCENA_3:                   # Ganó
                saldo += monto_apuesta * multiplicador
                print(f"{num_aleatorio} está en la 3ra docena, ¡Ganaste!")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:                                           # Perdió
                saldo -= monto_apuesta
                print(f"{num_aleatorio} no está la 3ra docena, perdiste")
                print(f"Tu nuevo saldo es: ${saldo}")
    elif opcion_apuesta == 5:                           # Columnas
        multiplicador = TIPOS_APUESTAS.get("columnas")

        while True:
            print("¿A cual opción quieres apostar?")
            print("1. 1ra columna")
            print("2. 2da columna")
            print("3. 3ra columna")

            eleccion_apuesta = int(input("Selecciona tu opción: "))

            if eleccion_apuesta != 1 and eleccion_apuesta != 2 and eleccion_apuesta != 3:
                print("Por favor, selecciona una opción válida")
            else:
                break

        print(50*"-")
        print(f"La bola cayó en {num_aleatorio}")
        print(50*"-")

        if eleccion_apuesta == 1:                       # Escogió 1ra columna
            if num_aleatorio in COLUMNA_1:                   # Ganó
                saldo += monto_apuesta * multiplicador
                print(f"{num_aleatorio} está en la 1ra columna, ¡Ganaste!")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:                                           # Perdió
                saldo -= monto_apuesta
                print(f"{num_aleatorio} no está la 1ra columna, perdiste")
                print(f"Tu nuevo saldo es: ${saldo}")
        elif eleccion_apuesta == 2:                     # Escogió 2da columna
            if num_aleatorio in COLUMNA_2:                   # Ganó
                saldo += monto_apuesta * multiplicador
                print(f"{num_aleatorio} está en la 2da columna, ¡Ganaste!")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:                                           # Perdió
                saldo -= monto_apuesta
                print(f"{num_aleatorio} no está la 2da columna, perdiste")
                print(f"Tu nuevo saldo es: ${saldo}")
        else:                                           # Escogió 3ra columna
            if num_aleatorio in COLUMNA_3:                   # Ganó
                saldo += monto_apuesta * multiplicador
                print(f"{num_aleatorio} está en la 3ra columna, ¡Ganaste!")
                print(f"Tu nuevo saldo es: ${saldo}")
            else:                                           # Perdió
                saldo -= monto_apuesta
                print(f"{num_aleatorio} no está la 3ra columna, perdiste")
                print(f"Tu nuevo saldo es: ${saldo}")
    elif opcion_apuesta == 6:                           # Pleno
        multiplicador = TIPOS_APUESTAS.get("pleno")

        while True:
            eleccion_apuesta = int(input("¿A qué número quieres apostar?: "))

            if eleccion_apuesta not in SECUENCIA:
                print("Por favor, ingresa un número válido")
            else:
                break

        print(50*"-")
        print(f"La bola cayó en {num_aleatorio}")
        print(50*"-")

        if num_aleatorio == eleccion_apuesta:               # Ganó
            saldo += monto_apuesta * multiplicador
            print("¡Ganaste!")
            print(f"Tu nuevo saldo es: ${saldo}")
        else:                                               # Perdió
            saldo -= monto_apuesta
            print("Perdiste")
            print(f"Tu nuevo saldo es: ${saldo}")
    elif opcion_apuesta == 7:                                               # Calle
        multiplicador = TIPOS_APUESTAS.get("calle")

        while True:
            for i in range(12):
                n1 = i * 3 + 1
                n2 = i * 3 + 2
                n3 = i * 3 + 3
                print(f"{i+1}. ({n1}, {n2}, {n3})")

            eleccion_apuesta = int(input("¿A qué calle quieres apostar?: "))

            if eleccion_apuesta not in list(range(1,13)):
                print("Por favor, ingresa una opción válida")
            else:
                break

        print(50*"-")
        print(f"La bola cayó en {num_aleatorio}")
        print(50*"-")

        num_fila_num_aleatorio = (num_aleatorio - 1) // 3 + 1
        
        if num_fila_num_aleatorio == eleccion_apuesta:      # Ganó
            saldo += monto_apuesta * multiplicador
            print("¡Ganaste!")
            print(f"Tu nuevo saldo es: ${saldo}")
        else:
            saldo -= monto_apuesta
            print("Perdiste")
            print(f"Tu nuevo saldo es: ${saldo}")          # Perdió

if saldo <= 0:
    print("Se acabó el juego, te quedaste sin dinero")
else:
    print("¡Gracias por jugar!")
    print(f"Tu saldo final es de: ${saldo}")