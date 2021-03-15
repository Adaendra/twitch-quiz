from apps.services.AnswerProcessorService import processContestantAnswers
from apps.models.QuizContestant import QuizContestant
from apps.services.stores.QuizStore import quiz_store
from apps.models.Question import Question


class TestAnswerProcessorService:

    # ----- processContestantAnswers ----- #
    def test_processContestantAnswers_ok(self, mocker):
        contestant_with_answer_1 = QuizContestant("z", 1)
        contestant_with_answer_1.selected_answer = "A"

        contestant_with_answer_2 = QuizContestant("y", 2)
        contestant_with_answer_2.selected_answer = "B"

        quiz_store.listContestants = [
            QuizContestant("a", 3),
            contestant_with_answer_1,
            QuizContestant("b", 3),
            contestant_with_answer_2,
            QuizContestant("c", 3),
        ]

        quiz_store.currentQuestionIndex = 2
        quiz_store.listQuestions = [
            Question("A", ["A1", "A2", "A3", "A4"], "A", "a"),
            Question("B", ["B1", "B2", "B3", "B4"], "B", "b"),
            Question("C", ["C1", "C2", "C3", "C4"], "C", "c")
        ]

        processContestantAnswers()

        assert len(quiz_store.listContestants) == 4

        for contestant in quiz_store.listContestants:
            assert contestant.number_lives == 2
