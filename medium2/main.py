from operator import index
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send




app = Flask(__name__)
app.config['SECRET_KEY'] = 'bruhhh'
socketio = SocketIO(app)



@app.route('/')
def main():
    return render_template('index.html')


dummy_message = ['bruh1', 'bruh2', 'bruh3', 'bruh4', 'bruh5']
i = 0
@socketio.on('message')
def message(msg):
    global i
    if i<len(dummy_message):
        socketio.send(dummy_message[i])
        i += 1
    else:
        i = 0


if __name__ == '__main__':
    socketio.run(app, port=8080)