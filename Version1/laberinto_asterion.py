#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
El Laberinto de Asterión
Aventura Interactiva de Teseo

Este juego carga toda su configuración desde context.json
"""

import json
import random
from pathlib import Path


class LaberintoAsterion:
    """Clase principal del juego El Laberinto de Asterión"""
    
    def __init__(self, config_path="context.json"):
        """Inicializa el juego cargando la configuración desde JSON"""
        self.config = self.cargar_configuracion(config_path)
        self.tablero = None
        self.posicion = None
        self.jugador = None
        self.personajes_en_tablero = {}
        self.inicializar_juego()
    
    def cargar_configuracion(self, config_path):
        """Carga el archivo de configuración JSON"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {config_path}")
            exit(1)
        except json.JSONDecodeError:
            print(f"Error: El archivo {config_path} no es un JSON válido")
            exit(1)
    
    def inicializar_juego(self):
        """Inicializa el tablero, jugador y personajes"""
        # Crear tablero 10x10
        n = 10
        self.tablero = [[None for _ in range(n)] for _ in range(n)]
        
        # Posición inicial del jugador (centro)
        self.posicion = [n // 2, n // 2]
        
        # Inicializar estadísticas del jugador desde config
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
        
        # Colocar personajes aleatoriamente en el tablero
        self.colocar_personajes()
    
    def colocar_personajes(self):
        """Coloca los 5 personajes aliados en posiciones aleatorias del tablero"""
        personajes = self.config['personajes_aliados']['lista']
        coords = self.generar_posiciones_aleatorias(10, len(personajes))
        
        for personaje, coord in zip(personajes, coords):
            x, y = coord
            # Guardamos el ID del personaje en el tablero
            self.tablero[x][y] = personaje['id']
            # Guardamos la info completa del personaje en un diccionario
            self.personajes_en_tablero[personaje['id']] = personaje
    
    def generar_posiciones_aleatorias(self, n, k):
        """Genera k posiciones únicas aleatorias en el tablero nxn"""
        coords = set()
        while len(coords) < k:
            coords.add((random.randrange(n), random.randrange(n)))
        return list(coords)
    
    def mostrar_titulo(self):
        """Muestra el título del juego"""
        info = self.config['game_info']
        lore = self.config['lore_context']
        
        print("\n" + "="*60)
        print(f"  {info['titulo'].upper()}")
        print(f"  {info['subtitulo']}")
        print("="*60)
        print(f"\n[*] Ubicación: {lore['ubicacion']}")
        print(f"[!] Protagonista: {lore['protagonista']}")
        print(f"[X] Enemigo: {lore['villano_principal']}")
        print(f"\n[>] Objetivo: {self.config['reglas_juego']['objetivo_principal']}")
        print("\n" + "="*60 + "\n")
    
    def mostrar_estado_jugador(self):
        """Muestra las estadísticas actuales del jugador"""
        print(f"\n{'─'*60}")
        print(f"[@] {self.jugador['nombre']} | ", end="")
        print(f"[HP] Salud: {self.jugador['salud']} | ", end="")
        print(f"[CD] Cordura: {self.jugador['cordura']} | ", end="")
        print(f"[--] Hilo: {self.jugador['hilo_ariadna']} | ", end="")
        print(f"[**] Puntos: {self.jugador['puntos']}")
        print(f"[##] Inventario ({len(self.jugador['inventario'])}/5): {', '.join(self.jugador['inventario']) if self.jugador['inventario'] else 'Vacío'}")
        print(f"{'─'*60}\n")
    
    def verificar_condiciones_derrota(self):
        """Verifica si el jugador ha perdido"""
        if self.jugador['salud'] <= 0:
            print("\n[XX] Tu salud ha llegado a 0. Has muerto en el laberinto...")
            return True
        
        if self.jugador['cordura'] <= 0:
            print("\n[@@] Tu cordura se ha desvanecido. Te pierdes en la locura del laberinto...")
            return True
        
        if self.jugador['hilo_ariadna'] <= 0:
            print("\n[--] El Hilo de Ariadna se ha agotado. Estás perdido para siempre...")
            return True
        
        return False
    
    def encontrar_personaje(self, personaje_id):
        """Maneja el encuentro con un personaje aliado"""
        personaje = self.personajes_en_tablero[personaje_id]
        
        print(f"\n{'='*60}")
        print(f"[+] ¡Has encontrado a {personaje['nombre']}!")
        print(f"{'='*60}")
        print(f"\n[i] {personaje['descripcion']}")
        print(f"\n[~] {personaje['nombre']}: \"{personaje['dialogo_encuentro']}\"\n")
        
        # Mostrar opciones de objetos
        objetos = personaje['objetos_disponibles']
        print("[?] Objetos disponibles:\n")
        
        for idx, obj in enumerate(objetos, 1):
            print(f"  {idx}) {obj['nombre']}")
            print(f"     Tipo: {obj['tipo']}")
            print(f"     {obj['descripcion']}")
            
            # Mostrar estadísticas específicas del objeto
            if 'dano' in obj:
                print(f"     [ATK] Daño: {obj['dano']}")
            if 'defensa' in obj:
                print(f"     [DEF] Defensa: {obj['defensa']}")
            if 'habilidad' in obj:
                print(f"     [SKL] Habilidad: {obj['habilidad']}")
            if 'poder' in obj:
                print(f"     [PWR] Poder: {obj['poder']}")
            print()
        
        # Solicitar elección del jugador
        while True:
            try:
                eleccion = int(input("Elige un objeto (1-3): "))
                if 1 <= eleccion <= 3:
                    objeto_elegido = objetos[eleccion - 1]
                    break
                else:
                    print("[!] Opción inválida. Elige 1, 2 o 3.")
            except ValueError:
                print("[!] Por favor ingresa un número.")
        
        # Agregar objeto al inventario
        self.jugador['inventario'].append(objeto_elegido['nombre'])
        print(f"\n[OK] Has obtenido: {objeto_elegido['nombre']}")
        
        # Remover personaje del tablero
        x, y = self.posicion
        self.tablero[x][y] = None
        
        # Aplicar subefecto aleatorio
        self.aplicar_subefecto()
    
    def aplicar_subefecto(self):
        """Aplica un efecto aleatorio después de recoger un objeto"""
        efectos = self.config['sistema_subefectos']['efectos_posibles']
        efecto = random.choice(efectos)
        
        self.jugador[efecto['tipo']] += efecto['valor']
        
        print(f"\n[?] Subefecto: {efecto['descripcion']}")
        
        # Mostrar cambio
        signo = '+' if efecto['valor'] > 0 else ''
        print(f"   {efecto['tipo'].capitalize()}: {signo}{efecto['valor']}")
    
    def mover_jugador(self):
        """Solicita y procesa el movimiento del jugador"""
        print("\n[^] Direcciones disponibles:")
        print("   N (Norte) | S (Sur) | E (Este) | O (Oeste)")
        
        mov = input("\nElige dirección: ").upper().strip()
        
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
            print("[!] Movimiento inválido. No puedes salir del laberinto.")
            return
        
        if movimiento_valido:
            # Consumir hilo de Ariadna
            self.jugador['hilo_ariadna'] -= 1
            print(f"[OK] Te has movido hacia el {mov}")
            print(f"   [--] Hilo de Ariadna restante: {self.jugador['hilo_ariadna']}")
    
    def determinar_final(self):
        """Determina qué final obtiene el jugador según su inventario"""
        inventario_set = set(self.jugador['inventario'])
        finales = self.config['finales_posibles']['finales']
        
        print("\n" + "="*60)
        print("  [!!!] ENFRENTAMIENTO FINAL CON ASTERIÓN")
        print("="*60 + "\n")
        
        print(f"Con tu inventario completo, te adentras al centro del laberinto...")
        print(f"Objetos recolectados: {', '.join(self.jugador['inventario'])}\n")
        
        input("Presiona ENTER para enfrentar al Minotauro...")
        
        # Buscar final válido
        final_encontrado = None
        for final in finales:
            combo_requerida = set(final['combinacion_requerida'])
            if inventario_set == combo_requerida:
                final_encontrado = final
                break
        
        print("\n" + "="*60)
        
        if final_encontrado:
            print(f"  [***] {final_encontrado['nombre']}")
            print("="*60)
            print(f"\n{final_encontrado['descripcion']}\n")
            print(f"[>] {final_encontrado['narrativa']}")
            print(f"\n[WIN] ¡VICTORIA! Has derrotado a Asterión y escapado del laberinto.")
        else:
            # Final de derrota
            final_derrota = self.config['finales_posibles']['final_derrota']
            print(f"  [XXX] {final_derrota['nombre']}")
            print("="*60)
            print(f"\n{final_derrota['descripcion']}\n")
            print(f"[>] {final_derrota['narrativa']}")
            print(f"\n[XXX] DERROTA. El laberinto reclama otra víctima...")
        
        print("\n" + "="*60)
        print(f"  Puntuación Final: {self.jugador['puntos']} puntos")
        print("="*60 + "\n")
    
    def jugar(self):
        """Bucle principal del juego"""
        self.mostrar_titulo()
        
        print("Comienzas tu aventura en el centro del laberinto...")
        print("Debes encontrar a los 5 aliados dispersos y recolectar sus objetos.\n")
        
        input("Presiona ENTER para comenzar...")
        
        # Bucle principal: hasta recolectar 5 objetos o morir
        while len(self.jugador['inventario']) < 5:
            # Verificar condiciones de derrota
            if self.verificar_condiciones_derrota():
                print("\n[XXX] GAME OVER")
                return
            
            # Mostrar estado
            self.mostrar_estado_jugador()
            
            x, y = self.posicion
            print(f"[*] Posición actual: Sala ({x}, {y})")
            
            # Verificar si hay personaje en esta celda
            personaje_id = self.tablero[x][y]
            if personaje_id:
                self.encontrar_personaje(personaje_id)
            else:
                print("   Esta sala está vacía. Continúa explorando...")
            
            # Mover jugador
            self.mover_jugador()
        
        # Final del juego
        self.determinar_final()


def main():
    """Función principal"""
    juego = LaberintoAsterion("context.json")
    juego.jugar()


if __name__ == "__main__":
    main()
