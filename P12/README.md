# Piedra, Papel o Tijera

Un juego de consola clásico escrito en Python, pensado como proyecto de aprendizaje para estudiantes de primer nivel de programación de la UNIVERSIDAD INTERNACIONAL DEL ECUADOR.

---

## Tabla de contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Cómo funciona](#cómo-funciona)
- [Ejemplo de ejecución](#ejemplo-de-ejecución)
- [Conceptos de Python utilizados](#conceptos-de-python-utilizados)
- [Posibles mejoras](#posibles-mejoras)
- [Autor](#autor)
- [Licencia](#licencia)

---

## Descripción

Este proyecto implementa el juego **Piedra, Papel o Tijera** en la terminal. El jugador compite contra la computadora, que elige su jugada de forma aleatoria. Al final de cada partida se muestran las estadísticas acumuladas, que se guardan en un archivo JSON para que persistan entre sesiones.

El código está escrito de forma deliberadamente sencilla y con comentarios que explican cada decisión.

---

## Características

- Validación estricta de entradas: el programa nunca acepta una respuesta inválida y repite la pregunta hasta recibir una opción correcta.
- Estadísticas persistentes: victorias, derrotas y empates se guardan automáticamente en `estadisticas.json`.
- Lógica clara: el resultado de cada ronda se decide con condicionales simples y fáciles de leer.
- Sin dependencias externas: solo usa módulos de la biblioteca estándar de Python (`random`, `json`, `os`).

---

## Requisitos

- Python 3.6 o superior
- No se necesita instalar ningún paquete adicional

Para verificar tu versión de Python:

```bash
python --version
```

---

## Instalación

1. Clona o descarga este repositorio:

```bash
git clone https://github.com/AndrewsValenciaAD/Homework/blob/main/P12/gamePpt.py
```


---

## Uso

Ejecuta el juego desde la terminal con:

```bash
python gamePpt.py
```

Durante el juego el programa te guiará paso a paso:

- Elige tu jugada ingresando `1`, `2` o `3`.
- Responde `s` (sí) o `n` (no) cuando se te pregunta si quieres ver las estadísticas o jugar otra ronda.
- Si ingresas cualquier otra cosa, el programa te pedirá que lo intentes de nuevo.

---

## Estructura del proyecto

```
P12/
│
├── gamePpt.py   # Código principal del juego
├── estadisticas.json        # Generado automáticamente al jugar por primera vez
└── README.md                # Este archivo
```

> **Nota:** `estadisticas.json` se crea solo la primera vez que ejecutas el juego. No es necesario crearlo manualmente.

---

## Cómo funciona

El juego sigue este flujo en cada ronda:

```
Inicio
  │
  ▼
El jugador elige (1/2/3)  ──── entrada inválida ──▶ vuelve a preguntar
  │
  ▼
La PC elige aleatoriamente
  │
  ▼
Se comparan las jugadas
  │
  ├── Empate    ──▶ "¡Empate!"
  ├── Gana PC   ──▶ "Perdiste."
  └── Gana jugador ──▶ "¡Ganaste!"
  │
  ▼
Se guardan las estadísticas
  │
  ▼
¿Ver estadísticas? (s/n)  ──── entrada inválida ──▶ vuelve a preguntar
  │
  ▼
¿Jugar otra ronda? (s/n)  ──── entrada inválida ──▶ vuelve a preguntar
  │
  ├── sí ──▶ vuelve al inicio
  └── no ──▶ muestra estadísticas finales y termina
```

### Reglas del juego

| Jugada    | Vence a  |
|-----------|----------|
| Piedra    | Tijera   |
| Tijera    | Papel    |
| Papel     | Piedra   |

---

## Ejemplo de ejecución

```
=== Piedra, Papel o Tijera ===

1. Piedra
2. Papel
3. Tijera
Elige una opción (1, 2 o 3): 5
Opción inválida. Por favor ingresa 1, 2 o 3.

1. Piedra
2. Papel
3. Tijera
Elige una opción (1, 2 o 3): 1

Tú elegiste:   piedra
La PC eligió:  tijera
¡Ganaste!

¿Ver estadísticas? (s/n): s

--- Estadísticas ---
Victorias: 1
Derrotas:  0
Empates:   0

¿Jugar otra ronda? (s/n): n

--- Estadísticas ---
Victorias: 1
Derrotas:  0
Empates:   0

¡Hasta la próxima!
```

---

## Conceptos de Python utilizados

Este proyecto es una buena práctica para los siguientes temas de introducción a la programación:

| Concepto | Dónde se aplica |
|---|---|
| Variables y tipos de datos | Jugadas, contadores de estadísticas |
| Condicionales `if / elif / else` | Decidir el ganador de cada ronda |
| Bucles `while True` + `break` | Validar entradas y repetir el juego |
| Funciones `def` | Organizar el código en bloques reutilizables |
| Módulo `random` | Generar la jugada de la computadora |
| Módulo `json` | Guardar y leer estadísticas en un archivo |
| Módulo `os` | Verificar si el archivo de estadísticas existe |

---

## Posibles mejoras

Estas son algunas ideas para extender el proyecto una vez que domines los conceptos básicos:

- [ ] Agregar un modo de **2 jugadores** en la misma computadora.
- [ ] Mostrar el **historial** de las últimas partidas jugadas.
- [ ] Implementar el modo **"Piedra, Papel, Tijera, Lagarto, Spock"** con 5 opciones.
- [ ] Crear una **interfaz gráfica** usando `tkinter`.
- [ ] Agregar un **límite de rondas** y un sistema de puntos por partida.

---

## Autor

Desarrollado por Andrés Chamba como proyecot de primer semestre de programción.

---

## Licencia

Este proyecto puedes usarlo, modificarlo y distribuirlo libremente, incluso con fines educativos o comerciales.
