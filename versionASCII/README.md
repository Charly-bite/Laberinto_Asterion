# 🏛️ El Laberinto de Asterión - Versión ASCII

## 📖 Descripción del Proyecto

**Aventura Interactiva – "El laberinto de la mazmorra"**

Este es un juego de aventura tipo Dungeon Crawler desarrollado en Python, donde controlas a Teseo, el héroe de Atenas, que debe explorar el laberinto del Palacio de Cnosos en Creta para encontrar aliados, recolectar objetos legendarios y enfrentar al Minotauro (Asterión).

---

## 🎯 Objetivo del Proyecto Educativo

**Base técnica:** Python / Google Colab  
**Duración:** 5 días hábiles  

Este proyecto está diseñado para ser **personalizable** y demuestra dominio de:
- ✅ Listas y estructuras de datos
- ✅ Condicionales complejas
- ✅ Ciclos (while, for)
- ✅ Funciones bien estructuradas
- ✅ Lectura/escritura de archivos JSON
- ✅ Programación orientada a objetos (básica)

---

## 🚀 Cómo Ejecutar en Google Colab

### Opción 1: Subir archivos manualmente

1. Ve a [Google Colab](https://colab.research.google.com/)
2. Crea un nuevo notebook
3. Sube los archivos:
   - `laberinto_ASCII.py`
   - `context.json`
4. Ejecuta en una celda de código:

```python
!python laberinto_ASCII.py
```

### Opción 2: Ejecutar desde notebook

Crea un nuevo notebook y ejecuta:

```python
# Celda 1: Subir archivos
from google.colab import files
uploaded = files.upload()  # Sube laberinto_ASCII.py y context.json

# Celda 2: Ejecutar el juego
!python laberinto_ASCII.py
```

### Opción 3: Desde repositorio

```python
# Clonar repositorio (si aplica)
!git clone <URL_DEL_REPOSITORIO>
%cd <DIRECTORIO>

# Ejecutar
!python laberinto_ASCII.py
```

---

## 🎮 Cómo Jugar

### Controles

- **N** = Mover al Norte (↑)
- **S** = Mover al Sur (↓)
- **E** = Mover al Este (→)
- **O** = Mover al Oeste (←)
- **HELP** = Mostrar ayuda en el juego

### Objetivo

1. Explora el laberinto 10×10
2. Encuentra los **5 personajes aliados** dispersos aleatoriamente
3. Cada personaje te ofrece **3 objetos legendarios**, pero solo puedes elegir **1**
4. Recolecta los 5 objetos correctos para obtener un **final victorioso**
5. ¡Evita que tus estadísticas lleguen a 0!

### Estadísticas

- **[HP] Salud:** Si llega a 0, mueres
- **[CD] Cordura:** Si llega a 0, enloqueces
- **[--] Hilo de Ariadna:** Cada movimiento consume 1 unidad
- **[**] Puntos:** Se acumulan con eventos aleatorios

---

## 🗂️ Estructura de Archivos

```
versionASCII/
├── laberinto_ASCII.py    # Código principal del juego
├── context.json          # Configuración (historia, personajes, objetos, finales)
├── README.md             # Este archivo
└── __pycache__/          # Archivos temporales de Python
```

---

## ⚙️ Requisitos del Sistema

- **Python:** 3.7 o superior
- **Dependencias:** Solo bibliotecas estándar
  - `json`
  - `random`
  - `time`
  - `os`
  - `pathlib`

**No requiere instalación de paquetes externos.**

---

## 🎨 Características Implementadas

### Requisitos Mínimos ✅

- [x] Historia personalizable desde `context.json`
- [x] 5 personajes aliados con 3 objetos cada uno
- [x] Mecánica nueva: **Campo de visión limitado** (fog of war)
- [x] Sistema de finales por combinación de objetos
- [x] Mensajes legibles en consola con colores ANSI
- [x] Lógica separada en funciones:
  - `inicializar_juego()` → Crea tablero y jugador
  - `colocar_personajes()` → Distribuye aliados
  - `encontrar_personaje()` → Interacción con NPCs
  - `mover_jugador()` → Sistema de movimiento
  - `determinar_final()` → Evaluación de finales
- [x] Comentarios esenciales en el código
- [x] README.md con instrucciones

### Características Opcionales ⭐

- [x] Sistema de **ayuda integrado** (comando `HELP`)
- [x] **Reproducibilidad** con `random.seed()` para demos
- [x] **ASCII art** decorativo (título, Minotauro, Teseo)
- [x] **Colores ANSI** para mejor visualización
- [x] **Campo de visión dinámico** (2 celdas de radio)
- [x] **Sistema de subefectos** aleatorios al recoger objetos

---

## 🏆 Sistema de Finales

Existen **10 finales posibles** según la combinación de objetos:

| Final | Nombre | Combinación Requerida |
|-------|--------|----------------------|
| A | Guerrero Supremo | Espada + Armadura Ligera + Lobo compañero |
| B | Mago Arcano | Anillo de Fuego + Varita de Luz + Fénix compañero |
| C | Guerrero Místico | Espada + Armadura Pesada + Báculo + Anillo de Agua |
| D | Explorador Protector | Armadura Pesada + Gato compañero + Varita de Sombra |
| E | Señor del Laberinto | Lanza + Escudo + Lobo compañero |
| F | Tecno-Mago | Anillo de Tierra + Báculo + Gato compañero |
| G | Paladín de la Luz | Espada + Armadura Ligera + Escudo + Anillo de Fuego |
| H | Guardián Elemental | Armadura Pesada + Anillo de Agua + Varita de Luz |
| I | Cazador Nocturno | Hacha + Gato compañero + Varita de Sombra |
| J | Maestro de Bestias | Lanza + Lobo compañero + Anillo de Tierra |

**Final de Derrota:** Si la combinación no coincide con ninguna anterior.

---

## 🛠️ Personalización

### Cambiar la Historia

Edita el archivo `context.json`:

```json
{
  "game_info": {
    "titulo": "Tu título aquí",
    "meta": "Tu objetivo aquí"
  },
  "lore_context": {
    "ubicacion": "Tu ubicación",
    "protagonista": "Tu héroe"
  }
}
```

### Agregar Nuevos Personajes

En `context.json`, dentro de `personajes_aliados.lista`, añade:

```json
{
  "id": "nuevo_personaje",
  "nombre": "Nombre del Personaje",
  "descripcion": "Descripción",
  "dialogo_encuentro": "Diálogo",
  "objetos_disponibles": [
    {
      "id": "objeto1",
      "nombre": "Objeto 1",
      "tipo": "tipo",
      "descripcion": "Descripción"
    }
  ]
}
```

### Crear Nuevos Finales

En `context.json`, dentro de `finales_posibles.finales`, añade:

```json
{
  "id": "final_nuevo",
  "nombre": "Final Nuevo: Título",
  "combinacion_requerida": ["Objeto 1", "Objeto 2", "Objeto 3"],
  "descripcion": "Breve descripción",
  "narrativa": "Narrativa completa del final"
}
```

### Modo Reproducible (para Demos)

En `laberinto_ASCII.py`, línea principal:

```python
# Modo normal (aleatorio)
juego = LaberintoAsterionASCII()

# Modo reproducible (siempre igual)
juego = LaberintoAsterionASCII(seed=42)
```

---

## 📊 Algoritmo Principal (Pseudocódigo)

```
INICIO
  1. Cargar configuración desde context.json
  2. Inicializar tablero 10×10
  3. Colocar jugador en posición (5, 5)
  4. Distribuir 5 personajes aleatoriamente
  5. Mostrar título y narrativa inicial
  
  MIENTRAS inventario < 5 Y jugador vivo:
    a. Mostrar estado del jugador
    b. Mostrar mapa con campo de visión
    c. SI hay personaje en celda actual ENTONCES
         i. Mostrar diálogo
         ii. Ofrecer 3 objetos
         iii. Jugador elige 1
         iv. Aplicar subefecto aleatorio
         v. Remover personaje del tablero
    FIN SI
    
    d. Solicitar movimiento (N/S/E/O/HELP)
    e. SI movimiento válido ENTONCES
         i. Actualizar posición
         ii. Consumir 1 unidad de Hilo de Ariadna
         iii. Marcar celda como visitada
    FIN SI
    
    f. Verificar condiciones de derrota:
       - Salud <= 0 → GAME OVER
       - Cordura <= 0 → GAME OVER
       - Hilo <= 0 → GAME OVER
  FIN MIENTRAS
  
  6. Evaluar combinación de objetos
  7. Mostrar final correspondiente (victoria o derrota)
FIN
```

---

## 🎓 Para el Informe (Entregable)

### Contenido Sugerido del PDF (1-2 páginas)

1. **Historia Breve**
   - Mitología del laberinto de Creta
   - Rol del protagonista (Teseo)
   
2. **Algoritmo/Pseudocódigo**
   - Ver sección anterior
   
3. **Decisiones de Diseño**
   - Tablero 10×10 para equilibrio exploración/tiempo
   - Campo de visión limitado para aumentar tensión
   - Sistema de finales por combinación para rejugabilidad
   - Hilo de Ariadna como límite de movimientos
   
4. **Captura de Pantalla**
   - Ejecutar el juego y capturar:
     - Pantalla de título
     - Mapa durante exploración
     - Encuentro con personaje
     - Pantalla de final
   
5. **Reflexión**
   - Qué aprendiste
   - Dificultades encontradas
   - Mejoras posibles

---

## 📦 Entregables (Resumen)

Para entregar en **Google Classroom**:

1. ✅ **Notebook (.ipynb)** que ejecute el juego
2. ✅ **Informe (.pdf)** de 1-2 páginas
3. ✅ **Archivos de código:**
   - `laberinto_ASCII.py`
   - `context.json`
4. ✅ **README.md** (este archivo)
5. ✅ **Captura(s) de pantalla** del juego funcionando

**Datos de entrega:**
- Nombre del proyecto
- Autor(es)
- Tiempo de ejecución usado
- Instrucciones para reproducir

---

## 🐛 Solución de Problemas

### Error: "No se encontró context.json"
- Asegúrate de que ambos archivos estén en el mismo directorio
- En Colab, sube ambos archivos a la sesión

### Los colores ANSI no se ven
- En Colab, los colores funcionan correctamente
- En Windows cmd, instala Windows Terminal o desactiva colores

### El juego se cierra inmediatamente
- Ejecuta desde terminal/Colab, no con doble clic
- Usa: `python laberinto_ASCII.py`

---

## 👨‍💻 Autor

Proyecto educativo basado en el mito griego del laberinto de Creta.  
Desarrollado como ejercicio de programación en Python.

---

## 📄 Licencia

Este proyecto es de uso educativo. Siéntete libre de modificarlo y personalizarlo para tu aprendizaje.

---

## 🌟 Mejoras Futuras Sugeridas

- [ ] Añadir enemigos que patrullen el laberinto
- [ ] Sistema de combate por turnos
- [ ] Objetos consumibles (pociones)
- [ ] Puertas con llaves
- [ ] Mini-misiones de NPCs neutrales
- [ ] Guardar/cargar partida
- [ ] Música y efectos de sonido
- [ ] Tablero dinámico (generación procedural)

---

**¡Buena suerte en tu aventura por el laberinto! 🏛️⚔️🐂**
