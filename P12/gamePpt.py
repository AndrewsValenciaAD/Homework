#__________________________________________FINAL RROYECT___________________________________________
import random
import json
import os

ARCHIVO_ESTADISTICAS = "estadisticas.json"

# ─── Estadísticas ─────────────────────────────────────────────────────────────

def cargar_estadisticas():
    if os.path.exists(ARCHIVO_ESTADISTICAS):
        with open(ARCHIVO_ESTADISTICAS, "r") as archivo:
            return json.load(archivo)
    return {"victorias": 0, "derrotas": 0, "empates": 0}

def guardar_estadisticas(estadisticas):
    with open(ARCHIVO_ESTADISTICAS, "w") as archivo:
        json.dump(estadisticas, archivo, indent=4)

def mostrar_estadisticas(estadisticas):
    print("\n--- Estadísticas ---")
    print("Victorias:", estadisticas["victorias"])
    print("Derrotas: ", estadisticas["derrotas"])
    print("Empates:  ", estadisticas["empates"])

# ─── Entrada del usuario ──────────────────────────────────────────────────────

def pedir_jugada():
    # Repetimos la pregunta hasta que el usuario ingrese 1, 2 o 3
    while True:
        print("\n1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        opcion = input("Elige una opción (1, 2 o 3): ").strip()

        if opcion == "1":
            return "piedra"
        elif opcion == "2":
            return "papel"
        elif opcion == "3":
            return "tijera"
        else:
            print("Opción inválida. Por favor ingresa 1, 2 o 3.")

def pedir_si_no(pregunta):
    # Repetimos la pregunta hasta recibir 's' o 'n'
    while True:
        respuesta = input(pregunta + " (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("Por favor ingresa 's' para sí o 'n' para no.")

# ─── Lógica del juego ─────────────────────────────────────────────────────────

def opcion_computadora():
    return random.choice(["piedra", "papel", "tijera"])

def decidir_ganador(usuario, computadora):
    if usuario == computadora:
        return "empate"
    # Condiciones donde el usuario gana
    if (usuario == "piedra" and computadora == "tijera") or \
       (usuario == "tijera" and computadora == "papel") or \
       (usuario == "papel"  and computadora == "piedra"):
        return "ganaste"
    return "perdiste"

# ─── Programa principal ───────────────────────────────────────────────────────

print("=== Piedra, Papel o Tijera ===")

estadisticas = cargar_estadisticas()

while True:
    # Turno del jugador y la computadora
    jugada_usuario      = pedir_jugada()
    jugada_computadora  = opcion_computadora()

    print("\nTú elegiste:  ", jugada_usuario)
    print("La PC eligió: ", jugada_computadora)

    # Resultado de la ronda
    resultado = decidir_ganador(jugada_usuario, jugada_computadora)

    if resultado == "ganaste":
        print("¡Ganaste!")
        estadisticas["victorias"] += 1
    elif resultado == "perdiste":
        print("Perdiste.")
        estadisticas["derrotas"] += 1
    else:
        print("¡Empate!")
        estadisticas["empates"] += 1

    guardar_estadisticas(estadisticas)

    # Preguntar si quiere continuar o ver estadísticas
    if pedir_si_no("\n¿Ver estadísticas?"):
        mostrar_estadisticas(estadisticas)

    if not pedir_si_no("¿Jugar otra ronda?"):
        break

mostrar_estadisticas(estadisticas)
print("\n¡Hasta la próxima!")
