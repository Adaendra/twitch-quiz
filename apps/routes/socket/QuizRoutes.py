from apps import socketio, emit


# Socket routes for quiz events.
class QuizRoutes(object):

    @socketio.on('my_event')
    def handle_my_custom_event(json):
        print('received my event: ' + str(json))
        emit('my_response', json)
