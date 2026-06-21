import random

print("===== PIEDRA, PAPEL O TIJERA =====\n")

jugar = "si"

while jugar == "si":
    print("¿QUÉ ELIGES?")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    
    opcion_usuario = input("\nIngresa tu opción (1, 2 o 3): ")
    
    # Convertir la opción del usuario
    if opcion_usuario == "1":
        usuario = "piedra"
    elif opcion_usuario == "2":
        usuario = "papel"
    elif opcion_usuario == "3":
        usuario = "tijera"
    else:
        print("⚠️ Opción inválida\n")
        continue
    
    # Generar opción de la computadora
    computadora = random.choice(["piedra", "papel", "tijera"])
    
    # Mostrar lo que eligió cada uno
    print("\n--- RESULTADO ---")
    print(f"Tú elegiste: {usuario}")
    print(f"Computadora eligió: {computadora}")
    print()
    
    # Comparar y determinar ganador
    if usuario == computadora:
        print("¡EMPATE!")
    elif usuario == "piedra" and computadora == "tijera":
        print("¡GANASTE! Piedra vence a Tijera")
    elif usuario == "papel" and computadora == "piedra":
        print("¡GANASTE! Papel vence a Piedra")
    elif usuario == "tijera" and computadora == "papel":
        print("¡GANASTE! Tijera vence a Papel")
    else:
        print("Perdiste esta ronda")
    
    # Preguntar si quiere jugar de nuevo
    print()
    jugar = input("¿Quieres jugar de nuevo? (si/no): ")

print("\n¡Gracias por jugar!")
