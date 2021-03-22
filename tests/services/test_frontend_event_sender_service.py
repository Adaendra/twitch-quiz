from unittest.mock import call

from apps.constants.SocketMessageTypeConstants import SOCKET_EVENT_QUIZ_NEXT_QUESTION, \
    SOCKET_EVENT_STATS_ANSWERS_ONGOING, SOCKET_EVENT_STATS_ANSWERS_QUESTION, SOCKET_EVENT_QUIZ_STOP, \
    SOCKET_EVENT_REVEAL_ANSWER, SOCKET_EVENT_RANKING, SOCKET_EVENT_QUIZ_STOP_NO_WINNER, SOCKET_EVENT_QUIZ_STOP_WINNER, \
    SOCKET_EVENT_QUIZ_STOP_NO_QUESTIONS, SOCKET_EVENT_QUIZ_CONTINUE
from apps.services.stores.QuizStore import quiz_store
from apps.models.Question import Question
from apps.models.QuizContestant import QuizContestant
from apps.services.FrontEndEventSenderService import sendNextQuestion, sendStatsAnswerQuestion, \
    sendStatsAnswersOngoing, sendEventStopQuiz, sendEventRevealAnswer, sendQuizRanking, sendEventStopQuizNoWinner, \
    sendEventContinueQuiz, sendEventStopQuizNoMoreQuestions, sendEventStopQuizWinner
from apps.models.Ranking import Ranking


class TestFrontEndEventSenderService:

    # ----- sendNextQuestion ----- #
    def test_sendNextQuestion_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.FrontEndEventSenderService.emit'
        )

        quiz_store.currentQuestionIndex = 1
        quiz_store.listQuestions = [
            Question("A", ["A1", "A2", "A3", "A4"], "A1", "a"),
            Question("B", ["B1", "B2", "B3", "B4"], "B1", "b"),
            Question("C", ["C1", "C2", "C3", "C4"], "C1", "c")
        ]

        sendNextQuestion()

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_QUIZ_NEXT_QUESTION,
                                           {
                                               "index": 1,
                                               "question": {
                                                   "question": "A",
                                                   "proposals": ["A1", "A2", "A3", "A4"],
                                                   "answer": "A1",
                                                   "theme": "a"
                                               }
                                           })

    # ----- sendStatsAnswersOngoing ----- #
    def test_sendStatsAnswersOngoing_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.FrontEndEventSenderService.emit'
        )
        contestant_with_answer_1 = QuizContestant("z", 3)
        contestant_with_answer_1.selected_answer = "A"

        contestant_with_answer_2 = QuizContestant("y", 3)
        contestant_with_answer_2.selected_answer = "A"

        quiz_store.listContestants = [
            QuizContestant("a", 1),
            contestant_with_answer_1,
            QuizContestant("b", 2),
            contestant_with_answer_2,
            QuizContestant("c", 3),
        ]

        sendStatsAnswersOngoing()

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_STATS_ANSWERS_ONGOING,
                                           {
                                               "numberAnswers": 2
                                           })

    # ----- sendEventRevealAnswer ----- #
    def test_sendEventRevealAnswer_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.FrontEndEventSenderService.emit'
        )

        quiz_store.currentQuestionIndex = 0
        quiz_store.listQuestions = [
            Question("A", ["A1", "A2", "A3", "A4"], "test", "a")
        ]

        sendEventRevealAnswer()

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_REVEAL_ANSWER, {"answer": "test"})

    # ----- sendStatsAnswerQuestion ----- #
    def test_sendStatsAnswerQuestion_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.FrontEndEventSenderService.emit'
        )
        contestant_with_answer_1 = QuizContestant("z", 3)
        contestant_with_answer_1.selected_answer = "A"

        contestant_with_answer_2 = QuizContestant("y", 3)
        contestant_with_answer_2.selected_answer = "A"

        contestant_with_answer_3 = QuizContestant("y", 3)
        contestant_with_answer_3.selected_answer = "B"

        contestant_with_answer_4 = QuizContestant("y", 3)
        contestant_with_answer_4.selected_answer = "B"

        contestant_with_answer_5 = QuizContestant("y", 3)
        contestant_with_answer_5.selected_answer = "B"

        quiz_store.listContestants = [
            QuizContestant("a", 1),
            contestant_with_answer_1,
            QuizContestant("b", 2),
            contestant_with_answer_2,
            contestant_with_answer_3,
            contestant_with_answer_4,
            contestant_with_answer_5,
            QuizContestant("c", 3),
        ]

        sendStatsAnswerQuestion()

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_STATS_ANSWERS_QUESTION, {"A": 2, "B": 3, "C": 0, "D": 0})

    # ----- sendEventStopQuiz ----- #
    def test_sendEventStopQuiz_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.FrontEndEventSenderService.emit'
        )

        sendEventStopQuiz()

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_QUIZ_STOP)

    # ----- sendQuizRanking ----- #
    def test_sendQuizRanking_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.FrontEndEventSenderService.emit'
        )

        ranking = Ranking()
        ranking.first = "first"
        ranking.second = "second"
        ranking.third = "third"

        sendQuizRanking(ranking)

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_RANKING, {
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
        })

    # ----- sendEventStopQuizNoWinner ----- #
    def test_sendEventStopQuizNoWinner_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.FrontEndEventSenderService.emit'
        )

        sendEventStopQuizNoWinner()

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_QUIZ_STOP_NO_WINNER)

    # ----- sendEventStopQuizWinner ----- #
    def test_sendEventStopQuizWinner_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.FrontEndEventSenderService.emit'
        )

        quiz_store.listContestants = [
            QuizContestant("zizou", 2)
        ]

        sendEventStopQuizWinner()

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_QUIZ_STOP_WINNER, {"winner": "zizou"})

    # ----- sendEventStopQuizNoMoreQuestions ----- #
    def test_sendEventStopQuizNoMoreQuestions_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.FrontEndEventSenderService.emit'
        )

        sendEventStopQuizNoMoreQuestions()

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_QUIZ_STOP_NO_QUESTIONS)

    # ----- sendEventContinueQuiz ----- #
    def test_sendEventContinueQuiz_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.FrontEndEventSenderService.emit'
        )

        sendEventContinueQuiz()

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_QUIZ_CONTINUE)


