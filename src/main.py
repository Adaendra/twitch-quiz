from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

@app.route('/')
def sessions():
    return render_template('index.html')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    emit('my response', json)

