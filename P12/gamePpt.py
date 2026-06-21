#*******************AVANCE*******************
import random
print("===== Bienvenido a mi primer juego =====\n")
print("===== PIEDRA, PAPEL O TIJERA =====\n")

jugar = "si"

while jugar == "si":
    
    # Mostrar opciones al usuario
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
    
    

print("\n¡Gracias por jugar!")





