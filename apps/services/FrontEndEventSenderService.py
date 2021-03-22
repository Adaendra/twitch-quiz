from apps import emit
from apps.constants.SocketMessageTypeConstants import SOCKET_EVENT_QUIZ_NEXT_QUESTION, \
    SOCKET_EVENT_STATS_ANSWERS_ONGOING, SOCKET_EVENT_STATS_ANSWERS_QUESTION, SOCKET_EVENT_QUIZ_STOP, \
    SOCKET_EVENT_REVEAL_ANSWER, SOCKET_EVENT_RANKING, SOCKET_EVENT_QUIZ_STOP_NO_WINNER, SOCKET_EVENT_QUIZ_STOP_WINNER, \
    SOCKET_EVENT_QUIZ_STOP_NO_QUESTIONS, SOCKET_EVENT_QUIZ_CONTINUE
from apps.constants.QuizConstants import SELECTED_ANSWER_A, SELECTED_ANSWER_B, SELECTED_ANSWER_C, SELECTED_ANSWER_D
from apps.services.stores.QuizStore import quiz_store
from apps.models.Ranking import Ranking

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


def sendEventRevealAnswer() -> None:
    """
    Send the answer to the front client.
    """
    emit(
        SOCKET_EVENT_REVEAL_ANSWER,
        {
            "answer": quiz_store.listQuestions[quiz_store.currentQuestionIndex - 1].answer
        }
    )


def sendStatsAnswerQuestion() -> None:
    """
    Send stats of the last question. (Each number of vote for each answer)
    """
    emit(
        SOCKET_EVENT_STATS_ANSWERS_QUESTION,
        {
            "A": len(list(
                filter(lambda contestant: contestant.selected_answer == SELECTED_ANSWER_A,
                       quiz_store.listContestants)
            )),
            "B": len(list(
                filter(lambda contestant: contestant.selected_answer == SELECTED_ANSWER_B,
                       quiz_store.listContestants)
            )),
            "C": len(list(
                filter(lambda contestant: contestant.selected_answer == SELECTED_ANSWER_C,
                       quiz_store.listContestants)
            )),
            "D": len(list(
                filter(lambda contestant: contestant.selected_answer == SELECTED_ANSWER_D,
                       quiz_store.listContestants)
            ))
        }
    )


def sendEventStopQuiz() -> None:
    """
    Send an event to stop the quiz.
    """
    emit(
        SOCKET_EVENT_QUIZ_STOP
    )


def sendQuizRanking(ranking: Ranking) -> None:
    """
    Send an event with the ranking.
    """
    emit(
        SOCKET_EVENT_RANKING,
        {
            "first": ranking.first,
            "second": ranking.second,
            "third": ranking.third,
            "fourth": ranking.fourth,
            "fifth": ranking.fifth,
            "sixth": ranking.sixth,
            "seventh": ranking.seventh,
            "eighth": ranking.eighth,
            "ninth": ranking.ninth,
            "tenth": ranking.tenth
        }
    )


def sendEventStopQuizNoWinner() -> None:
    """
    Send an event to stop the quiz because everyone is eliminated.
    """
    emit(
        SOCKET_EVENT_QUIZ_STOP_NO_WINNER
    )


def sendEventStopQuizWinner() -> None:
    """
    Send an event to stop the quiz because only one player is alive.
    """
    emit(
        SOCKET_EVENT_QUIZ_STOP_WINNER,
        {
            "winner": quiz_store.listContestants[0].contestant_name
        }
    )


def sendEventStopQuizNoMoreQuestions() -> None:
    """
    Send an event to stop the quiz because there are no other questions available.
    """
    emit(
        SOCKET_EVENT_QUIZ_STOP_NO_QUESTIONS
    )


def sendEventContinueQuiz() -> None:
    """
    Send an event to continue the quiz when all the answers have been processed.
    """
    emit(
        SOCKET_EVENT_QUIZ_CONTINUE
    )
