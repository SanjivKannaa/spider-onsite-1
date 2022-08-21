from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
socketio = SocketIO(app)



@app.route('/')
def main():
    return render_template('index.html')

'''
@socketio.on('connect')
def connect():
    send("connected")
'''

if __name__ == '__main__':
    socketio.run(app, port=5000)