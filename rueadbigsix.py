import random  


saldo = 1000
dolar1 = 60000
dolar2 = 120000
dolar3 = 90000
perdida = 20

premios = [0, 0, 0, dolar1, dolar2, dolar3]

print("Bienvenido a Rueda Big Six")
print("Cada giro cuesta $20 (las perdidas se multiplican)")


while saldo >= 20:
    
    print(f" Saldo actual: ${saldo}")
    
    
    jugada = input("Escribe '1' para jugar, '2' para salir ")
    
    
    if jugada.isdigit():
        opcion = int(jugada) 
    else:
        print("ingresa un número válido.")
        continue

    
    if opcion == 2:
        print("Has decidido retirarte de la mesa.")
        break
    elif opcion == 1:
        print("Girando la rueda", end="")
        for i in range(6):
            print(".", end="")
        perdida = perdida * 5
        
        
        resultado = random.choice(premios)
        
        if resultado == 0:
            print(" La rueda cayó en 0.")
            print(f"Pierdes ${perdida}.")
            saldo -= perdida  
        else:
            print(f" La rueda cayó en una casilla ganadora.")
            print(f"Ganaste ${resultado}")
            saldo += resultado
            
        print("-" * 35)
    else:
        print(" Opción no válida")

# Mensaje final de despedida
if saldo < 20:
    print(" Te has quedado sin saldo suficiente para seguir jugando.")
    
print(f"tu saldo final para llevar a casa es: ${saldo}.")