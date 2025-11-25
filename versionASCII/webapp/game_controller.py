import uuid
import os
import sys

# Ensure parent folder is on sys.path so we can import the game module
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from laberinto_ASCII import LaberintoAsterionASCII

# Simple in-memory session manager mapping session_id -> game instance
class GameManager:
    def __init__(self):
        self.sessions = {}

    def start_game(self, seed=None, config_path=None):
        session_id = str(uuid.uuid4())
        game = LaberintoAsterionASCII(config_path=config_path, seed=seed)
        self.sessions[session_id] = game
        return session_id, game.get_state()

    def get_state(self, session_id):
        game = self.sessions.get(session_id)
        if not game:
            return None
        return game.get_state()

    def perform_action(self, session_id, action, **kwargs):
        game = self.sessions.get(session_id)
        if not game:
            return {'error': 'invalid session'}

        # Dispatch simple actions
        if action in ('N', 'S', 'E', 'O', 'HELP', 'H'):
            return game.mover_jugador_headless(action)

        if action == 'pick':
            personaje_id = kwargs.get('personaje_id')
            choice = kwargs.get('choice')
            return game.encontrar_personaje_headless(personaje_id, choice)

        if action == 'start_combat':
            return game.start_minotauro_combat()

        if action == 'combat':
            sub = kwargs.get('subaction')
            item_index = kwargs.get('item_index')
            return game.combat_action(sub, item_index)

        return {'error': 'unknown action'}


manager = GameManager()
