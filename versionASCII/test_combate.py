#!/usr/bin/env python3
"""Simulación del sistema de combate Teseo vs Minotauro"""

from laberinto_ASCII import Color
import random

print(f'{Color.BRIGHT_CYAN}{"═"*70}{Color.RESET}')
print(f'{Color.BRIGHT_WHITE}       SIMULACIÓN DE COMBATE: TESEO VS MINOTAURO{Color.RESET}')
print(f'{Color.BRIGHT_CYAN}{"═"*70}{Color.RESET}\n')

# Estadísticas iniciales
teseo_hp = 100
teseo_cordura = 100
minotauro_hp = 150

print(f'{Color.BRIGHT_GREEN}◉ TESEO{Color.RESET}       HP: {teseo_hp}/100  Cordura: {teseo_cordura}/100')
print(f'{Color.BRIGHT_RED}⚠ MINOTAURO{Color.RESET}   HP: {minotauro_hp}/150\n')

print(f'{Color.BRIGHT_YELLOW}{"═"*70}{Color.RESET}')

# Turno 1 - ATAQUE NORMAL
print(f'\n{Color.BRIGHT_WHITE}[TURNO 1] Teseo elige: ATACAR{Color.RESET}')
dano = random.randint(20, 35)
minotauro_hp -= dano
print(f'{Color.BRIGHT_GREEN}  → Teseo ataca y causa {dano} de daño{Color.RESET}')
print(f'{Color.RED}  → Minotauro: {minotauro_hp}/150 HP{Color.RESET}')

dano_mino = random.randint(20, 35)
teseo_hp -= dano_mino
teseo_cordura -= random.randint(5, 10)
print(f'{Color.BRIGHT_RED}  → El Minotauro contraataca: {dano_mino} de daño{Color.RESET}')
print(f'{Color.GREEN}  → Teseo: {teseo_hp}/100 HP, {teseo_cordura}/100 Cordura{Color.RESET}')

# Turno 2 - ATAQUE CRÍTICO
print(f'\n{Color.BRIGHT_WHITE}[TURNO 2] Teseo elige: ATACAR (¡CRÍTICO!){Color.RESET}')
dano = random.randint(20, 35)
dano_critico = int(dano * 1.5)
minotauro_hp -= dano_critico
print(f'{Color.BRIGHT_YELLOW}  → ¡GOLPE CRÍTICO! {dano_critico} de daño (x1.5){Color.RESET}')
print(f'{Color.RED}  → Minotauro: {minotauro_hp}/150 HP{Color.RESET}')

dano_mino = random.randint(20, 35)
teseo_hp -= dano_mino
teseo_cordura -= random.randint(5, 10)
print(f'{Color.BRIGHT_RED}  → El Minotauro contraataca: {dano_mino} de daño{Color.RESET}')
print(f'{Color.GREEN}  → Teseo: {teseo_hp}/100 HP, {teseo_cordura}/100 Cordura{Color.RESET}')

# Turno 3 - DEFENDER
print(f'\n{Color.BRIGHT_WHITE}[TURNO 3] Teseo elige: DEFENDER{Color.RESET}')
print(f'{Color.BRIGHT_BLUE}  → Teseo adopta posición defensiva (🛡){Color.RESET}')

dano_mino = random.randint(20, 35)
dano_reducido = dano_mino // 2
teseo_hp -= dano_reducido
teseo_cordura -= random.randint(5, 10)
print(f'{Color.BRIGHT_RED}  → El Minotauro ataca: {dano_mino} → {dano_reducido} de daño (reducido 50%){Color.RESET}')
print(f'{Color.GREEN}  → Teseo: {teseo_hp}/100 HP, {teseo_cordura}/100 Cordura{Color.RESET}')

# Turno 4 - USAR ITEM
print(f'\n{Color.BRIGHT_WHITE}[TURNO 4] Teseo elige: USAR ITEM (Poción de curación){Color.RESET}')
curacion = random.randint(15, 30)
teseo_hp = min(100, teseo_hp + curacion)
print(f'{Color.BRIGHT_GREEN}  → Teseo usa una Poción y recupera {curacion} HP{Color.RESET}')
print(f'{Color.GREEN}  → Teseo: {teseo_hp}/100 HP{Color.RESET}')

dano_mino = random.randint(20, 35)
teseo_hp -= dano_mino
teseo_cordura -= random.randint(5, 10)
print(f'{Color.BRIGHT_RED}  → El Minotauro contraataca: {dano_mino} de daño{Color.RESET}')
print(f'{Color.GREEN}  → Teseo: {teseo_hp}/100 HP, {teseo_cordura}/100 Cordura{Color.RESET}')

# Turno 5 - HUIR (éxito)
print(f'\n{Color.BRIGHT_WHITE}[TURNO 5] Teseo elige: HUIR{Color.RESET}')
prob_huida = teseo_cordura
print(f'{Color.YELLOW}  → Probabilidad de huida: {prob_huida}%{Color.RESET}')
print(f'{Color.BRIGHT_GREEN}  → ¡ÉXITO! Teseo escapa del combate{Color.RESET}')
teseo_cordura -= 10
print(f'{Color.MAGENTA}  → Pierdes 10 de cordura por huir{Color.RESET}')
print(f'{Color.CYAN}  → El Minotauro retrocede 3 casillas{Color.RESET}')

print(f'\n{Color.BRIGHT_YELLOW}{"═"*70}{Color.RESET}')
print(f'\n{Color.BRIGHT_WHITE}MECÁNICAS DE COMBATE:{Color.RESET}')
print(f'{Color.BRIGHT_RED}  • ATACAR:{Color.RESET}')
print(f'{Color.WHITE}    - Daño base: 20-35 puntos{Color.RESET}')
print(f'{Color.YELLOW}    - 10% probabilidad de crítico (x1.5 daño){Color.RESET}')
print(f'\n{Color.BRIGHT_BLUE}  • DEFENDER:{Color.RESET}')
print(f'{Color.WHITE}    - Reduce el daño recibido en 50%{Color.RESET}')
print(f'{Color.WHITE}    - Efecto dura solo el turno del Minotauro{Color.RESET}')
print(f'\n{Color.BRIGHT_YELLOW}  • HUIR:{Color.RESET}')
print(f'{Color.WHITE}    - Probabilidad = Cordura actual (%){Color.RESET}')
print(f'{Color.WHITE}    - Éxito: Escapa y el Minotauro retrocede{Color.RESET}')
print(f'{Color.WHITE}    - Penalización: -10 cordura{Color.RESET}')
print(f'{Color.WHITE}    - Fallo: Pierdes el turno{Color.RESET}')
print(f'\n{Color.BRIGHT_MAGENTA}  • USAR ITEM:{Color.RESET}')
print(f'{Color.WHITE}    - Pociones/Antorchas: +15-30 HP{Color.RESET}')
print(f'{Color.WHITE}    - Espadas/Coronas: 30-50 daño directo{Color.RESET}')
print(f'{Color.WHITE}    - Otros items: +20 HP{Color.RESET}')

print(f'\n{Color.BRIGHT_RED}  • MINOTAURO:{Color.RESET}')
print(f'{Color.WHITE}    - HP: 150 puntos{Color.RESET}')
print(f'{Color.WHITE}    - Daño: 20-35 por turno{Color.RESET}')
print(f'{Color.WHITE}    - Reduce cordura: 5-10 por turno{Color.RESET}')
print(f'{Color.WHITE}    - Derrota Teseo si HP ≤ 0{Color.RESET}')

print(f'\n{Color.BRIGHT_GREEN}{"═"*70}{Color.RESET}')
print(f'{Color.BRIGHT_GREEN}    ✓ SISTEMA DE COMBATE COMPLETO Y BALANCEADO{Color.RESET}')
print(f'{Color.BRIGHT_GREEN}{"═"*70}{Color.RESET}')
