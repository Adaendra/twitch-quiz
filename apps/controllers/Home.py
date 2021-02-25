from apps import app, render_template, emit, socketio


class Home(object):

    @app.route('/', methods=['GET', 'POST'])
    def Home():
        return render_template('twitch_quiz_frontend/index.html')


    @socketio.on('my event')
    def handle_my_custom_event(json):
        print('received my event: ' + str(json))
        emit('my response', json)
