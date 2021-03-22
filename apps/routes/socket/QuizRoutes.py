from apps import socketio
from apps.controllers.QuizController import quizController
from apps.constants.SocketMessageTypeConstants import SOCKET_REQUEST_QUIZ_INIT, SOCKET_REQUEST_START_QUIZ


class QuizRoutes(object):
    """
    QuizRoutes
    ----------

    Socket routes for quiz events.
    """

    @socketio.on(SOCKET_REQUEST_QUIZ_INIT)
    def initQuiz():
        """
        Initialize quiz.
        """
        quizController.init_quiz()

    @socketio.on(SOCKET_REQUEST_START_QUIZ)
    def startQuiz():
        """
        Start quiz.
        """
        quizController.start_quiz()

