"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  PROYECTO: Aventura Interactiva "El laberinto de la mazmorra"                ║
║  Base técnica: Python / Google Colab                                         ║
║  Duración: 5 días hábiles                                                    ║
║                                                                              ║
║  OBJETIVO:                                                                   ║
║  Tomar el código base (Colab) y convertirlo en un proyecto personalizable    ║
║  que demuestre dominio de listas, condicionales, ciclos, funciones y         ║
║  estructura básica de programas.                                             ║
║                                                                              ║
║  REQUISITOS IMPLEMENTADOS:                                                   ║
║    Historia personalizable (context.json)                                    ║
║    5 personajes aliados con 3 objetos cada uno                               ║
║    Sistema de finales por combinación                                        ║
║    Mensajes legibles en consola                                              ║
║    Lógica separada en funciones                                              ║
║    Comentarios esenciales                                                    ║
║    Sistema de ayuda (comando 'help')                                         ║
║    Reproducibilidad con random.seed()                                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import json
import random
import time
import os
import sys
from pathlib import Path


# ==================== COLORES ANSI ====================
class Color:
    """Códigos de color ANSI para terminal"""
    # Colores básicos
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    
    # Colores de texto
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Colores brillantes
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Fondos
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'


# ==================== ASCII ART ====================
ASCII_TITLE = f"""{Color.BRIGHT_YELLOW}
 ▗▄▖  ▄▄▄  ■  ▗▞▀▚▖ ▄▄▄ ▄  ▄▄▄  ▄▄▄▄  
▐▌ ▐▌▀▄▄▗▄▟▙▄▖▐▛▀▀▘█    ▄ █   █ █   █ 
▐▛▀▜▌▄▄▄▀ ▐▌  ▝▚▄▄▖█    █ ▀▄▄▄▀ █   █ 
▐▌ ▐▌     ▐▌            █             
          ▐▌                          
                                                                                                                                                                           
{Color.RESET}"""

MINOTAURO_ASCII = Color.BRIGHT_RED + """
              -"\\
    .-"  .`)     (
   j   .'_+     :[                )      .^--..
  i    -"       |l                ].    /      i
 ," .:j         `8o  _,,+.,.--,   d|   `:::;    b
 i  :'|          "88p;.  (-."_"-.oP        \\.   :
 ; .  (            >,%%%   f),):8"          \\:'  i
i  :: j          ,;%%%:; ; ; i:%%%.,        i.   `.
i  `: ( ____  ,-::::::' ::j  [:```          [8:   )
<  ..``'::::8888oooooo.  :(jj(,;,,,         [8::  <
`. ``:.      oo.8888888888:;%%%8o.::.+888+o.:`:'  |
 `.   `        `o`88888888b`%%%%%88< Y888P""'-    ;
   "`---`.       Y`888888888;;.,"888b.\\"\\"\\".."
          "-....  b`8888888:::::.`8888._::-"
             `:::. `:::::O:::::::.`%%'|
              `.      "``::::::''    .'
                `.                   <
                  +:         `:   -';
                   `:         : .::/
                    ;+_  :::. :..;;;      
                    ;;;;,;;;;;;;;,;;
""" + Color.RESET

TESEO_ASCII = f"""{Color.BRIGHT_CYAN}

              .
             /.\
             |.|
             |.|
             |.|
             |.|   ,'`.
             |.|  ;\  /:
             |.| /  \/  \
             |.|<.<_\/_>,>
             |.| \`.::,'/
             |.|,'.'||'/.
          ,-'|.|.`.____,'`.
        ,' .`|.| `.____,;/ \
       ,'=-.`|.|\ .   \ |,':
      /_   :)|.|.`.___:,:,'|.
     (  `-:;\|.|.`.)  |.`-':,\
     /.   /  ;.:--'   |    | ,`.
    / _>-'._.'-'.     |.   |' / )._
   :.'    ((.__;/     |    |._ /__ `.___
   `.>._.-' |)=(      |.   ;  '--.._,`-.`.
            ',--'`-._ | _,:          `='`'
            /_`-. `..`:'/_.\
           :__``--..\\_/_..:
           |  ``--..,:;\__.|
           |`--..__/:;  :__|
           `._____:-;_,':__;
            |:'    /::'  `|
            |,---.:  :,-'`;
            : __  )  ;__,'\
            \' ,`/   \__  :
            :. |,:   :  `./
            | `| |   |   |:
            |  | |   |   ||
            |  | |   |   ||
            |  | |   '   ||
            |  : |    \  ||
            |  ; :    :  ||
            | / ,;    |\,'`.
            ;-.(,'    '-._,-`.
          ,'-.//          `--' 
          `---'

{Color.RESET}"""

TESEO_DERROTADO_ASCII = Color.BRIGHT_RED + r"""
                                                                _
                                                              _( (~\
       _ _                        /                          ( \> > \
   -/~/ / ~\                     :;                \       _  > /(~\/
  || | | /\ ;\                   |l      _____     |;     ( \/ /   /
  _\)\)\)/ ;;;                  `8o __-~     ~\   d|      \   \  //
 ///(())(__/~;;\                  "88p;.  -. _\_;.oP        (_._/ /
(((__   __ \   \                  `>,% (\  (\./)8"         ;:'  i
)))--`.'-- (( ;,8 \               ,;%%%:  ./V^^^V'          ;.   ;.
((\   |   /)) .,88  `: ..,,;;;;,-::::::'_::\   ||\         ;[8:   ;
 )|  ~-~  |(|(888; ..``'::::8888oooooo.  :\`^^^/,,~--._    |88::| |
  \ -===- /|  \8;; ``:.      oo.8888888888:`((( o.ooo8888Oo;:;:'  |
 |_~-___-~_|   `-\.   `        `o`88888888b` )) 888b88888P""'     ;
  ;~~~~;~~         "`--_`.       b`888888888;(.,"888b888"  ..::;-'
   ;      ;              ~"-....  b`8888888:::::.`8888. .:;;;''
      ;    ;                 `:::. `:::OOO:::::::.`OO' ;;;''
 :       ;                     `.      "``::::::''    .'
    ;                           `.   \_              /
  ;       ;                       +:   ~~--  `:'  -';
                                   `:         : .::/
      ;                            ;;+_  :::. :..;;;

    "El héroe cayó ante      
     la furia del Minotauro"
     
        ⚰️  R.I.P. Teseo  ⚰️      
""" + Color.RESET

TESEO_VENCIDO_ASCII = Color.RED + r"""

            .-'''''-.
          .-'    '-.
       .-'  :::::_:::::  '-.
   ___/ ==:...:::-:::...:== \___
  /_____________________________\
':'-._________________________.-'_
 ':::\ @-,`-[-][-^-][-]-`,-@ / _| |_
  '::| .-------------------. ||_ @ _|
   ::|=|*   ___  _  ___   *|=|'.| |
   ':| |'   ))_) )) ))_)  '| |::.^|
   _:|=|'  ((`\ (( ((     '|=|::::::.
 _| || |' TESEO DE ATENAS '| |:::::::.
|_   |=|'      _( )'       |= |':::::.
  | || |' (   (_ ~ _)   ) '| | ':::'
  |^||=|*  )    (_)    (  *|=| '::'
     | '-------------------' .::::'
     |_____________________.::::::'
   .'___________________.::::::''
   |_______________.::::'':::'''
 .'_____________.::::::''::::''
            .:::'''' :::: .'::::'
         .:::::''':.   .:::::'

""" + Color.RESET

TESEO_VICTORIOSO_ASCII = Color.BRIGHT_GREEN + r"""

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%%%%%S#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+,.:....:,,;+?#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@S*:,,;:;*???*?+;;...;%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+,::+%#@@@@@@@@@@@S*:.::%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,.:%#@@@@@@@@@@@@@@@@@S+..;#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:,*@@@@@@@@@@@@@@@@@@@@@@S:,;#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?.,S@@@@@@@@@@@@@@@@@@@@@@@@@+.:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:,?@@@@@@@@@@@@@@@@@@@@@@@@@@@:,?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,+@@@@@@@@@@@@@@@@@@@@@@@@@@@@S,:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?.%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*,S@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:S@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+;#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?;#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:#@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*,S@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;,@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*,S@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;,#@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@?:S@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;:#@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@+,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+,#@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@+.S@@@@@@@@@@@@@##@@@@@@@@@@@@@@;,#@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@*,S@@@@@@@@@@@@%?S%#@@@@@@@@@@@@;:#@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:#@@@@@@@@@@@@%@@S#@@@@@@@@@@@@+:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+,S@@@@@@@@@@@@SS@%@@@@@@@@@@@@@;:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:S@@@@@@@@@@#%S@@#SS#@@@@@@@@@@;;#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@*:#@@@@@@@@#S#@@@@@@@#%@@@@@@@@@+:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@+.S@@@@@@@@S@@@@@@@@@@#S@@@@@@@@;.#@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@+.S@@@@@@@@?@@@@@@@@@@@%@@@@@@@@;.#@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@*,S@@@@@@@#S@S@@@@@@#####@@@@@@@+:###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+,#@@@@@@@S@S#S@@@@@S@S@S@@@@@@@+:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+,S@@@@@@@#@###@@@@@##@###@@@@@@;,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*,S@@@@@@##S#S@@@@@@@S@###@@@@@@+:#@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@*;S@@@@@#S#S##@@@@@@@S@#@#@@@@@@;,#@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@+,S@@@@#*:*###@@@@@@@#@#@#@@@@@@;.#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@+,S@@@S+,+%#@#@@@@@@@@@#@#@@@@@@;.#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@+:S@#%:,*#@@@##@@S#@@#@#@#@@@@@@;,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@+:S#*,:%@@@@@@%@@SS@#S@@#@@@@@@@+:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.*;,+S@@@@@@@%#@#S@S#@@#@@@@@@@;:#@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;.,,*#@@@@@@@@%@@S#@S#@#@@@@@@@@;:#@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;,;%@@@@@@@@@@S#@##@#@#@@@@@@@@@+:#@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.S@@@@@@@@@@@@#@@S#@@@#@@@@@@@@;,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.?%SS#######S#%@###SS#%%%%%%%%%:.#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*;++**?***+;:::;S###?????******++;@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@#S??%%??****?#%?****S@#S@?+:;:;*?*****????%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@#SSS#@@#S%%?;*++*%@@@@S#@@@SSSSSS%;,,,,,,,,,:;*%#@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@#%*;;;;;;;;;;;;;;;+S@@@@#S@@@@@@@@@@@@%;;%#%::*SS#######S##@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@#%?+;:,,,,,,,,,,,,,,,::+**%@@@#@@@@@@@@@@@@??S@@#???#@?**???????********?S#@@@@@@@@@@@@@
@@@@@@@S%*;,...................,:,....:#@@@@@@@@@@@@@@@@@@@@@@@@@@#*,.................,:+*%#@@@@@@@@
@@@@@@S%%%%%%%%%%%%%%%%%%%%%%%%S%%%%%%%%S#@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%SSS?S@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@S?S@@@@
                 
            🏛️  TESEO VICTORIOSO  🏛️
            
      ╔══════════════════════════════════╗
      ║  "Con el hilo de Ariadna y      ║
      ║   la espada de Atenas,          ║
      ║   he vencido al Minotauro       ║
      ║   y escapado del laberinto"     ║
      ╚══════════════════════════════════╝
      
           ⚡ HÉROE DE ATENAS ⚡
           
          🌟 LEYENDA INMORTAL 🌟
          
    La luz del sol brilla sobre el héroe
       que conquistó la oscuridad...
       
           ⚔️ === VICTORIA === ⚔️
           
""" + Color.RESET


# ==================== FUNCIONES AUXILIARES ====================
def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('clear' if os.name != 'nt' else 'cls')


def escribir_lento(texto, delay=0.03):
    """Escribe texto con efecto de máquina de escribir"""
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def pausar(mensaje="Presiona ENTER para continuar..."):
    """Pausa la ejecución esperando input del usuario"""
    input(f"\n{Color.BRIGHT_BLACK}{mensaje}{Color.RESET}")


def mostrar_ayuda():
    """Muestra el menú de ayuda con instrucciones del juego"""
    limpiar_pantalla()
    print(f"\n{Color.BRIGHT_CYAN}╔{'═'*70}╗{Color.RESET}")
    print(f"{Color.BRIGHT_CYAN}║{Color.RESET}{Color.BRIGHT_WHITE}                        AYUDA DEL JUEGO                            {Color.RESET}{Color.BRIGHT_CYAN}║{Color.RESET}")
    print(f"{Color.BRIGHT_CYAN}╚{'═'*70}╝{Color.RESET}\n")
    
    print(f"{Color.BRIGHT_YELLOW}📖 OBJETIVO:{Color.RESET}")
    print(f"   Encuentra los 5 personajes aliados dispersos en el laberinto.")
    print(f"   Cada uno te ofrecerá 3 objetos, pero solo puedes elegir 1.")
    print(f"   La combinación de objetos determinará tu final.\n")
    
    print(f"{Color.BRIGHT_YELLOW}🎮 CONTROLES:{Color.RESET}")
    print(f"   {Color.BRIGHT_WHITE}N{Color.RESET} = Mover al Norte (arriba)")
    print(f"   {Color.BRIGHT_WHITE}S{Color.RESET} = Mover al Sur (abajo)")
    print(f"   {Color.BRIGHT_WHITE}E{Color.RESET} = Mover al Este (derecha)")
    print(f"   {Color.BRIGHT_WHITE}O{Color.RESET} = Mover al Oeste (izquierda)")
    print(f"   {Color.BRIGHT_WHITE}HELP{Color.RESET} = Mostrar esta ayuda\n")
    
    print(f"{Color.BRIGHT_YELLOW}📊 ESTADÍSTICAS:{Color.RESET}")
    print(f"   {Color.BRIGHT_GREEN}[HP]{Color.RESET} Salud: Si llega a 0, pierdes")
    print(f"   {Color.BRIGHT_CYAN}[CD]{Color.RESET} Cordura: Si llega a 0, enloqueces y pierdes")
    print(f"   {Color.BRIGHT_MAGENTA}[--]{Color.RESET} Hilo de Ariadna: Cada movimiento consume 1 unidad")
    print(f"   {Color.BRIGHT_YELLOW}[**]{Color.RESET} Puntos: Acumula puntos durante la aventura\n")
    
    print(f"{Color.BRIGHT_YELLOW}🗺️  MAPA:{Color.RESET}")
    print(f"   {Color.BRIGHT_GREEN}◉{Color.RESET} = Tu posición (Teseo)")
    print(f"   {Color.BRIGHT_YELLOW}★{Color.RESET} = Aliado visible")
    print(f"   {Color.BRIGHT_RED}⚠{Color.RESET} = Minotauro (¡PELIGRO!)")
    print(f"   {Color.WHITE}░{Color.RESET} = Área visible sin explorar")
    print(f"   {Color.BRIGHT_BLACK}·{Color.RESET} = Área ya explorada")
    print(f"   {Color.DIM}█{Color.RESET} = Área desconocida (fuera de tu visión)\n")
    
    print(f"{Color.BRIGHT_YELLOW}⚠️  CONDICIONES DE DERROTA:{Color.RESET}")
    print(f"   • Salud llega a 0 o menos")
    print(f"   • Cordura llega a 0")
    print(f"   • Hilo de Ariadna se agota completamente\n")
    
    print(f"{Color.BRIGHT_YELLOW}🏆 VICTORIA:{Color.RESET}")
    print(f"   Recolecta 5 objetos (uno de cada personaje) y logra una")
    print(f"   combinación válida para derrotar al Minotauro.\n")
    
    pausar()


# ==================== CLASE PRINCIPAL ====================
class LaberintoAsterionASCII:
    """Clase principal del juego con ASCII art y colores"""
    
    def __init__(self, config_path=None, seed=None):
        """Inicializa el juego cargando la configuración desde JSON
        
        Args:
            config_path (str, optional): Ruta al archivo context.json. Si es None, busca automáticamente.
            seed (int, optional): Semilla para random.seed() para reproducibilidad en demos.
        """
        # Configurar semilla para reproducibilidad (útil para demos y testing)
        if seed is not None:
            random.seed(seed)
            print(f"{Color.BRIGHT_CYAN}[i] Modo reproducible activado con semilla: {seed}{Color.RESET}")
            time.sleep(1)
        if config_path is None:
            # Intentar múltiples ubicaciones
            possible_paths = [
                "context.json",           # Mismo directorio que el script
                "../context.json",        # Directorio padre
                "./context.json",         # Directorio actual
            ]
            config_path = None
            for path in possible_paths:
                if Path(path).exists():
                    config_path = path
                    break
            
            if config_path is None:
                print(f"{Color.RED}[ERR] No se encontró context.json en ninguna ubicación esperada{Color.RESET}")
                print(f"{Color.YELLOW}[i] Ubicaciones buscadas:{Color.RESET}")
                for path in possible_paths:
                    print(f"    - {path}")
                exit(1)
        
        self.config = self.cargar_configuracion(config_path)
        self.tablero = None
        self.posicion = None
        self.jugador = None
        self.personajes_en_tablero = {}
        self.mapa_visitado = set()
        # Minotauro
        self.minotauro_pos = None
        self.minotauro_ultimo_movimiento = 0
        self.minotauro_detectado = False
        # Estado de combate para modo headless
        self._combat = None
        self.inicializar_juego()

    # ----------------- Métodos headless / API-friendly -----------------
    def get_state(self):
        """Retorna un dict serializable con el estado mínimo del juego"""
        return {
            'posicion': tuple(self.posicion),
            'jugador': {
                'nombre': self.jugador['nombre'],
                'salud': self.jugador['salud'],
                'cordura': self.jugador['cordura'],
                'puntos': self.jugador['puntos'],
                'hilo_ariadna': self.jugador['hilo_ariadna'],
                'inventario': list(self.jugador['inventario']),
            },
            'minotauro_pos': tuple(self.minotauro_pos) if self.minotauro_pos else None,
            'personajes_en_tablero': list(self.personajes_en_tablero.keys()),
            'mapa_visitado': [tuple(p) for p in self.mapa_visitado],
            'combat': self._combat.copy() if self._combat else None
        }

    def mover_jugador_headless(self, mov):
        """Mueve al jugador usando la lógica de `mover_jugador` pero sin input/prints.

        Args:
            mov (str): 'N','S','E','O' o 'HELP'
        Returns:
            dict: nuevo estado y flags (moved, encounter_personaje, encounter_minotauro)
        """
        mov = (mov or '').upper().strip()
        if mov == 'HELP' or mov == 'H':
            return {'moved': False, 'help': True}

        x, y = self.posicion
        n = 10
        movimiento_valido = False

        if mov == 'N' and x > 0:
            self.posicion[0] -= 1
            movimiento_valido = True
        elif mov == 'S' and x < n - 1:
            self.posicion[0] += 1
            movimiento_valido = True
        elif mov == 'E' and y < n - 1:
            self.posicion[1] += 1
            movimiento_valido = True
        elif mov == 'O' and y > 0:
            self.posicion[1] -= 1
            movimiento_valido = True
        else:
            return {'moved': False, 'error': 'Movimiento inválido'}

        if movimiento_valido:
            self.jugador['hilo_ariadna'] -= 1
            self.mapa_visitado.add(tuple(self.posicion))
            # Mover minotauro después
            self.mover_minotauro()

            personaje_id = self.tablero[self.posicion[0]][self.posicion[1]]
            mino_here = self.minotauro_pos == self.posicion if self.minotauro_pos else False
            return {'moved': True, 'personaje': personaje_id, 'minotauro': mino_here, 'state': self.get_state()}

    def encontrar_personaje_headless(self, personaje_id, choice_index):
        """Versión headless de `encontrar_personaje` que acepta la elección del objeto.

        Args:
            personaje_id: id del personaje en el tablero
            choice_index: 1-based index del objeto elegido
        Returns:
            dict: resultado y estado actualizado
        """
        if personaje_id not in self.personajes_en_tablero:
            return {'error': 'personaje no encontrado'}

        personaje = self.personajes_en_tablero[personaje_id]
        objetos = personaje['objetos_disponibles']

        if not (1 <= choice_index <= len(objetos)):
            return {'error': 'índice de objeto inválido'}

        objeto_elegido = objetos[choice_index - 1]
        self.jugador['inventario'].append(objeto_elegido['nombre'])

        # Remover personaje del tablero
        x, y = self.posicion
        self.tablero[x][y] = None
        # Eliminar de la lista de personajes para evitar reconexiones
        del self.personajes_en_tablero[personaje_id]

        # Aplicar subefecto (usa la misma función)
        self.aplicar_subefecto()

        return {'picked': objeto_elegido['nombre'], 'state': self.get_state()}

    def start_minotauro_combat(self):
        """Inicia un estado de combate headless con el Minotauro"""
        if self._combat is None:
            self._combat = {'minotauro_hp': 150, 'turno': 1, 'defendiendo': False}
        return {'combat': self._combat.copy()}

    def combat_action(self, action, item_index=None):
        """Procesa una acción durante el combate en modo headless.

        Actions: 'attack','defend','flee','use_item'
        """
        if self._combat is None:
            return {'error': 'no combat active'}

        minotauro_hp = self._combat['minotauro_hp']
        defendiendo = self._combat.get('defendiendo', False)

        # Acción del jugador
        if action == 'attack':
            dano_jugador = random.randint(20, 35)
            if random.random() < 0.1:
                dano_jugador = int(dano_jugador * 1.5)
            minotauro_hp -= dano_jugador
            result_player = {'action': 'attack', 'dano': dano_jugador}
            if minotauro_hp <= 0:
                # victoria
                self._combat = None
                self.victoria_contra_minotauro()
                return {'result': 'victory', 'state': self.get_state()}

        elif action == 'defend':
            defendiendo = True
            result_player = {'action': 'defend'}
        elif action == 'flee':
            probabilidad_huida = min(90, max(10, self.jugador['cordura']))
            if random.randint(1, 100) <= probabilidad_huida:
                # Escape exitoso: alejar minotauro
                direcciones = [(-3, 0), (3, 0), (0, -3), (0, 3), (-2, -2), (2, 2)]
                for dx, dy in direcciones:
                    new_x = self.minotauro_pos[0] + dx
                    new_y = self.minotauro_pos[1] + dy
                    if 0 <= new_x < 10 and 0 <= new_y < 10:
                        self.minotauro_pos = [new_x, new_y]
                        break
                self.jugador['cordura'] -= 10
                self._combat = None
                return {'result': 'fled', 'state': self.get_state()}
            else:
                result_player = {'action': 'flee', 'result': 'failed'}

        elif action == 'use_item':
            if not self.jugador['inventario']:
                return {'error': 'no items'}
            if item_index is None or item_index < 1 or item_index > len(self.jugador['inventario']):
                return {'error': 'invalid item index'}
            item = self.jugador['inventario'].pop(item_index - 1)
            if 'Poción' in item or 'Antorcha' in item:
                curacion = random.randint(15, 30)
                self.jugador['salud'] = min(100, self.jugador['salud'] + curacion)
                result_player = {'action': 'use_item', 'item': item, 'healed': curacion}
            else:
                dano_item = random.randint(30, 50)
                minotauro_hp -= dano_item
                result_player = {'action': 'use_item', 'item': item, 'dano': dano_item}
                if minotauro_hp <= 0:
                    self._combat = None
                    self.victoria_contra_minotauro()
                    return {'result': 'victory', 'state': self.get_state()}
        else:
            return {'error': 'acción inválida'}

        # Turno del minotauro
        dano_minotauro = random.randint(20, 35)
        if defendiendo:
            dano_minotauro = dano_minotauro // 2
        self.jugador['salud'] -= dano_minotauro
        self.jugador['cordura'] -= random.randint(5, 10)

        # Actualizar estado de combate
        if self._combat is not None:
            self._combat['minotauro_hp'] = minotauro_hp
            self._combat['turno'] = self._combat.get('turno', 1) + 1
            self._combat['defendiendo'] = False

        # Verificar derrota del jugador
        if self.jugador['salud'] <= 0:
            self.derrota_por_minotauro()
            return {'result': 'defeat', 'state': self.get_state()}

        return {'result_player': result_player, 'dano_minotauro': dano_minotauro, 'state': self.get_state()}
    
    def cargar_configuracion(self, config_path):
        """Carga el archivo de configuración JSON"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"{Color.RED}[ERR] No se encontró el archivo {config_path}{Color.RESET}")
            exit(1)
        except json.JSONDecodeError:
            print(f"{Color.RED}[ERR] El archivo {config_path} no es un JSON válido{Color.RESET}")
            exit(1)
    
    def inicializar_juego(self):
        """Inicializa el tablero, jugador y personajes
        
        FUNCIÓN: crea_tablero() + inicializa_jugador() + colocar_personajes()
        Cumple con requisito de separar lógica en funciones.
        """
        # Crear tablero 10x10 (matriz de listas)
        n = 10
        self.tablero = [[None for _ in range(n)] for _ in range(n)]
        # Posición inicial: centro del laberinto (5, 5)
        self.posicion = [n // 2, n // 2]
        
        stats = self.config['jugador']['stats_base']
        self.jugador = {
            'nombre': self.config['jugador']['nombre'],
            'salud': stats['salud'],
            'cordura': stats['cordura'],
            'sigilo': stats['sigilo'],
            'velocidad': stats['velocidad'],
            'puntos': stats['puntos'],
            'inventario': [],
            'hilo_ariadna': self.config['jugador']['inventario_inicial'][0]['cantidad_inicial']
        }
        
        self.colocar_personajes()
        self.colocar_minotauro()
        self.mapa_visitado.add(tuple(self.posicion))
    
    def colocar_personajes(self):
        """Coloca los 5 personajes aliados en posiciones aleatorias del tablero
        
        FUNCIÓN SEPARADA: colocar_personajes()
        Cumple con requisito de separar lógica en funciones.
        Usa ciclos (while) y condicionales (if) para validar posiciones.
        """
        personajes = self.config['personajes_aliados']['lista']
        
        # Generar posiciones excluyendo la posición inicial del jugador (5, 5)
        posicion_inicial = (5, 5)
        coords = []
        
        while len(coords) < len(personajes):
            pos = (random.randrange(10), random.randrange(10))
            # Asegurar que no sea la posición inicial y no esté repetida
            if pos != posicion_inicial and pos not in coords:
                coords.append(pos)
        
        for personaje, coord in zip(personajes, coords):
            x, y = coord
            self.tablero[x][y] = personaje['id']
            self.personajes_en_tablero[personaje['id']] = personaje
    
    def colocar_minotauro(self):
        """Coloca al Minotauro en una posición aleatoria lejos del jugador"""
        # Colocar al Minotauro lejos del jugador (mínimo 5 casillas)
        while True:
            x = random.randrange(10)
            y = random.randrange(10)
            distancia = abs(x - self.posicion[0]) + abs(y - self.posicion[1])
            
            # Verificar que no esté en posición del jugador, personajes, y esté lejos
            if (x, y) != tuple(self.posicion) and self.tablero[x][y] is None and distancia >= 5:
                self.minotauro_pos = [x, y]
                break
    
    def mover_minotauro(self):
        """Mueve al Minotauro según su IA (patrulla o persigue al jugador)"""
        if self.minotauro_pos is None:
            return
        
        # Calcular distancia al jugador
        distancia = abs(self.minotauro_pos[0] - self.posicion[0]) + abs(self.minotauro_pos[1] - self.posicion[1])
        
        # Radio de detección del Minotauro
        radio_deteccion = 4
        
        if distancia <= radio_deteccion:
            # PERSEGUIR al jugador
            self.minotauro_detectado = True
            dx = self.posicion[0] - self.minotauro_pos[0]
            dy = self.posicion[1] - self.minotauro_pos[1]
            
            # Moverse hacia el jugador (pathfinding simple)
            if abs(dx) > abs(dy):
                if dx > 0 and self.minotauro_pos[0] < 9:
                    self.minotauro_pos[0] += 1
                elif dx < 0 and self.minotauro_pos[0] > 0:
                    self.minotauro_pos[0] -= 1
            else:
                if dy > 0 and self.minotauro_pos[1] < 9:
                    self.minotauro_pos[1] += 1
                elif dy < 0 and self.minotauro_pos[1] > 0:
                    self.minotauro_pos[1] -= 1
        else:
            # PATRULLAR aleatoriamente
            self.minotauro_detectado = False
            movimientos = []
            if self.minotauro_pos[0] > 0:
                movimientos.append((-1, 0))
            if self.minotauro_pos[0] < 9:
                movimientos.append((1, 0))
            if self.minotauro_pos[1] > 0:
                movimientos.append((0, -1))
            if self.minotauro_pos[1] < 9:
                movimientos.append((0, 1))
            
            if movimientos:
                dx, dy = random.choice(movimientos)
                self.minotauro_pos[0] += dx
                self.minotauro_pos[1] += dy
        
        # Verificar si el Minotauro alcanzó al jugador
        if self.minotauro_pos == self.posicion:
            self.encuentro_con_minotauro()
    
    def encuentro_con_minotauro(self):
        """Maneja el encuentro directo con el Minotauro - Sistema de combate por turnos
        
        SISTEMA DE COMBATE INTERACTIVO:
        - Combate por turnos con múltiples opciones estratégicas
        - El jugador puede ATACAR, DEFENDER, HUIR o usar ITEMS
        - El Minotauro tiene 150 HP y ataca cada turno
        - Sistema de bloqueo reduce daño recibido
        - Huida tiene probabilidad basada en cordura
        """
        limpiar_pantalla()
        print(MINOTAURO_ASCII)
        print(f"\n{Color.BRIGHT_RED}{'═'*70}{Color.RESET}")
        print(f"{Color.BRIGHT_RED}  [!!!] ¡EL MINOTAURO TE HA ENCONTRADO!{Color.RESET}")
        print(f"{Color.BRIGHT_RED}{'═'*70}{Color.RESET}\n")
        
        escribir_lento(f"{Color.RED}Asterión emerge de las sombras con un rugido ensordecedor...{Color.RESET}", 0.03)
        escribir_lento(f"{Color.YELLOW}¡Debes luchar por tu vida!{Color.RESET}\n", 0.03)
        time.sleep(1)
        
        # Estadísticas del Minotauro
        minotauro_hp = 150
        minotauro_max_hp = 150
        turno = 1
        defendiendo = False
        
        # Combate por turnos
        while True:
            limpiar_pantalla()
            
            # Mostrar estado del combate
            print(f"{Color.BRIGHT_RED}{'═'*70}{Color.RESET}")
            print(f"{Color.BRIGHT_WHITE}                    COMBATE - TURNO {turno}{Color.RESET}")
            print(f"{Color.BRIGHT_RED}{'═'*70}{Color.RESET}\n")
            
            # Estado del Minotauro
            minotauro_hp_pct = minotauro_hp / minotauro_max_hp
            if minotauro_hp_pct > 0.6:
                color_mino = Color.BRIGHT_RED
            elif minotauro_hp_pct > 0.3:
                color_mino = Color.YELLOW
            else:
                color_mino = Color.RED
            
            barra_mino = int(minotauro_hp_pct * 20)
            print(f"{Color.BRIGHT_RED}⚠ MINOTAURO{Color.RESET}")
            print(f"  HP: {color_mino}[{'█' * barra_mino}{' ' * (20 - barra_mino)}]{Color.RESET} {minotauro_hp}/{minotauro_max_hp}")
            
            print(f"\n{Color.BRIGHT_CYAN}{'─'*70}{Color.RESET}\n")
            
            # Estado de Teseo
            salud_pct = self.jugador['salud'] / 100
            if salud_pct > 0.6:
                color_salud = Color.BRIGHT_GREEN
            elif salud_pct > 0.3:
                color_salud = Color.YELLOW
            else:
                color_salud = Color.BRIGHT_RED
            
            cordura_pct = self.jugador['cordura'] / 100
            if cordura_pct > 0.6:
                color_cordura = Color.BRIGHT_CYAN
            elif cordura_pct > 0.3:
                color_cordura = Color.YELLOW
            else:
                color_cordura = Color.BRIGHT_RED
            
            barra_salud = int(salud_pct * 20)
            barra_cordura = int(cordura_pct * 20)
            
            print(f"{Color.BRIGHT_GREEN}◉ TESEO{Color.RESET}")
            print(f"  HP:      {color_salud}[{'█' * barra_salud}{' ' * (20 - barra_salud)}]{Color.RESET} {self.jugador['salud']}/100")
            print(f"  Cordura: {color_cordura}[{'█' * barra_cordura}{' ' * (20 - barra_cordura)}]{Color.RESET} {self.jugador['cordura']}/100")
            
            if defendiendo:
                print(f"\n{Color.BRIGHT_BLUE}[🛡] Estás en posición defensiva (daño reducido en 50%){Color.RESET}")
            
            # Opciones de combate
            print(f"\n{Color.BRIGHT_YELLOW}{'─'*70}{Color.RESET}")
            print(f"{Color.BRIGHT_WHITE}¿Qué harás?{Color.RESET}")
            print(f"  {Color.BRIGHT_RED}[1] ATACAR{Color.RESET}   - Ataque directo al Minotauro (20-35 de daño)")
            print(f"  {Color.BRIGHT_BLUE}[2] DEFENDER{Color.RESET} - Posición defensiva (reduce daño recibido 50%)")
            print(f"  {Color.BRIGHT_YELLOW}[3] HUIR{Color.RESET}     - Intentar escapar (probabilidad basada en cordura)")
            print(f"  {Color.BRIGHT_MAGENTA}[4] ITEM{Color.RESET}     - Usar un objeto del inventario")
            print(f"{Color.BRIGHT_YELLOW}{'─'*70}{Color.RESET}")
            
            accion = input(f"\n{Color.BRIGHT_WHITE}Elige tu acción [1-4]: {Color.RESET}").strip()
            
            print()
            
            # ========== ACCIÓN DEL JUGADOR ==========
            if accion == '1':  # ATACAR
                defendiendo = False
                dano_jugador = random.randint(20, 35)
                
                # Crítico (10% de probabilidad)
                if random.random() < 0.1:
                    dano_jugador = int(dano_jugador * 1.5)
                    print(f"{Color.BRIGHT_YELLOW}[***] ¡GOLPE CRÍTICO!{Color.RESET}")
                    time.sleep(0.5)
                
                minotauro_hp -= dano_jugador
                
                escribir_lento(f"{Color.BRIGHT_GREEN}[⚔] Atacas al Minotauro con tu espada...{Color.RESET}", 0.03)
                time.sleep(0.5)
                print(f"{Color.BRIGHT_RED}[!] Infliges {dano_jugador} puntos de daño{Color.RESET}")
                time.sleep(1)
                
                # Verificar si el Minotauro fue derrotado
                if minotauro_hp <= 0:
                    self.victoria_contra_minotauro()
                    return
            
            elif accion == '2':  # DEFENDER
                defendiendo = True
                escribir_lento(f"{Color.BRIGHT_BLUE}[🛡] Adoptas una posición defensiva...{Color.RESET}", 0.03)
                print(f"{Color.CYAN}[i] El siguiente ataque del Minotauro hará menos daño{Color.RESET}")
                time.sleep(1)
            
            elif accion == '3':  # HUIR
                defendiendo = False
                probabilidad_huida = min(90, max(10, self.jugador['cordura']))
                
                escribir_lento(f"{Color.YELLOW}[↻] Intentas escapar del Minotauro...{Color.RESET}", 0.03)
                time.sleep(1)
                
                if random.randint(1, 100) <= probabilidad_huida:
                    print(f"{Color.BRIGHT_GREEN}[✓] ¡Logras escapar!{Color.RESET}")
                    time.sleep(1)
                    
                    # Mover al Minotauro lejos
                    direcciones = [(-3, 0), (3, 0), (0, -3), (0, 3), (-2, -2), (2, 2)]
                    for dx, dy in direcciones:
                        new_x = self.minotauro_pos[0] + dx
                        new_y = self.minotauro_pos[1] + dy
                        if 0 <= new_x < 10 and 0 <= new_y < 10:
                            self.minotauro_pos = [new_x, new_y]
                            break
                    
                    # Penalización por huir
                    self.jugador['cordura'] -= 10
                    print(f"{Color.MAGENTA}[-10] Pierdes cordura por huir (-10){Color.RESET}")
                    time.sleep(1)
                    return
                else:
                    print(f"{Color.BRIGHT_RED}[✗] ¡No puedes escapar!{Color.RESET}")
                    print(f"{Color.RED}[!] El Minotauro bloquea tu salida{Color.RESET}")
                    time.sleep(1)
            
            elif accion == '4':  # USAR ITEM
                if not self.jugador['inventario']:
                    print(f"{Color.RED}[!] No tienes objetos en tu inventario{Color.RESET}")
                    time.sleep(1.5)
                    continue
                
                print(f"{Color.BRIGHT_MAGENTA}Inventario:{Color.RESET}")
                for idx, item in enumerate(self.jugador['inventario'], 1):
                    print(f"  [{idx}] {item}")
                
                try:
                    item_idx = int(input(f"\n{Color.BRIGHT_WHITE}Elige objeto [1-{len(self.jugador['inventario'])}] o 0 para cancelar: {Color.RESET}").strip())
                    
                    if item_idx == 0:
                        continue
                    
                    if 1 <= item_idx <= len(self.jugador['inventario']):
                        item = self.jugador['inventario'][item_idx - 1]
                        
                        # Efectos de items (ejemplo)
                        if 'Poción' in item or 'Antorcha' in item:
                            curacion = random.randint(15, 30)
                            self.jugador['salud'] = min(100, self.jugador['salud'] + curacion)
                            print(f"{Color.BRIGHT_GREEN}[+] Usas {item} y recuperas {curacion} HP{Color.RESET}")
                        elif 'Espada' in item or 'Corona' in item:
                            dano_item = random.randint(30, 50)
                            minotauro_hp -= dano_item
                            print(f"{Color.BRIGHT_YELLOW}[⚔] Usas {item} y causas {dano_item} de daño{Color.RESET}")
                            
                            if minotauro_hp <= 0:
                                time.sleep(1)
                                self.victoria_contra_minotauro()
                                return
                        else:
                            curacion = 20
                            self.jugador['salud'] = min(100, self.jugador['salud'] + curacion)
                            print(f"{Color.BRIGHT_GREEN}[+] Usas {item} y recuperas {curacion} HP{Color.RESET}")
                        
                        self.jugador['inventario'].pop(item_idx - 1)
                        defendiendo = False
                        time.sleep(1)
                    else:
                        print(f"{Color.RED}[!] Opción inválida{Color.RESET}")
                        time.sleep(1)
                        continue
                except ValueError:
                    print(f"{Color.RED}[!] Entrada inválida{Color.RESET}")
                    time.sleep(1)
                    continue
            
            else:
                print(f"{Color.RED}[!] Acción inválida. Pierdes tu turno.{Color.RESET}")
                time.sleep(1.5)
            
            # ========== TURNO DEL MINOTAURO ==========
            print(f"\n{Color.BRIGHT_RED}{'─'*70}{Color.RESET}")
            escribir_lento(f"{Color.RED}¡El Minotauro contraataca!{Color.RESET}", 0.03)
            time.sleep(0.5)
            
            dano_minotauro = random.randint(20, 35)
            
            # Reducir daño si está defendiendo
            if defendiendo:
                dano_minotauro = dano_minotauro // 2
                print(f"{Color.BRIGHT_BLUE}[🛡] Tu defensa reduce el daño a la mitad{Color.RESET}")
            
            self.jugador['salud'] -= dano_minotauro
            self.jugador['cordura'] -= random.randint(5, 10)
            
            print(f"{Color.BRIGHT_RED}[!!] El Minotauro te golpea por {dano_minotauro} puntos de daño{Color.RESET}")
            time.sleep(1.5)
            
            # Verificar si Teseo murió
            if self.jugador['salud'] <= 0:
                self.derrota_por_minotauro()
                return
            
            turno += 1
            defendiendo = False  # Reset defensa después del turno del Minotauro
    
    def victoria_contra_minotauro(self):
        """Final especial: Teseo derrota al Minotauro"""
        limpiar_pantalla()
        print(f"{Color.BRIGHT_GREEN}{'═'*70}{Color.RESET}")
        print(f"{Color.BRIGHT_GREEN}              ¡¡¡VICTORIA!!!{Color.RESET}")
        print(f"{Color.BRIGHT_GREEN}{'═'*70}{Color.RESET}\n")
        
        escribir_lento(f"{Color.BRIGHT_YELLOW}El Minotauro cae de rodillas con un último rugido...{Color.RESET}", 0.04)
        escribir_lento(f"{Color.BRIGHT_GREEN}¡Has vencido a Asterión, la bestia del laberinto!{Color.RESET}\n", 0.04)
        
        print(TESEO_VICTORIOSO_ASCII)
        
        print(f"\n{Color.BRIGHT_YELLOW}[***] FINAL ÉPICO DESBLOQUEADO{Color.RESET}")
        print(f"{Color.BRIGHT_GREEN}[+500] Puntos de victoria{Color.RESET}")
        
        self.jugador['puntos'] += 500
        self.jugador['salud'] = 100  # Recuperación completa
        
        escribir_lento(f"\n{Color.BRIGHT_CYAN}Has liberado a Atenas del terror del Minotauro.{Color.RESET}", 0.04)
        escribir_lento(f"{Color.BRIGHT_CYAN}Tu nombre será recordado por siempre como el héroe que venció al laberinto.{Color.RESET}\n", 0.04)
        
        pausar("Presiona ENTER para continuar tu aventura...")
        
        # El Minotauro es eliminado del mapa
        self.minotauro_pos = None
    
    def derrota_por_minotauro(self):
        """Final de derrota: Teseo muere a manos del Minotauro"""
        limpiar_pantalla()
        print(TESEO_DERROTADO_ASCII)
        
        print(f"\n{Color.BRIGHT_RED}{'═'*70}{Color.RESET}")
        print(f"{Color.BRIGHT_RED}              GAME OVER{Color.RESET}")
        print(f"{Color.BRIGHT_RED}{'═'*70}{Color.RESET}\n")
        
        escribir_lento(f"{Color.RED}Teseo cae derrotado ante la furia del Minotauro...{Color.RESET}", 0.04)
        escribir_lento(f"{Color.BRIGHT_BLACK}El laberinto se cobra otra víctima.{Color.RESET}\n", 0.04)
        
        print(f"{Color.YELLOW}Puntuación final: {self.jugador['puntos']}{Color.RESET}")
        print(f"{Color.MAGENTA}Inventario: {', '.join(self.jugador['inventario']) if self.jugador['inventario'] else 'Vacío'}{Color.RESET}\n")
        
        pausar("Presiona ENTER para terminar...")
        
        # Fin del juego
        sys.exit(0)
    
    def generar_posiciones_aleatorias(self, n, k):
        """Genera k posiciones únicas aleatorias en el tablero nxn"""
        coords = set()
        while len(coords) < k:
            coords.add((random.randrange(n), random.randrange(n)))
        return list(coords)
    
    def mostrar_titulo(self):
        """Muestra el título del juego con ASCII art"""
        limpiar_pantalla()
        print(ASCII_TITLE)
        
        info = self.config['game_info']
        lore = self.config['lore_context']
        
        print(f"\n{Color.BRIGHT_WHITE}{'═'*70}{Color.RESET}")
        print(f"{Color.CYAN}[*] Ubicación:{Color.RESET} {lore['ubicacion']}")
        print(f"{Color.GREEN}[!] Protagonista:{Color.RESET} {lore['protagonista']}")
        print(f"{Color.RED}[X] Enemigo:{Color.RESET} {lore['villano_principal']}")
        print(f"\n{Color.YELLOW}[>] Objetivo:{Color.RESET} {self.config['reglas_juego']['objetivo_principal']}")
        print(f"{Color.BRIGHT_WHITE}{'═'*70}{Color.RESET}\n")
    
    def mostrar_mapa(self):
        """Muestra un mapa visual del laberinto con campo de visión"""
        print(f"\n{Color.BRIGHT_CYAN}╔{'═'*31}╗{Color.RESET}")
        print(f"{Color.BRIGHT_CYAN}║{Color.RESET}{Color.BRIGHT_WHITE}   MAPA DEL LABERINTO          {Color.RESET}{Color.BRIGHT_CYAN}║{Color.RESET}")
        print(f"{Color.BRIGHT_CYAN}╠{'═'*31}╣{Color.RESET}")
        
        # Radio de visión del jugador
        vision_radius = 2
        x_jugador, y_jugador = self.posicion
        
        for i in range(10):
            print(f"{Color.BRIGHT_CYAN}║{Color.RESET} ", end="")
            for j in range(10):
                # Calcular distancia al jugador
                distancia = max(abs(i - x_jugador), abs(j - y_jugador))
                
                # Posición del jugador
                if i == x_jugador and j == y_jugador:
                    print(f"{Color.BRIGHT_GREEN}◉{Color.RESET}  ", end="")
                
                # Posición del Minotauro (si está visible)
                elif self.minotauro_pos and i == self.minotauro_pos[0] and j == self.minotauro_pos[1] and distancia <= vision_radius:
                    print(f"{Color.BRIGHT_RED}⚠{Color.RESET}  ", end="")
                
                # Dentro del campo de visión
                elif distancia <= vision_radius:
                    if self.tablero[i][j]:  # Hay un personaje
                        print(f"{Color.BRIGHT_YELLOW}★{Color.RESET}  ", end="")
                    elif (i, j) in self.mapa_visitado:  # Ya visitado
                        print(f"{Color.BRIGHT_BLACK}·{Color.RESET}  ", end="")
                    else:  # Visible pero no visitado
                        print(f"{Color.WHITE}░{Color.RESET}  ", end="")
                
                # Fuera del campo de visión pero visitado anteriormente
                elif (i, j) in self.mapa_visitado:
                    if self.tablero[i][j]:  # Había un personaje (ya no visible)
                        print(f"{Color.DIM}?{Color.RESET}  ", end="")
                    else:
                        print(f"{Color.DIM}·{Color.RESET}  ", end="")
                
                # Completamente desconocido
                else:
                    print(f"{Color.DIM}█{Color.RESET}  ", end="")
            
            print(f"{Color.BRIGHT_CYAN}║{Color.RESET}")
        
        print(f"{Color.BRIGHT_CYAN}╚{'═'*31}╝{Color.RESET}")
        
        # Leyenda mejorada
        print(f"\n{Color.BRIGHT_WHITE}Leyenda:{Color.RESET}")
        print(f"  {Color.BRIGHT_GREEN}◉{Color.RESET} Teseo (tú)      ", end="")
        print(f"{Color.BRIGHT_YELLOW}★{Color.RESET} Aliado visible")
        print(f"  {Color.BRIGHT_RED}⚠{Color.RESET} Minotauro       ", end="")
        print(f"{Color.WHITE}░{Color.RESET} Área visible")
        print(f"  {Color.BRIGHT_BLACK}·{Color.RESET} Explorado        ", end="")
        print(f"{Color.DIM}█{Color.RESET} Desconocido")
        print(f"\n{Color.BRIGHT_CYAN}[i] Campo de visión: {vision_radius} celdas{Color.RESET}")
        
        # Advertencia si el Minotauro está cerca
        if self.minotauro_pos:
            dist_minotauro = abs(self.minotauro_pos[0] - x_jugador) + abs(self.minotauro_pos[1] - y_jugador)
            if dist_minotauro <= 4:
                print(f"{Color.BRIGHT_RED}[!!!] ¡ALERTA! El Minotauro está cerca...{Color.RESET}")
            elif dist_minotauro <= 6:
                print(f"{Color.YELLOW}[!] Sientes una presencia amenazante...{Color.RESET}")
    
    def mostrar_estado_jugador(self):
        """Muestra las estadísticas actuales del jugador con colores"""
        print(f"\n{Color.BRIGHT_WHITE}{'─'*70}{Color.RESET}")
        
        # Barra de salud
        salud_pct = self.jugador['salud'] / 100
        if salud_pct > 0.6:
            color_salud = Color.BRIGHT_GREEN
        elif salud_pct > 0.3:
            color_salud = Color.BRIGHT_YELLOW
        else:
            color_salud = Color.BRIGHT_RED
        
        # Barra de cordura
        cordura_pct = self.jugador['cordura'] / 100
        if cordura_pct > 0.6:
            color_cordura = Color.BRIGHT_CYAN
        elif cordura_pct > 0.3:
            color_cordura = Color.BRIGHT_YELLOW
        else:
            color_cordura = Color.BRIGHT_RED
        
        print(f"{Color.BRIGHT_CYAN}[@] {self.jugador['nombre']}{Color.RESET}")
        print(f"  {color_salud}[HP]{Color.RESET} Salud: {color_salud}{self.jugador['salud']}/100{Color.RESET} ", end="")
        print(f"| {color_cordura}[CD]{Color.RESET} Cordura: {color_cordura}{self.jugador['cordura']}/100{Color.RESET}")
        print(f"  {Color.BRIGHT_MAGENTA}[--]{Color.RESET} Hilo: {self.jugador['hilo_ariadna']} ", end="")
        print(f"| {Color.BRIGHT_YELLOW}[**]{Color.RESET} Puntos: {self.jugador['puntos']}")
        
        # Inventario
        inv_color = Color.BRIGHT_GREEN if len(self.jugador['inventario']) < 5 else Color.BRIGHT_CYAN
        print(f"  {inv_color}[##]{Color.RESET} Inventario ({len(self.jugador['inventario'])}/5): ", end="")
        if self.jugador['inventario']:
            print(f"{Color.WHITE}{', '.join(self.jugador['inventario'])}{Color.RESET}")
        else:
            print(f"{Color.BRIGHT_BLACK}Vacío{Color.RESET}")
        
        print(f"{Color.BRIGHT_WHITE}{'─'*70}{Color.RESET}\n")
    
    def verificar_condiciones_derrota(self):
        """Verifica si el jugador ha perdido"""
        if self.jugador['salud'] <= 0:
            limpiar_pantalla()
            print(TESEO_DERROTADO_ASCII)
            print(f"\n{Color.BRIGHT_RED}╔{'═'*50}╗{Color.RESET}")
            print(f"{Color.BRIGHT_RED}║{Color.RESET}  {Color.RED}[XX] Tu salud ha llegado a 0...{Color.RESET}              {Color.BRIGHT_RED}║{Color.RESET}")
            print(f"{Color.BRIGHT_RED}║{Color.RESET}  {Color.RED}Has muerto en el laberinto.{Color.RESET}                  {Color.BRIGHT_RED}║{Color.RESET}")
            print(f"{Color.BRIGHT_RED}║{Color.RESET}  {Color.RED}Asterión ha reclamado otra víctima.{Color.RESET}         {Color.BRIGHT_RED}║{Color.RESET}")
            print(f"{Color.BRIGHT_RED}╚{'═'*50}╝{Color.RESET}\n")
            return True
        
        if self.jugador['cordura'] <= 0:
            limpiar_pantalla()
            print(f"\n{Color.BRIGHT_MAGENTA}╔{'═'*50}╗{Color.RESET}")
            print(f"{Color.BRIGHT_MAGENTA}║{Color.RESET}  {Color.MAGENTA}[@@] Tu cordura se ha desvanecido...{Color.RESET}         {Color.BRIGHT_MAGENTA}║{Color.RESET}")
            print(f"{Color.BRIGHT_MAGENTA}║{Color.RESET}  {Color.MAGENTA}Te pierdes en la locura del laberinto.{Color.RESET}       {Color.BRIGHT_MAGENTA}║{Color.RESET}")
            print(f"{Color.BRIGHT_MAGENTA}╚{'═'*50}╝{Color.RESET}\n")
            return True
        
        if self.jugador['hilo_ariadna'] <= 0:
            limpiar_pantalla()
            print(f"\n{Color.BRIGHT_YELLOW}╔{'═'*50}╗{Color.RESET}")
            print(f"{Color.BRIGHT_YELLOW}║{Color.RESET}  {Color.YELLOW}[--] El Hilo de Ariadna se ha agotado...{Color.RESET}     {Color.BRIGHT_YELLOW}║{Color.RESET}")
            print(f"{Color.BRIGHT_YELLOW}║{Color.RESET}  {Color.YELLOW}Estás perdido para siempre.{Color.RESET}                  {Color.BRIGHT_YELLOW}║{Color.RESET}")
            print(f"{Color.BRIGHT_YELLOW}╚{'═'*50}╝{Color.RESET}\n")
            return True
        
        return False
    
    def encontrar_personaje(self, personaje_id):
        """Maneja el encuentro con un personaje aliado
        
        FUNCIÓN SEPARADA: interactuar_personaje()
        Cumple con requisito de separar lógica en funciones.
        Usa condicionales para validar entrada y ciclos para mostrar opciones.
        """
        personaje = self.personajes_en_tablero[personaje_id]
        
        limpiar_pantalla()
        print(f"\n{Color.BRIGHT_YELLOW}{'═'*70}{Color.RESET}")
        print(f"{Color.BRIGHT_GREEN}[+] ¡Has encontrado a {personaje['nombre']}!{Color.RESET}")
        print(f"{Color.BRIGHT_YELLOW}{'═'*70}{Color.RESET}\n")
        
        escribir_lento(f"{Color.CYAN}[i] {personaje['descripcion']}{Color.RESET}", 0.02)
        print()
        escribir_lento(f"{Color.BRIGHT_WHITE}[~] {personaje['nombre']}:{Color.RESET} \"{personaje['dialogo_encuentro']}\"", 0.02)
        
        # Mostrar opciones de objetos
        objetos = personaje['objetos_disponibles']
        print(f"\n{Color.BRIGHT_MAGENTA}[?] Objetos disponibles:{Color.RESET}\n")
        
        for idx, obj in enumerate(objetos, 1):
            print(f"{Color.BRIGHT_YELLOW}  {idx}) {obj['nombre']}{Color.RESET}")
            print(f"     {Color.BRIGHT_BLACK}Tipo:{Color.RESET} {obj['tipo']}")
            print(f"     {Color.WHITE}{obj['descripcion']}{Color.RESET}")
            
            # Mostrar estadísticas específicas del objeto
            if 'dano' in obj:
                print(f"     {Color.RED}[ATK]{Color.RESET} Daño: {obj['dano']}")
            if 'defensa' in obj:
                print(f"     {Color.BLUE}[DEF]{Color.RESET} Defensa: {obj['defensa']}")
            if 'habilidad' in obj:
                print(f"     {Color.CYAN}[SKL]{Color.RESET} Habilidad: {obj['habilidad']}")
            if 'poder' in obj:
                print(f"     {Color.MAGENTA}[PWR]{Color.RESET} Poder: {obj['poder']}")
            print()
        
        # Solicitar elección del jugador
        while True:
            try:
                eleccion = int(input(f"{Color.BRIGHT_WHITE}Elige un objeto (1-3): {Color.RESET}"))
                if 1 <= eleccion <= 3:
                    objeto_elegido = objetos[eleccion - 1]
                    break
                else:
                    print(f"{Color.RED}[!] Opción inválida. Elige 1, 2 o 3.{Color.RESET}")
            except ValueError:
                print(f"{Color.RED}[!] Por favor ingresa un número.{Color.RESET}")
        
        # Agregar objeto al inventario
        self.jugador['inventario'].append(objeto_elegido['nombre'])
        print(f"\n{Color.BRIGHT_GREEN}[OK] Has obtenido: {objeto_elegido['nombre']}{Color.RESET}")
        
        # Remover personaje del tablero
        x, y = self.posicion
        self.tablero[x][y] = None
        
        # Aplicar subefecto aleatorio
        self.aplicar_subefecto()
        
        # Pequeña pausa para leer el resultado
        time.sleep(1.5)
    
    def aplicar_subefecto(self):
        """Aplica un efecto aleatorio después de recoger un objeto"""
        efectos = self.config['sistema_subefectos']['efectos_posibles']
        efecto = random.choice(efectos)
        
        self.jugador[efecto['tipo']] += efecto['valor']
        
        time.sleep(0.5)
        print(f"\n{Color.BRIGHT_CYAN}[?] Subefecto:{Color.RESET} {efecto['descripcion']}")
        
        # Mostrar cambio con color
        signo = '+' if efecto['valor'] > 0 else ''
        if efecto['valor'] > 0:
            color = Color.BRIGHT_GREEN
        else:
            color = Color.BRIGHT_RED
        
        print(f"   {color}{efecto['tipo'].capitalize()}: {signo}{efecto['valor']}{Color.RESET}")
    
    def mover_jugador(self):
        """Solicita y procesa el movimiento del jugador
        
        FUNCIÓN SEPARADA: mover_jugador()
        Cumple con requisito de separar lógica en funciones.
        Usa condicionales complejos para validar movimientos y límites del tablero.
        """
        print(f"\n{Color.BRIGHT_CYAN}[^] Direcciones disponibles:{Color.RESET}")
        print(f"   {Color.BRIGHT_WHITE}N{Color.RESET} (Norte) | {Color.BRIGHT_WHITE}S{Color.RESET} (Sur) | {Color.BRIGHT_WHITE}E{Color.RESET} (Este) | {Color.BRIGHT_WHITE}O{Color.RESET} (Oeste) | {Color.BRIGHT_WHITE}HELP{Color.RESET} (Ayuda)")
        
        mov = input(f"\n{Color.BRIGHT_YELLOW}Elige dirección (o escribe HELP): {Color.RESET}").upper().strip()
        
        # Sistema de ayuda integrado
        if mov == 'HELP' or mov == 'H':
            mostrar_ayuda()
            return
        
        x, y = self.posicion
        n = 10
        movimiento_valido = False
        
        if mov == 'N' and x > 0:
            self.posicion[0] -= 1
            movimiento_valido = True
        elif mov == 'S' and x < n - 1:
            self.posicion[0] += 1
            movimiento_valido = True
        elif mov == 'E' and y < n - 1:
            self.posicion[1] += 1
            movimiento_valido = True
        elif mov == 'O' and y > 0:
            self.posicion[1] -= 1
            movimiento_valido = True
        else:
            print(f"{Color.RED}[!] Movimiento inválido. No puedes salir del laberinto.{Color.RESET}")
            time.sleep(1)
            return
        
        if movimiento_valido:
            # Consumir hilo de Ariadna
            self.jugador['hilo_ariadna'] -= 1
            self.mapa_visitado.add(tuple(self.posicion))
            
            print(f"{Color.BRIGHT_GREEN}[OK] Te has movido hacia el {mov}{Color.RESET}")
            print(f"   {Color.MAGENTA}[--]{Color.RESET} Hilo de Ariadna restante: {self.jugador['hilo_ariadna']}")
            
            # El Minotauro se mueve después del jugador
            self.mover_minotauro()
            
            time.sleep(0.5)
    
    def determinar_final(self):
        """Determina qué final obtiene el jugador según su inventario
        
        FUNCIÓN SEPARADA: evaluar_final()
        Cumple con requisito de separar lógica en funciones.
        Usa ciclos para iterar finales y condicionales para evaluar combinaciones.
        Sistema de finales por combinación según requisitos del proyecto.
        """
        inventario_set = set(self.jugador['inventario'])
        finales = self.config['finales_posibles']['finales']
        
        limpiar_pantalla()
        print(MINOTAURO_ASCII)
        
        print(f"\n{Color.BRIGHT_RED}{'═'*70}{Color.RESET}")
        print(f"{Color.BRIGHT_RED}  [!!!] ENFRENTAMIENTO FINAL CON ASTERIÓN{Color.RESET}")
        print(f"{Color.BRIGHT_RED}{'═'*70}{Color.RESET}\n")
        
        escribir_lento(f"{Color.WHITE}Con tu inventario completo, te adentras al centro del laberinto...{Color.RESET}", 0.03)
        print(f"{Color.BRIGHT_CYAN}Objetos recolectados:{Color.RESET} {Color.YELLOW}{', '.join(self.jugador['inventario'])}{Color.RESET}\n")
        
        pausar("Presiona ENTER para enfrentar al Minotauro...")
        
        # Buscar final válido
        final_encontrado = None
        for final in finales:
            combo_requerida = set(final['combinacion_requerida'])
            if inventario_set == combo_requerida:
                final_encontrado = final
                break
        
        limpiar_pantalla()
        print(f"\n{Color.BRIGHT_WHITE}{'═'*70}{Color.RESET}")
        
        if final_encontrado:
            print(f"{Color.BRIGHT_GREEN}  [***] {final_encontrado['nombre']}{Color.RESET}")
            print(f"{Color.BRIGHT_WHITE}{'═'*70}{Color.RESET}\n")
            escribir_lento(f"{Color.CYAN}{final_encontrado['descripcion']}{Color.RESET}\n", 0.02)
            escribir_lento(f"{Color.WHITE}[>] {final_encontrado['narrativa']}{Color.RESET}", 0.02)
            print(TESEO_VICTORIOSO_ASCII)
            print(f"\n{Color.BRIGHT_GREEN}{'─'*70}{Color.RESET}")
            print(f"{Color.BRIGHT_GREEN}[WIN] ¡VICTORIA! Has derrotado a Asterión y escapado del laberinto.{Color.RESET}")
            print(f"{Color.BRIGHT_GREEN}{'─'*70}{Color.RESET}")
        else:
            # Final de derrota
            print(TESEO_VENCIDO_ASCII)
            final_derrota = self.config['finales_posibles']['final_derrota']
            print(f"\n{Color.BRIGHT_RED}  [XXX] {final_derrota['nombre']}{Color.RESET}")
            print(f"{Color.BRIGHT_WHITE}{'═'*70}{Color.RESET}\n")
            escribir_lento(f"{Color.RED}{final_derrota['descripcion']}{Color.RESET}\n", 0.02)
            escribir_lento(f"{Color.BRIGHT_BLACK}[>] {final_derrota['narrativa']}{Color.RESET}", 0.02)
            print(f"\n{Color.BRIGHT_RED}{'─'*70}{Color.RESET}")
            print(f"{Color.BRIGHT_RED}[XXX] DERROTA. El laberinto reclama otra víctima...{Color.RESET}")
            print(f"{Color.BRIGHT_RED}{'─'*70}{Color.RESET}")
        
        print(f"\n{Color.BRIGHT_YELLOW}{'═'*70}{Color.RESET}")
        print(f"{Color.BRIGHT_YELLOW}  Puntuación Final: {self.jugador['puntos']} puntos{Color.RESET}")
        print(f"{Color.BRIGHT_YELLOW}{'═'*70}{Color.RESET}\n")
    
    def jugar(self):
        """Bucle principal del juego
        
        ALGORITMO PRINCIPAL:
        1. Inicio: Mostrar título y narrativa inicial
        2. Ciclo: Mientras inventario < 5 y jugador vivo
           a. Mostrar estado del jugador (salud, cordura, hilo, puntos, inventario)
           b. Mostrar mapa del laberinto con campo de visión
           c. Verificar si hay personaje en celda actual
           d. Si hay personaje: interactuar y elegir objeto
           e. Solicitar movimiento del jugador (N/S/E/O/HELP)
           f. Actualizar posición y consumir hilo
           g. Verificar condiciones de derrota
        3. Fin: Evaluar inventario y mostrar final correspondiente
        """
        self.mostrar_titulo()
        
        escribir_lento(f"{Color.WHITE}Comienzas tu aventura en el centro del laberinto...{Color.RESET}", 0.03)
        escribir_lento(f"{Color.WHITE}Debes encontrar a los 5 aliados dispersos y recolectar sus objetos.{Color.RESET}\n", 0.03)
        
        pausar()
        
        # Bucle principal: hasta recolectar 5 objetos o morir
        while len(self.jugador['inventario']) < 5:
            # Verificar condiciones de derrota
            if self.verificar_condiciones_derrota():
                print(f"\n{Color.BRIGHT_RED}[XXX] GAME OVER{Color.RESET}\n")
                pausar()
                return
            
            limpiar_pantalla()
            
            # Mostrar estado
            self.mostrar_estado_jugador()
            
            # Mostrar mapa
            self.mostrar_mapa()
            
            x, y = self.posicion
            print(f"\n{Color.BRIGHT_CYAN}[*] Posición actual:{Color.RESET} Sala ({x}, {y})")
            
            # Verificar si hay personaje en esta celda
            personaje_id = self.tablero[x][y]
            if personaje_id:
                time.sleep(0.5)
                self.encontrar_personaje(personaje_id)
            else:
                print(f"   {Color.BRIGHT_BLACK}Esta sala está vacía. Continúa explorando...{Color.RESET}")
            
            # Mover jugador
            self.mover_jugador()
        
        # Final del juego
        self.determinar_final()


def main():
    """Función principal
    
    Permite ejecutar el juego con parámetros opcionales:
    - seed: Para reproducibilidad en demos (ejemplo: seed=42)
    - config_path: Para usar un archivo de configuración personalizado
    
    Requisito del proyecto: Este código debe ser personalizable para que
    los estudiantes puedan modificar la historia, personajes y mecánicas.
    """
    # Descomentar la siguiente línea para modo reproducible (útil para demos)
    # juego = LaberintoAsterionASCII(seed=42)
    
    try:
        juego = LaberintoAsterionASCII()
        juego.jugar()
    except KeyboardInterrupt:
        print(f"\n\n{Color.BRIGHT_YELLOW}[!] Juego interrumpido por el usuario.{Color.RESET}\n")
    except Exception as e:
        print(f"\n{Color.BRIGHT_RED}[ERR] Error inesperado: {e}{Color.RESET}\n")


if __name__ == "__main__":
    main()
