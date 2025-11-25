from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os

from game_controller import manager

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/health')
def health():
    return jsonify({'status': 'ok'})


@app.route('/api/start', methods=['POST'])
def api_start():
    data = request.json or {}
    seed = data.get('seed')
    config_path = data.get('config_path')
    session_id, state = manager.start_game(seed=seed, config_path=config_path)
    return jsonify({'session_id': session_id, 'state': state})


@app.route('/api/action', methods=['POST'])
def api_action():
    data = request.json or {}
    session_id = data.get('session_id')
    action = data.get('action')
    if not session_id:
        return jsonify({'error': 'missing session_id'}), 400

    # Map simple payloads into manager actions
    if action in ('N', 'S', 'E', 'O', 'HELP', 'H'):
        result = manager.perform_action(session_id, action)
        return jsonify(result)

    if action == 'pick':
        personaje_id = data.get('personaje_id')
        choice = data.get('choice')
        result = manager.perform_action(session_id, 'pick', personaje_id=personaje_id, choice=choice)
        return jsonify(result)

    if action == 'start_combat':
        result = manager.perform_action(session_id, 'start_combat')
        return jsonify(result)

    if action == 'combat':
        sub = data.get('subaction')
        item_index = data.get('item_index')
        result = manager.perform_action(session_id, 'combat', subaction=sub, item_index=item_index)
        return jsonify(result)

    return jsonify({'error': 'unknown action'}), 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
