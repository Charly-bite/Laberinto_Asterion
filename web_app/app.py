import os
import sys
import pty
import select
import subprocess
import termios
import struct
import fcntl
from flask import Flask, render_template, jsonify, request, session
from threading import Thread, Lock
import uuid

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Store active game sessions
# Key: session_id, Value: {'process': subprocess, 'fd': file_descriptor, 'output_buffer': []}
SESSIONS = {}
SESSIONS_LOCK = Lock()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/start', methods=['POST'])
def start_game():
    """Start a new game session with a pseudo-terminal"""
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    
    user_id = session['user_id']
    
    # Clean up existing session if any
    with SESSIONS_LOCK:
        if user_id in SESSIONS:
            try:
                SESSIONS[user_id]['process'].terminate()
                os.close(SESSIONS[user_id]['fd'])
            except:
                pass
            del SESSIONS[user_id]
    
    # Start the game in a pseudo-terminal
    game_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'versionASCII', 'laberinto_ASCII.py'))
    
    # Create a pseudo-terminal
    master_fd, slave_fd = pty.openpty()
    
    # Set terminal size (rows, cols)
    winsize = struct.pack('HHHH', 40, 120, 0, 0)
    fcntl.ioctl(slave_fd, termios.TIOCSWINSZ, winsize)
    
    # Start the process
    process = subprocess.Popen(
        ['python3', game_path],
        stdin=slave_fd,
        stdout=slave_fd,
        stderr=slave_fd,
        cwd=os.path.dirname(game_path),
        env={**os.environ, 'TERM': 'xterm-256color'}
    )
    
    os.close(slave_fd)
    
    # Make master_fd non-blocking
    flags = fcntl.fcntl(master_fd, fcntl.F_GETFL)
    fcntl.fcntl(master_fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
    
    with SESSIONS_LOCK:
        SESSIONS[user_id] = {
            'process': process,
            'fd': master_fd,
            'output_buffer': []
        }
    
    return jsonify({'status': 'success', 'message': 'Game started'})

@app.route('/api/input', methods=['POST'])
def send_input():
    """Send input to the game"""
    if 'user_id' not in session or session['user_id'] not in SESSIONS:
        return jsonify({'status': 'error', 'message': 'No active session'}), 404
    
    user_id = session['user_id']
    data = request.json
    user_input = data.get('input', '')
    
    with SESSIONS_LOCK:
        if user_id not in SESSIONS:
            return jsonify({'status': 'error', 'message': 'Session expired'}), 404
        
        fd = SESSIONS[user_id]['fd']
        
        try:
            # Send input with newline
            os.write(fd, (user_input + '\n').encode('utf-8'))
            return jsonify({'status': 'success'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/output', methods=['GET'])
def get_output():
    """Get output from the game"""
    if 'user_id' not in session or session['user_id'] not in SESSIONS:
        return jsonify({'status': 'error', 'message': 'No active session'}), 404
    
    user_id = session['user_id']
    
    with SESSIONS_LOCK:
        if user_id not in SESSIONS:
            return jsonify({'status': 'error', 'message': 'Session expired'}), 404
        
        fd = SESSIONS[user_id]['fd']
        output = []
        
        try:
            while True:
                ready, _, _ = select.select([fd], [], [], 0.1)
                if ready:
                    chunk = os.read(fd, 4096).decode('utf-8', errors='replace')
                    if chunk:
                        output.append(chunk)
                    else:
                        break
                else:
                    break
        except Exception as e:
            pass
        
        return jsonify({'status': 'success', 'output': ''.join(output)})

@app.route('/api/stop', methods=['POST'])
def stop_game():
    """Stop the game session"""
    if 'user_id' not in session:
        return jsonify({'status': 'success'})
    
    user_id = session['user_id']
    
    with SESSIONS_LOCK:
        if user_id in SESSIONS:
            try:
                SESSIONS[user_id]['process'].terminate()
                os.close(SESSIONS[user_id]['fd'])
            except:
                pass
            del SESSIONS[user_id]
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
