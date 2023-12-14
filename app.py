from flask import Flask, render_template
from flask_socketio import SocketIO
from tqdm import tqdm
from time import sleep
import psutil
import threading
import os
from algorithms.aes import encrypt_aes
from algorithms.rsa import generate_rsa_keypair, save_rsa_key_to_file, load_rsa_key_from_file, encrypt_rsa
from algorithms.chacha20 import encrypt_chacha20
from algorithms.copy_large_file import copy_large_file
from algorithms.process_api_data import process_api_data
from algorithms.process_file import process_file

app = Flask(__name__)
socketio = SocketIO(app)

# PID of the process to monitor progress
target_pid = os.getpid()  # Change this to the actual PID

def monitor_progress():
    with tqdm(total=100, desc='cpu%', position=1, leave=False, file=open(os.devnull, 'w')) as cpubar, \
            tqdm(total=100, desc='ram%', position=0, leave=False, file=open(os.devnull, 'w')) as rambar, \
            tqdm(total=100, desc='disk%', position=2, leave=False, file=open(os.devnull, 'w')) as diskbar:
        while True:
            # Get information about the process with the specified PID
            process = psutil.Process(target_pid)

            # Update progress bars based on CPU and RAM load of the process
            cpubar.n = process.cpu_percent(interval=0.5)
            rambar.n = process.memory_percent()

            # Disk information
            disk_usage = psutil.disk_usage('/')
            diskbar.n = disk_usage.percent

            socketio.emit('update_progress', {'cpu': cpubar.n, 'ram': rambar.n, 'disk': diskbar.n}, namespace='/test')

            rambar.refresh()
            cpubar.refresh()
            diskbar.refresh()
            sleep(0.5)

def start_another_app():
    # Start another Python application after 5 seconds
    sleep(5)

    # AES encryption application
    key = os.urandom(32)
    file_to_encrypt = 'secret_message.txt'
    encrypt_aes(key, file_to_encrypt)

    # RSA encryption application
    private_key_file = 'private_key.pem'
    if not os.path.exists(private_key_file):
        private_key, public_key = generate_rsa_keypair()
        save_rsa_key_to_file(private_key, private_key_file, password=b'MySecurePassword')
        save_rsa_key_to_file(public_key, 'public_key.pem')

    # Load the private key
    loaded_private_key = load_rsa_key_from_file(private_key_file, password=b'MySecurePassword')
    encrypt_rsa(loaded_private_key, file_to_encrypt)

    # ChaCha20 encryption application
    encrypt_chacha20(key, file_to_encrypt)

    # I/O application copy_large_file.py
    copy_large_file(file_to_encrypt, 'large_file_output.txt')

    # I/O application process_api_data.py
    api_url = "https://jsonplaceholder.typicode.com/users"
    process_api_data(api_url)

    # I/O application process_file.py
    process_file(file_to_encrypt, 'process_file_output.txt')

    sleep(5)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')

if __name__ == '__main__':
    # Start the progress monitoring thread
    monitor_thread = threading.Thread(target=monitor_progress, daemon=True)
    monitor_thread.start()

    # Start the thread that launches another application
    start_app_thread = threading.Thread(target=start_another_app)
    start_app_thread.start()

    # Run the Flask-SocketIO server on port 8080
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)
