# Piedra, Papel o Tijera

**Universidad Internacional del Ecuador — Primer Semestre -Lógica de Programación**  
**Autor:** Andrés Chamba  
**Fecha de entrega:** Semana 8 — Junio 2025  
**Repositorio:** [github.com/AndrewsValenciaAD/Homework/P12](https://github.com/AndrewsValenciaAD/Homework/blob/main/P12/gamePpt.py)

---

## Tabla de contenidos

1. [Introducción](#introducción)
2. [Descripción del problema](#descripción-del-problema)
3. [Planificación del proyecto](#planificación-del-proyecto)
4. [Cronograma de actividades](#cronograma-de-actividades)
5. [Funcionalidades del sistema](#funcionalidades-del-sistema)
6. [Estructura lógica del programa](#estructura-lógica-del-programa)
7. [Organización del código](#organización-del-código)
8. [Relación con los contenidos de la asignatura](#relación-con-los-contenidos-de-la-asignatura)
9. [Herramientas de desarrollo](#herramientas-de-desarrollo)
10. [Impacto tecnológico en la sociedad](#impacto-tecnológico-en-la-sociedad)
11. [Instalación y uso](#instalación-y-uso)
12. [Ejemplo de ejecución](#ejemplo-de-ejecución)
13. [Posibles mejoras](#posibles-mejoras)
14. [Reflexión final](#reflexión-final)

---

## Introducción

Este proyecto es un juego de **Piedra, Papel o Tijera** desarrollado en Python como proyecto del primer semestre de programación. El objetivo es aplicar de forma práctica los conceptos estudiados a lo largo de las ocho semanas de la asignatura: variables, condicionales, bucles, funciones, entre otros.

---

## Descripción del problema

El juego Piedra, Papel o Tijera es un problema clásico de lógica con reglas simples pero que exige tomar decisiones, comparar valores y manejar la entrada del usuario de forma robusta. El reto principal es que el programa no se rompa ante respuestas inesperadas y que las estadísticas del jugador se conserven entre sesiones.

**Problema que resuelve:** el usuario necesita un juego interactivo en consola que valide sus respuestas, decida un ganador de forma justa y recuerde sus resultados anteriores.

**Nuevas funcionalidades implementadas respecto a la versión básica:**

- Validación estricta de entradas: si el usuario escribe algo que no corresponde a una opción válida, el programa vuelve a preguntar indefinidamente hasta recibir una respuesta correcta. Esto aplica tanto a la jugada (1/2/3) como a las preguntas de sí/no.
- Estadísticas persistentes: los resultados se guardan en un archivo `estadisticas.json` y se mantienen entre partidas, incluso si se cierra el programa.
- Organización en funciones: el código está dividido en funciones con responsabilidades claras, lo que lo hace más fácil de leer, mantener y extender.

---

## Planificación del proyecto

**Alcance del sistema:**

- Juego funcional en consola, un jugador vs. computadora.
- Validación completa de entradas del usuario.
- Registro y persistencia de estadísticas en archivo JSON.
- Código organizado en funciones documentadas con comentarios.

**Fuera del alcance (versión actual):**

- Interfaz gráfica.
- Modo multijugador en red.
- Base de datos o historial detallado por fecha.

---

## Cronograma de actividades

| Semana | Tema de la asignatura                        | Actividad del proyecto                                              |
|--------|----------------------------------------------|---------------------------------------------------------------------|
| 1      | Introducción a la resolución de problemas    | Definir el problema, identificar entradas, salidas y proceso        |
| 2      | Entorno de programación y depuración         | Configurar VS Code, crear el archivo `.py`, primeras pruebas        |
| 3      | Manejo de datos: variables y tipos           | Declarar variables de jugada y contadores de estadísticas           |
| 4      | Algoritmos y diagramas de flujo              | Diseñar el flujo del juego y dibujar el diagrama principal          |
| 5      | Condicionales (`if / elif / else`)           | Implementar la lógica que decide el ganador de cada ronda           |
| 6      | Bucles (`while`, `for`)                      | Agregar el bucle principal del juego y la validación de entradas    |
| 7      | Estructuras de datos y funciones             | Refactorizar el código en funciones; usar diccionarios para el JSON |
| 8      | Entrega final                                | Documentar, hacer pruebas, subir a GitHub y escribir el README      |

---

## Funcionalidades del sistema

| Funcionalidad              | Descripción                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Selección de jugada        | El usuario elige entre Piedra (1), Papel (2) o Tijera (3)                  |
| Jugada de la computadora   | La PC elige aleatoriamente con `random.choice()`                           |
| Decisión del ganador       | Se comparan ambas jugadas con condicionales `if/elif/else`                 |
| Validación de entradas     | Bucles `while True` rechazan cualquier entrada fuera de las opciones válidas|
| Estadísticas persistentes  | Se leen y escriben con el módulo `json` en `estadisticas.json`             |
| Repetición de partidas     | El jugador puede jugar tantas rondas como quiera antes de salir            |

---

## Estructura lógica del programa

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
Se actualizan y guardan las estadísticas
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

**Reglas del juego:**

| Jugada  | Vence a |
|---------|---------|
| Piedra  | Tijera  |
| Tijera  | Papel   |
| Papel   | Piedra  |

---

## Organización del código

```
P12/
│
├── gamePpt.py          # Código principal del juego
├── estadisticas.json   # Generado automáticamente al jugar por primera vez
└── README.md           # Este archivo
```

El archivo `gamePpt.py` está dividido en cuatro bloques de funciones:

| Bloque        | Funciones                              | Responsabilidad                              |
|---------------|----------------------------------------|----------------------------------------------|
| Estadísticas  | `cargar_estadisticas()`  `guardar_estadisticas()`  `mostrar_estadisticas()` | Leer, escribir y mostrar los resultados acumulados |
| Entrada       | `pedir_jugada()`  `pedir_si_no()`      | Solicitar y validar la entrada del usuario   |
| Lógica        | `opcion_computadora()`  `decidir_ganador()` | Generar la jugada de la PC y comparar ambas jugadas |
| Principal     | Bloque `while True` en `main`          | Coordinar el flujo completo del juego        |

---

## Relación con los contenidos de la asignatura

| Unidad | Tema                              | Aplicación en el proyecto                                      |
|--------|-----------------------------------|----------------------------------------------------------------|
| 1      | Resolución de problemas           | Análisis del juego: entradas, proceso y salidas               |
| 2      | Variables, tipos y operadores     | `jugada_usuario`, `jugada_computadora`, contadores            |
| 2      | Algoritmos y diagramas de flujo   | Diagrama del flujo del juego (ver sección anterior)           |
| 3      | Condicionales `if/elif/else`      | Función `decidir_ganador()` y validación de entradas          |
| 3      | Bucles `while`                    | Bucle principal del juego y bucles de validación              |
| 4      | Funciones                         | Todo el código está organizado en funciones reutilizables     |
| 4      | Diccionarios                      | Estructura JSON de estadísticas; `opciones` como diccionario  |

---

## Herramientas de desarrollo

| Herramienta   | Uso                                           |
|---------------|-----------------------------------------------|
| Python 3.x    | Lenguaje de programación principal            |
| VS Code       | Editor de código con depurador integrado      |
| Git & GitHub  | Control de versiones y entrega del proyecto   |
| Módulo `random` | Generación de la jugada aleatoria de la PC  |
| Módulo `json`   | Persistencia de estadísticas entre sesiones  |
| Módulo `os`     | Verificar si el archivo de estadísticas existe |

---

## Impacto tecnológico en la sociedad

Aunque este es un juego sencillo, demuestra conceptos que están en la base de sistemas mucho más complejos. La validación de entradas protege al sistema de errores humanos, algo esencial en aplicaciones médicas, bancarias o de transporte. La persistencia de datos en archivos es el principio detrás de cualquier sistema que "recuerde" al usuario. Aprender a programar este tipo de lógica desde cero forma la base del pensamiento computacional que permite resolver problemas reales del mundo.

---

## Instalación y uso

**Requisitos:** Python 3.6 o superior. Sin dependencias externas.

```bash
# Verificar versión de Python
python --version

# Clonar el repositorio
git clone https://github.com/AndrewsValenciaAD/Homework.git

# Ir a la carpeta del proyecto
cd Homework/P12

# Ejecutar el juego
python gamePpt.py
```

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

## Posibles mejoras

- [ ] Modo de 2 jugadores en la misma computadora.
- [ ] Historial detallado con fecha y hora de cada partida.
- [ ] Versión extendida: Piedra, Papel, Tijera, Lagarto, Spock.
- [ ] Interfaz gráfica con `tkinter`.
- [ ] Límite de rondas con sistema de puntos por partida.

---

## Reflexión final

Desarrollar este proyecto permitió conectar cada tema de la asignatura con un problema concreto. El mayor aprendizaje fue entender que un programa robusto no solo hace lo correcto cuando todo va bien, sino que también maneja los errores del usuario de forma controlada. La organización del código en funciones hizo que cada parte fuera más fácil de entender, probar y corregir por separado.
