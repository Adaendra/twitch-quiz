from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


if __name__ == '__main__':
    socketio.run(app)

@app.route('/')
def siteIndex():
    return render_template('twitch_quiz_frontend/index.html')


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    emit('my response', json)

