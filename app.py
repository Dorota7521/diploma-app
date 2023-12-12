from flask import Flask, render_template
from flask_socketio import SocketIO
from tqdm import tqdm
from time import sleep
import psutil
import threading
import os
import subprocess
from algorithms.aes import encrypt_aes

app = Flask(__name__)
socketio = SocketIO(app)

# PID procesu, którego postęp chcesz monitorować
target_pid = os.getpid()  # Zmień to na rzeczywisty PID

def monitor_progress():
    with tqdm(total=100, desc='cpu%', position=1, leave=False, file=open(os.devnull, 'w')) as cpubar, \
            tqdm(total=100, desc='ram%', position=0, leave=False, file=open(os.devnull, 'w')) as rambar, \
            tqdm(total=100, desc='disk%', position=2, leave=False, file=open(os.devnull, 'w')) as diskbar:
        while True:
            # Pobierz informacje o procesie o określonym PID
            process = psutil.Process(target_pid)

            # Aktualizuj paski postępu na podstawie obciążenia CPU i pamięci RAM procesu
            cpubar.n = process.cpu_percent()
            rambar.n = process.memory_percent()

            # Informacje o dysku
            disk_usage = psutil.disk_usage('/')
            diskbar.n = disk_usage.percent

            socketio.emit('update_progress', {'cpu': cpubar.n, 'ram': rambar.n, 'disk': diskbar.n}, namespace='/test')

            rambar.refresh()
            cpubar.refresh()
            diskbar.refresh()
            sleep(0.5)

def start_another_app():
    # Uruchom inną aplikację Pythona po 5 sekundach
    sleep(5)
    key = b'sixteen_byte_key'  # 128-bit key for AES-128
    plik = 'secret_message.txt'
    encrypt_aes(key, plik)
    sleep(5)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')

if __name__ == '__main__':
    # Uruchom wątek monitorowania postępu
    monitor_thread = threading.Thread(target=monitor_progress, daemon=True)
    monitor_thread.start()

    # Uruchom wątek startujący inną aplikację
    start_app_thread = threading.Thread(target=start_another_app)
    start_app_thread.start()

    # Uruchom serwer Flask-SocketIO
    socketio.run(app, debug=True)













