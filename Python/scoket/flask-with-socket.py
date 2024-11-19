from flask import Flask, jsonify
import socket
import threading
import time

app = Flask(__name__)

# TCP Server Configuration
TCP_SERVER_HOST = 'your_tcp_server_host'
TCP_SERVER_PORT = 12345  # Replace with your actual port

# Flag to indicate the status of the TCP connection
tcp_connection_status = False

# Function to check the TCP connection
def check_tcp_connection():
    global tcp_connection_status
    try:
        with socket.create_connection((TCP_SERVER_HOST, TCP_SERVER_PORT), timeout=5):
            tcp_connection_status = True
    except Exception as e:
        print(f"Error checking TCP connection: {e}")
        tcp_connection_status = False

# Function to run in the background and check TCP connection every 9 minutes
def background_task():
    while True:
        check_tcp_connection()
        time.sleep(9 * 60)

# Start the background thread
background_thread = threading.Thread(target=background_task)
background_thread.start()

# Flask route to get the status of the TCP connection
@app.route('/tcp-connection-status', methods=['GET'])
def get_tcp_connection_status():
    return jsonify({'status': 'alive' if tcp_connection_status else 'dead'})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)