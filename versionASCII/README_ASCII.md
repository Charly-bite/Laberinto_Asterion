# 🎨 El Laberinto de Asterión - Versión ASCII Art

**Versión mejorada con colores ANSI y arte ASCII**

Esta es la versión visual mejorada del juego con:
- ✨ Colores ANSI para mejor experiencia visual
- 🎨 ASCII Art para título y elementos gráficos
- 🗺️ Mapa visual del laberinto en tiempo real
- ⌨️ Animaciones de texto tipo "máquina de escribir"
- 🎭 Interfaz interactiva mejorada

## 🚀 Cómo Ejecutar

```bash
cd versionASCII
python3 laberinto_ASCII.py
```

## 🎮 Características Visuales

### Colores por Elemento

| Elemento | Color | Significado |
|----------|-------|-------------|
| **Salud** | Verde/Amarillo/Rojo | >60% / 30-60% / <30% |
| **Cordura** | Cyan/Amarillo/Rojo | >60% / 30-60% / <30% |
| **Hilo de Ariadna** | Magenta | Recurso de navegación |
| **Puntos** | Amarillo | Puntuación acumulada |
| **Inventario** | Verde/Cyan | <5 objetos / 5 objetos |
| **Personajes** | Verde brillante | Encuentros positivos |
| **Enemigo** | Rojo brillante | Peligro |
| **Narrativa** | Blanco/Cyan | Texto de historia |

### Mapa del Laberinto

El mapa se actualiza en tiempo real mostrando:

```
╔══════════════════════════════════════════╗
║          MAPA DEL LABERINTO          ║
╠══════════════════════════════════════════╣
║ [#] [#] [#] [#] [#] [#] [#] [#] [#] [#] ║
║ [#] [·] [·] [?] [#] [#] [#] [#] [#] [#] ║
║ [#] [·] [@] [·] [#] [#] [#] [#] [#] [#] ║
║ [#] [#] [#] [#] [#] [#] [#] [#] [#] [#] ║
...
╚══════════════════════════════════════════╝

Leyenda:
  [@] Teseo  [?] Aliado  [·] Visitado  [#] Desconocido
```

### ASCII Art

#### Título del Juego
```
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   ███████╗██╗         ██╗      █████╗ ██████╗ ███████╗██████╗    ║
║   ██╔════╝██║         ██║     ██╔══██╗██╔══██╗██╔════╝██╔══██╗   ║
║   █████╗  ██║         ██║     ███████║██████╔╝█████╗  ██████╔╝   ║
║   ██╔══╝  ██║         ██║     ██╔══██║██╔══██╗██╔══╝  ██╔══██╗   ║
║   ███████╗███████╗    ███████╗██║  ██║██████╔╝███████╗██║  ██║   ║
║   ╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ║
║                                                                   ║
║              ██████╗ ███████╗                                     ║
║              ██╔══██╗██╔════╝                                     ║
║              ██║  ██║█████╗                                       ║
║              ██║  ██║██╔══╝                                       ║
║              ██████╔╝███████╗                                     ║
║              ╚═════╝ ╚══════╝                                     ║
║                                                                   ║
║          █████╗ ███████╗████████╗███████╗██████╗ ██╗ ██████╗ ███╗║
║         ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║██╔═══██╗████║
║         ███████║███████╗   ██║   █████╗  ██████╔╝██║██║   ██║██╔█║
║         ██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗██║██║   ██║██║╚║
║         ██║  ██║███████║   ██║   ███████╗██║  ██║██║╚██████╔╝██║ ║
║         ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝ ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

#### El Minotauro
Se muestra en el enfrentamiento final con arte ASCII impresionante.

## 🎯 Mejoras Visuales

### 1. **Pantalla Limpia**
- La pantalla se limpia entre turnos para mejor legibilidad
- Información organizada en secciones claras

### 2. **Barras de Estado Coloreadas**
- Salud: Verde → Amarillo → Rojo según el porcentaje
- Cordura: Cyan → Amarillo → Rojo según el porcentaje
- Feedback visual inmediato del estado del jugador

### 3. **Animaciones de Texto**
- Efecto de "máquina de escribir" para diálogos
- Pausas dramáticas en momentos clave
- Transiciones suaves entre escenas

### 4. **Mapa Interactivo**
- Muestra tu posición actual en tiempo real
- Marca las salas visitadas
- Indica dónde hay aliados sin descubrir
- Ayuda a navegar el laberinto

### 5. **Código de Colores Consistente**
```
[*]  Cyan    - Información/Ubicación
[!]  Verde   - Protagonista/Acción
[X]  Rojo    - Enemigo/Peligro
[>]  Amarillo - Objetivo/Dirección
[@]  Cyan    - Jugador
[HP] Variable - Salud (Verde/Amarillo/Rojo)
[CD] Variable - Cordura (Cyan/Amarillo/Rojo)
[--] Magenta - Hilo de Ariadna
[**] Amarillo - Puntos
[##] Verde   - Inventario
[+]  Verde   - Encuentro positivo
[?]  Magenta - Opciones/Aleatorio
[OK] Verde   - Confirmación
[ERR] Rojo   - Error
[WIN] Verde  - Victoria
[XXX] Rojo   - Derrota
```

## 🎬 Experiencia de Juego

### Inicio
1. Título ASCII art impresionante
2. Información del contexto con colores
3. Animación de texto para la introducción

### Durante el Juego
1. Estado del jugador con barras de color
2. Mapa visual actualizado en tiempo real
3. Posición actual destacada
4. Encuentros con personajes con diálogos animados
5. Feedback visual de cada acción

### Final
1. Arte ASCII del Minotauro
2. Narrativa del enfrentamiento con animación
3. Resultado final con colores dramáticos
4. Puntuación final destacada

## 💻 Requisitos

- Python 3.6+
- Terminal con soporte ANSI (la mayoría de terminales modernas)
- Archivo `context.json` en el directorio padre

## 🎨 Personalización

Puedes modificar los colores editando la clase `Color` en el archivo:

```python
class Color:
    # Personaliza estos valores
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_RED = '\033[91m'
    # ... etc
```

## 📝 Notas

- **Mejor experiencia**: Terminal de pantalla completa
- **Colores**: Algunos terminales pueden mostrar colores ligeramente diferentes
- **Velocidad de texto**: Ajustable en la función `escribir_lento()`
- **Compatibilidad**: Funciona en Linux, macOS y Windows (con terminal compatible)

## 🔄 Diferencias con la Versión Original

| Característica | Versión Original | Versión ASCII |
|----------------|------------------|---------------|
| Colores | ❌ No | ✅ Sí (ANSI) |
| Mapa visual | ❌ No | ✅ Sí |
| ASCII Art | ❌ No | ✅ Sí |
| Animaciones | ❌ No | ✅ Sí |
| Pantalla limpia | ❌ No | ✅ Sí |
| Barras de estado | ❌ No | ✅ Sí (coloreadas) |

---

**¡Disfruta de la aventura visual en el Laberinto de Asterión!** 🏛️⚔️
