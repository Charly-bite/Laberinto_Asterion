# 📊 Comparación de Versiones - El Laberinto de Asterión

## Estructura del Proyecto

```
Laberinto_Creta/
├── context.json                    # Configuración del juego (compartida)
├── laberinto_asterion.py          # Versión original (Paso 1)
├── README.md                       # Documentación general
└── versionASCII/
    ├── laberinto_ASCII.py         # Versión mejorada (Paso 2)
    └── README_ASCII.md            # Documentación de la versión ASCII
```

## 🔄 Comparación de Características

| Característica | Versión Original | Versión ASCII Art |
|----------------|------------------|-------------------|
| **Funcionalidad Core** | ✅ Completa | ✅ Completa |
| **Lee context.json** | ✅ Sí | ✅ Sí |
| **5 Personajes** | ✅ Sí | ✅ Sí |
| **10 Finales** | ✅ Sí | ✅ Sí |
| **Sistema de inventario** | ✅ Sí | ✅ Sí |
| **Subefectos aleatorios** | ✅ Sí | ✅ Sí |
| | | |
| **Colores ANSI** | ❌ No | ✅ Sí (16 colores) |
| **ASCII Art** | ❌ No | ✅ Sí (Título + Minotauro) |
| **Mapa visual** | ❌ No | ✅ Sí (10×10 en tiempo real) |
| **Animaciones** | ❌ No | ✅ Sí (Texto animado) |
| **Pantalla limpia** | ❌ No | ✅ Sí (Entre turnos) |
| **Barras de estado** | ❌ No | ✅ Sí (Coloreadas dinámicamente) |
| **Efectos de sonido** | ❌ No | ❌ No (futuro) |
| **Tracking de visitados** | ❌ No | ✅ Sí (Mapa persistente) |
| | | |
| **Tamaño del archivo** | ~11 KB | ~23 KB |
| **Líneas de código** | ~310 | ~580 |
| **Dependencias** | Solo stdlib | Solo stdlib |
| **Compatibilidad** | Universal | Terminales ANSI |

## 🎨 Comparación Visual

### Versión Original (laberinto_asterion.py)

```
============================================================
  EL LABERINTO DE ASTERIÓN
  Aventura Interactiva de Teseo
============================================================

[*] Ubicación: Palacio de Cnosos, Creta
[!] Protagonista: Teseo, héroe de Atenas
[X] Enemigo: Asterión (El Minotauro)

[>] Objetivo: Encontrar los 5 personajes aliados...

────────────────────────────────────────────────────────────
[@] Teseo | [HP] Salud: 100 | [CD] Cordura: 100 | [--] Hilo: 500 | [**] Puntos: 0
[##] Inventario (0/5): Vacío
────────────────────────────────────────────────────────────

[*] Posición actual: Sala (5, 5)
   Esta sala está vacía. Continúa explorando...

[^] Direcciones disponibles:
   N (Norte) | S (Sur) | E (Este) | O (Oeste)

Elige dirección:
```

### Versión ASCII Art (laberinto_ASCII.py)

```
[AMARILLO BRILLANTE]
╔═══════════════════════════════════════════════════════════════════╗
║   ███████╗██╗         ██╗      █████╗ ██████╗ ███████╗██████╗    ║
║   ██╔════╝██║         ██║     ██╔══██╗██╔══██╗██╔════╝██╔══██╗   ║
║   █████╗  ██║         ██║     ███████║██████╔╝█████╗  ██████╔╝   ║
║   ██╔══╝  ██║         ██║     ██╔══██║██╔══██╗██╔══╝  ██╔══██╗   ║
║   ███████╗███████╗    ███████╗██║  ██║██████╔╝███████╗██║  ██║   ║
║   ╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ║
║              ██████╗ ███████╗                                     ║
║          █████╗ ███████╗████████╗███████╗██████╗ ██╗ ██████╗ ███╗║
╚═══════════════════════════════════════════════════════════════════╝
[RESET]

[BLANCO BRILLANTE]══════════════════════════════════════════════════════════════════════[RESET]
[CYAN][*] Ubicación:[RESET] Palacio de Cnosos, Creta
[VERDE][!] Protagonista:[RESET] Teseo, héroe de Atenas
[ROJO][X] Enemigo:[RESET] Asterión (El Minotauro)

[AMARILLO][>] Objetivo:[RESET] Encontrar los 5 personajes aliados...
[BLANCO BRILLANTE]══════════════════════════════════════════════════════════════════════[RESET]

[BLANCO BRILLANTE]──────────────────────────────────────────────────────────────────────[RESET]
[CYAN BRILLANTE][@] Teseo[RESET]
  [VERDE BRILLANTE][HP][RESET] Salud: [VERDE BRILLANTE]100/100[RESET] | [CYAN BRILLANTE][CD][RESET] Cordura: [CYAN BRILLANTE]100/100[RESET]
  [MAGENTA BRILLANTE][--][RESET] Hilo: 500 | [AMARILLO BRILLANTE][**][RESET] Puntos: 0
  [VERDE BRILLANTE][##][RESET] Inventario (0/5): [NEGRO BRILLANTE]Vacío[RESET]
[BLANCO BRILLANTE]──────────────────────────────────────────────────────────────────────[RESET]

[CYAN BRILLANTE]╔══════════════════════════════════════════╗[RESET]
[CYAN BRILLANTE]║[BLANCO BRILLANTE]          MAPA DEL LABERINTO          [CYAN BRILLANTE]║[RESET]
[CYAN BRILLANTE]╠══════════════════════════════════════════╣[RESET]
[CYAN BRILLANTE]║[RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [CYAN BRILLANTE]║[RESET]
[CYAN BRILLANTE]║[RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [CYAN BRILLANTE]║[RESET]
[CYAN BRILLANTE]║[RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [CYAN BRILLANTE]║[RESET]
[CYAN BRILLANTE]║[RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [CYAN BRILLANTE]║[RESET]
[CYAN BRILLANTE]║[RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [CYAN BRILLANTE]║[RESET]
[CYAN BRILLANTE]║[RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [VERDE BRILLANTE][@][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [CYAN BRILLANTE]║[RESET]
[CYAN BRILLANTE]║[RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [CYAN BRILLANTE]║[RESET]
[CYAN BRILLANTE]║[RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [CYAN BRILLANTE]║[RESET]
[CYAN BRILLANTE]║[RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [CYAN BRILLANTE]║[RESET]
[CYAN BRILLANTE]║[RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [DIM][#][RESET] [CYAN BRILLANTE]║[RESET]
[CYAN BRILLANTE]╚══════════════════════════════════════════╝[RESET]

[BLANCO BRILLANTE]Leyenda:[RESET]
  [VERDE BRILLANTE][@][RESET] Teseo  [AMARILLO BRILLANTE][?][RESET] Aliado  [NEGRO BRILLANTE][·][RESET] Visitado  [DIM][#][RESET] Desconocido

[CYAN BRILLANTE][*] Posición actual:[RESET] Sala (5, 5)
   [NEGRO BRILLANTE]Esta sala está vacía. Continúa explorando...[RESET]

[CYAN BRILLANTE][^] Direcciones disponibles:[RESET]
   [BLANCO BRILLANTE]N[RESET] (Norte) | [BLANCO BRILLANTE]S[RESET] (Sur) | [BLANCO BRILLANTE]E[RESET] (Este) | [BLANCO BRILLANTE]O[RESET] (Oeste)

[AMARILLO BRILLANTE]Elige dirección: [RESET]
```

## 🎯 Cuándo Usar Cada Versión

### Usa la Versión Original si:
- ✅ Necesitas máxima compatibilidad
- ✅ Prefieres salida simple y directa
- ✅ Estás en un terminal sin soporte ANSI
- ✅ Quieres menor uso de recursos
- ✅ Prefieres código más simple para aprender

### Usa la Versión ASCII Art si:
- ✅ Quieres la mejor experiencia visual
- ✅ Tienes un terminal moderno con soporte ANSI
- ✅ Prefieres una interfaz más inmersiva
- ✅ Quieres ver el mapa del laberinto
- ✅ Disfrutas de los efectos visuales y animaciones

## 📈 Rendimiento

| Métrica | Versión Original | Versión ASCII |
|---------|------------------|---------------|
| Tiempo de inicio | ~0.1s | ~0.2s |
| Memoria RAM | ~15 MB | ~18 MB |
| CPU por turno | Mínimo | Bajo |
| Refresco de pantalla | No | Sí (cada turno) |

## 🔮 Futuras Mejoras

### Paso 3: Mecánicas Avanzadas
- Sistema de cordura activo
- Encuentros con el Minotauro
- Sistema de combate
- Trampas y eventos aleatorios

### Paso 4: Versión Web
- Interfaz gráfica HTML/CSS/JS
- Sprites y animaciones
- Música y efectos de sonido
- Guardado de progreso

---

**Ambas versiones son completamente funcionales y comparten el mismo `context.json`** 🎮
