# Laberinto de Asterión

Una aventura interactiva basada en el mito del Minotauro, implementada en Python con interfaz CLI y web.

## 🎮 Características

- **Versión CLI**: Juego completo con ASCII art y colores ANSI
- **Versión Web**: Interfaz de terminal en el navegador que replica exactamente la salida de la CLI
- **Sistema de combate**: Enfréntate al Minotauro con múltiples estrategias
- **Múltiples finales**: Tus decisiones determinan el destino de Teseo

## 🚀 Despliegue en Render.com

### Configuración Rápida

1. **Crear nuevo Web Service** en Render.com
2. **Conectar repositorio**: `https://github.com/Charly-bite/Laberinto_Asterion`
3. **Configuración**:
   - **Name**: `laberinto-asterion`
   - **Language**: `Python 3`
   - **Branch**: `main`
   - **Root Directory**: (dejar vacío)
   - **Build Command**: `pip install -r web_app/requirements.txt`
   - **Start Command**: `./start.sh`

### Variables de Entorno

No se requieren variables de entorno especiales.

## 💻 Ejecución Local

### Versión CLI

```bash
cd versionASCII
python3 laberinto_ASCII.py
```

### Versión Web

```bash
cd web_app
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Luego abre http://localhost:5000 en tu navegador.

## 📁 Estructura del Proyecto

```
Laberinto_Creta/
├── versionASCII/          # Versión CLI con ASCII art
│   ├── laberinto_ASCII.py
│   └── context.json
├── web_app/               # Aplicación web
│   ├── app.py
│   ├── templates/
│   └── static/
├── Version1/              # Versión original
└── README.md
```

## 🎯 Cómo Jugar

1. Explora el laberinto usando los comandos N, S, E, O
2. Encuentra a los 5 aliados dispersos
3. Elige sabiamente los objetos que te ofrecen
4. Enfrenta al Minotauro con la estrategia correcta
5. Escapa del laberinto... si puedes

## 📝 Contributing
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
