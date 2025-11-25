const outputDiv = document.getElementById('output');
const cmdInput = document.getElementById('cmd-input');

let pollInterval = null;
let gameStarted = false;

// Auto-start game on load
window.onload = async () => {
    await startGame();
    cmdInput.focus();
};

async function startGame() {
    const res = await fetch('/api/start', { method: 'POST' });
    const data = await res.json();

    if (data.status === 'success') {
        gameStarted = true;
        // Start polling for output
        pollInterval = setInterval(pollOutput, 100);
    }
}

async function pollOutput() {
    if (!gameStarted) return;

    const res = await fetch('/api/output');
    const data = await res.json();

    if (data.status === 'success' && data.output) {
        appendOutput(data.output);
    }
}

function appendOutput(text) {
    // Convert ANSI codes to HTML
    const html = ansiToHtml(text);
    outputDiv.innerHTML += html;
    outputDiv.scrollTop = outputDiv.scrollHeight;
}

function ansiToHtml(text) {
    // Basic ANSI color code mapping
    const colorMap = {
        '0': 'reset',
        '30': 'black', '31': 'red', '32': 'green', '33': 'yellow',
        '34': 'blue', '35': 'magenta', '36': 'cyan', '37': 'white',
        '90': 'bright-black', '91': 'bright-red', '92': 'bright-green', '93': 'bright-yellow',
        '94': 'bright-blue', '95': 'bright-magenta', '96': 'bright-cyan', '97': 'bright-white',
        '1': 'bold', '2': 'dim', '3': 'italic', '4': 'underline'
    };
    
    let html = '';
    let currentClasses = [];
    let buffer = '';
    let i = 0;
    
    function flushBuffer() {
        if (buffer) {
            // Escape HTML but preserve spaces
            let escaped = buffer
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/ /g, '&nbsp;');
            
            if (currentClasses.length > 0) {
                html += `<span class="${currentClasses.join(' ')}">${escaped}</span>`;
            } else {
                html += escaped;
            }
            buffer = '';
        }
    }
    
    while (i < text.length) {
        if (text[i] === '\x1b' && text[i + 1] === '[') {
            // Flush buffer before changing style
            flushBuffer();
            
            // ANSI escape sequence
            let j = i + 2;
            while (j < text.length && text[j] !== 'm') j++;
            
            const codes = text.substring(i + 2, j).split(';');
            
            for (const code of codes) {
                if (code === '0') {
                    currentClasses = [];
                } else if (colorMap[code]) {
                    currentClasses.push('ansi-' + colorMap[code]);
                }
            }
            
            i = j + 1;
        } else if (text[i] === '\n') {
            flushBuffer();
            html += '<br>';
            i++;
        } else if (text[i] === '\r') {
            // Ignore carriage return
            i++;
        } else {
            // Add to buffer
            buffer += text[i];
            i++;
        }
    }
    
    flushBuffer();
    return html;
}

// Input handling
cmdInput.addEventListener('keydown', async (e) => {
    if (e.key === 'Enter') {
        const input = cmdInput.value;
        cmdInput.value = '';

        // Send input to backend
        await fetch('/api/input', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ input })
        });
    }
});

// Cleanup on page unload
window.addEventListener('beforeunload', () => {
    if (pollInterval) clearInterval(pollInterval);
    fetch('/api/stop', { method: 'POST' });
});
