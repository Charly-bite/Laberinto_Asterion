# 🏛️ El Laberinto de Asterión

**Aventura Interactiva de Teseo**

Un juego de aventura basado en texto que recrea la leyenda del Minotauro de Creta. Explora un laberinto de 10×10, encuentra aliados, recolecta objetos legendarios y enfrenta a Asterión en un combate épico.

## 📋 Descripción

Eres **Teseo**, héroe de Atenas que se ofrece como tributo para liberar a su pueblo de la maldición del Minotauro. Debes navegar por el laberinto de Dédalo en el Palacio de Cnosos, encontrar 5 aliados dispersos, elegir sabiamente tus objetos legendarios y enfrentar a **Asterión** (El Minotauro) con la combinación correcta de equipo.

## 🎮 Versiones Disponibles

Este proyecto tiene **dos versiones** del juego:

### 1️⃣ Versión Original (Paso 1)
**Archivo:** `laberinto_asterion.py`

Versión funcional básica con:
- ✅ Sistema completo de juego
- ✅ Símbolos ASCII simples
- ✅ Máxima compatibilidad
- ✅ Código limpio y educativo

```bash
python3 laberinto_asterion.py
```

### 2️⃣ Versión ASCII Art (Paso 2)
**Directorio:** `versionASCII/`

Versión mejorada con experiencia visual:
- ✨ Colores ANSI (16 colores)
- 🎨 ASCII Art impresionante
- 🗺️ Mapa visual del laberinto
- ⌨️ Animaciones de texto
- 🎭 Interfaz interactiva

```bash
cd versionASCII
python3 laberinto_ASCII.py
```

📖 **[Ver comparación detallada](COMPARACION.md)**

## 🚀 Inicio Rápido

### Requisitos
- Python 3.6 o superior
- No requiere dependencias externas
- Terminal con soporte ANSI (para versión ASCII)

### Instalación

```bash
# Clonar o descargar el proyecto
cd Laberinto_Creta

# Ejecutar versión original
python3 laberinto_asterion.py

# O ejecutar versión ASCII
cd versionASCII
python3 laberinto_ASCII.py
```

## 📁 Estructura del Proyecto

```
Laberinto_Creta/
├── context.json              # Configuración completa del juego
├── laberinto_asterion.py     # Versión original (Paso 1)
├── COMPARACION.md            # Comparación entre versiones
├── README.md                 # Este archivo
└── versionASCII/
    ├── laberinto_ASCII.py    # Versión mejorada (Paso 2)
    └── README_ASCII.md       # Documentación versión ASCII
```

## 🎯 Características del Juego

### Sistema de Configuración JSON
- Todo el juego se configura desde `context.json`
- Fácil de modificar y personalizar
- Separación clara entre datos y lógica

### 10 Finales Diferentes
Dependiendo de la combinación exacta de objetos que recolectes:
1. **Guerrero Supremo** - Espada + Armadura Ligera + Lobo compañero
2. **Mago Arcano** - Anillo de Fuego + Varita de Luz + Fénix compañero
3. **Guerrero Místico** - Espada + Armadura Pesada + Báculo + Anillo de Agua
4. **Explorador Protector** - Armadura Pesada + Gato compañero + Varita de Sombra
5. **Señor del Laberinto** - Lanza + Escudo + Lobo compañero
6. **Tecno-Mago** - Anillo de Tierra + Báculo + Gato compañero
7. **Paladín de la Luz** - Espada + Armadura Ligera + Escudo + Anillo de Fuego
8. **Guardián Elemental** - Armadura Pesada + Anillo de Agua + Varita de Luz
9. **Cazador Nocturno** - Hacha + Gato compañero + Varita de Sombra
10. **Maestro de Bestias** - Lanza + Lobo compañero + Anillo de Tierra

### 5 Personajes Aliados Únicos

| Personaje | Objetos Disponibles |
|-----------|---------------------|
| **Guerrero de Creta** | Espada, Hacha, Lanza |
| **Guardián del Palacio** | Armadura Ligera, Armadura Pesada, Escudo |
| **Comerciante Fenicio** | Anillo de Fuego, Anillo de Agua, Anillo de Tierra |
| **Mago de Delfos** | Varita de Luz, Varita de Sombra, Báculo |
| **Druida Semihumano** | Lobo compañero, Fénix compañero, Gato compañero |

### Sistema de Estadísticas
- **Salud**: 100 puntos iniciales
- **Cordura**: 100 puntos iniciales
- **Hilo de Ariadna**: 500 unidades (1 por movimiento)
- **Puntos**: Acumulados por eventos aleatorios

### Eventos Aleatorios
Cada vez que recoges un objeto:
- 📦 Encuentras monedas antiguas (+5 puntos)
- 💰 Descubres un tesoro escondido (+10 puntos)
- 🗡️ Una trampa te hiere levemente (-1 salud)
- 🌿 Encuentras hierbas curativas (+1 salud)

## 🎮 Cómo Jugar

### Controles
- **N**: Mover al Norte
- **S**: Mover al Sur
- **E**: Mover al Este
- **O**: Mover al Oeste
- **1-3**: Elegir objeto cuando encuentras un aliado

### Objetivo
1. Explorar el laberinto de 10×10 celdas
2. Encontrar los 5 aliados dispersos aleatoriamente
3. Elegir 1 objeto de cada aliado (¡elige sabiamente!)
4. Llegar al centro con la combinación correcta
5. Derrotar a Asterión y escapar del laberinto

### Condiciones de Victoria
- Recolectar 5 objetos (uno de cada personaje)
- Lograr una combinación válida para un final

### Condiciones de Derrota
- Salud llega a 0
- Cordura llega a 0
- Hilo de Ariadna se agota completamente

## 🛠️ Personalización

Puedes modificar `context.json` para personalizar:

```json
{
  "jugador": {
    "stats_base": {
      "salud": 100,        // Cambia la salud inicial
      "cordura": 100,      // Cambia la cordura inicial
      "puntos": 0
    }
  },
  "personajes_aliados": {
    "lista": [
      // Modifica personajes, objetos, diálogos...
    ]
  },
  "finales_posibles": {
    "finales": [
      // Crea nuevos finales o modifica existentes
    ]
  }
}
```

## 📊 Comparación de Versiones

| Característica | Original | ASCII Art |
|----------------|----------|-----------|
| Funcionalidad | ✅ Completa | ✅ Completa |
| Colores | ❌ No | ✅ Sí |
| ASCII Art | ❌ No | ✅ Sí |
| Mapa visual | ❌ No | ✅ Sí |
| Animaciones | ❌ No | ✅ Sí |
| Compatibilidad | Universal | Terminales ANSI |

Ver **[COMPARACION.md](COMPARACION.md)** para detalles completos.

## 🎨 Capturas de Pantalla

### Versión Original
```
============================================================
  EL LABERINTO DE ASTERIÓN
  Aventura Interactiva de Teseo
============================================================

[*] Ubicación: Palacio de Cnosos, Creta
[!] Protagonista: Teseo, héroe de Atenas
[X] Enemigo: Asterión (El Minotauro)
```

### Versión ASCII Art
```
╔═══════════════════════════════════════════════════════════════════╗
║   ███████╗██╗         ██╗      █████╗ ██████╗ ███████╗██████╗    ║
║   ██╔════╝██║         ██║     ██╔══██╗██╔══██╗██╔════╝██╔══██╗   ║
║   █████╗  ██║         ██║     ███████║██████╔╝█████╗  ██████╔╝   ║
╚═══════════════════════════════════════════════════════════════════╝

[Colores ANSI + Mapa Visual + Animaciones]
```

## 🔮 Roadmap del Proyecto

- [x] **Paso 1**: Código Python que lee `context.json` ✅
- [x] **Paso 2**: Versión interactiva con colores y ASCII art ✅
- [ ] **Paso 3**: Mecánicas adicionales (cordura activa, encuentros con Minotauro)
- [ ] **Paso 4**: Versión web con interfaz gráfica

## 📝 Notas Técnicas

### Símbolos Utilizados

```
[*]  - Información/Ubicación
[!]  - Protagonista/Acción
[X]  - Enemigo/Peligro
[>]  - Objetivo/Dirección
[@]  - Jugador
[HP] - Salud (Health Points)
[CD] - Cordura
[--] - Hilo de Ariadna
[**] - Puntos
[##] - Inventario
[+]  - Encuentro positivo
[?]  - Opciones/Aleatorio
[OK] - Confirmación
[!]  - Error/Advertencia
```

### Compatibilidad
- **Linux**: ✅ Totalmente compatible
- **macOS**: ✅ Totalmente compatible
- **Windows**: ✅ Compatible (CMD/PowerShell/Windows Terminal)

## 📜 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 🙏 Créditos

Basado en la leyenda griega del Minotauro y el héroe Teseo.

**Desarrollo:**
- Paso 1: Sistema base con `context.json`
- Paso 2: Mejoras visuales con ASCII art y colores

---

**¡Que los dioses te acompañen en tu aventura, héroe!** ⚔️🏛️

## 🆘 Soporte

Si encuentras problemas:
1. Verifica que tienes Python 3.6+
2. Asegúrate de que `context.json` está en el directorio correcto
3. Para la versión ASCII, verifica que tu terminal soporte colores ANSI

**¿Preguntas?** Revisa la documentación en cada directorio.
