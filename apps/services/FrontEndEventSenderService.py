from apps import emit
from apps.constants.SocketMessageTypeConstants import SOCKET_EVENT_QUIZ_NEXT_QUESTION, \
    SOCKET_EVENT_STATS_ANSWERS_ONGOING, SOCKET_EVENT_STATS_ANSWERS_QUESTION, SOCKET_EVENT_QUIZ_STOP
from apps.services.stores.QuizStore import quiz_store


"""
FrontEndEventSenderService
--------------------------

Contains all methods to send events for show something on the frontend.
"""


def sendNextQuestion() -> None:
    """
    Send event to frontend the next question.
    """
    emit(
        SOCKET_EVENT_QUIZ_NEXT_QUESTION,
        {
            "index": quiz_store.currentQuestionIndex,
            "question": quiz_store.listQuestions[quiz_store.currentQuestionIndex - 1].toJson()
        }
    )


def sendStatsAnswersOngoing() -> None:
    """
    Send stats to frontend containing the number of player which gave an answer.
    """
    emit(
        SOCKET_EVENT_STATS_ANSWERS_ONGOING,
        {
            "numberAnswers": len(list(
                filter(lambda contestant: contestant.selected_answer is not None,
                       quiz_store.listContestants)
            ))
        }
    )


def sendStatsAnswerQuestion() -> None:
    """
    Send stats of the last question. (Each number of vote for each answer)
    """
    # TODO
    emit(
        SOCKET_EVENT_STATS_ANSWERS_QUESTION,
        {}
    )

def sendEventStopQuiz() -> None:
    """
    Send an event to stop the quiz.
    """
    emit(
        SOCKET_EVENT_QUIZ_STOP
    )
