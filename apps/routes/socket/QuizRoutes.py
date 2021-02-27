from apps import socketio, emit


class QuizRoutes(object):

    @socketio.on('my event')
    def handle_my_custom_event(json):
        print('received my event: ' + str(json))
        emit('my response', json)
