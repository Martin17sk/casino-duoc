#Parte Jairo TRAGAMONEDAS

import random

saldo = 1000
iconos = ["🍒", "🔔", "💎", "⭐"]
tiradas = 0
prestamo = False
deuda_prestamo = 0
salida = False

print()
print("🎰 Bienvenido al TRAGAMONEDAS 🎰")
print("  🎰========================🎰")
print("    || 🍒 | 🔔 | 💎 | ⭐ ||")
print("    >> ⭐ | 🍒 | 🔔 | 💎 <<")
print("    || 💎 | ⭐ | 🍒 | 🔔 ||")
print("  🎰========================🎰")
print("          🎮 GIRAR 🎮")

while True:
    print(f"\n💰 Saldo actual:💲{saldo}")

    if saldo <= 0 and prestamo == False:
        print()
        print("💀 Vaya, parece que te quedaste sin dinero...\n"
              "El casino le está ofreciendo un préstamo de💲2000\n")

        opcion_prestamo = input("¿Deseas el préstamo? (si/no): ").lower()

        if opcion_prestamo == "si":
            saldo += 2000
            deuda_prestamo = 2000
            prestamo = True
            print(f"\nHas adquirido el préstamo, tu nuevo 💰 saldo es💲{saldo}")

        else:
            print("💀 Fin del juego.\n")
            break

    if saldo > 2000 and tiradas >= 6 and prestamo == True:
        pago_prestamo = input("¿Deseas pagar el préstamo? (si/no): ").lower()
        tiradas = 0

        if pago_prestamo == "si":
            saldo -= deuda_prestamo
            prestamo = False
            print(f"Préstamo pagado. Su 💰 saldo actual es:💲{saldo}")
        else:
            continue

    if saldo <= 0 and prestamo == True:
        print()
        print("💀 Te quedaste sin dinero.🕴️🕴️  Unos hombres vestidos de negro vienen a tu casa.\nFin del juego.\n")
        break

    print()

    if salida == True:
        salida = input("¿Deseas continuar? (si/no): ").lower()
        if salida != "si":
            print("💀 Fin del juego.\n")
            break

    entrada = input("¿Cuánto desea apostar?:💲")
    salida = True

    es_numero = True
    for c in entrada:
        if c < "0" or c > "9":
            es_numero = False

    if entrada == "" or es_numero == False:
        print("Ingrese un número válido")
        continue

    saldo_de_apuesta = int(entrada)

    if saldo_de_apuesta <= 0:
        print("Ingrese un monto válido")
        continue

    if saldo_de_apuesta > saldo:
        print("No tienes suficiente 💰 saldo")
        continue

    saldo -= saldo_de_apuesta

    superior1 = random.choice(iconos)
    superior2 = random.choice(iconos)
    superior3 = random.choice(iconos)
    superior4 = random.choice(iconos)

    resultado1 = random.choice(iconos)
    resultado2 = random.choice(iconos)
    resultado3 = random.choice(iconos)
    resultado4 = random.choice(iconos)

    inferior1 = random.choice(iconos)
    inferior2 = random.choice(iconos)
    inferior3 = random.choice(iconos)
    inferior4 = random.choice(iconos)

    print("")
    print("        LAS VEGAS SLOTS")
    print("  🎰========================🎰")
    print(f"    || {superior1} | {superior2} | {superior3} | {superior4} ||")
    print(f"    >> {resultado1} | {resultado2} | {resultado3} | {resultado4} <<")
    print(f"    || {inferior1} | {inferior2} | {inferior3} | {inferior4} ||")
    print("  🎰========================🎰")

    if resultado1 == resultado2 == resultado3 == resultado4:
        premio = saldo_de_apuesta * 5
        saldo += premio
        tiradas += 1
        print()
        print(f"🎉 ¡JACKPOT! 🎉 Ganaste💲{premio}")

    elif (
        resultado1 == resultado2 == resultado3 or
        resultado1 == resultado2 == resultado4 or
        resultado1 == resultado3 == resultado4 or
        resultado2 == resultado3 == resultado4
    ):
        premio = saldo_de_apuesta * 2
        saldo += premio
        tiradas += 1
        print()
        print(f"✨ Ganaste💲{premio}")

    else:
        tiradas += 1
        print()
        print("😢 Perdiste la apuesta")