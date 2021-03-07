from apps.services.stores.QuizStore import QuizStore
from tests.TestsConstants import TEST_QUESTION_LIST


class TestQuizStore:

    # ----- QuizStore ----- #
    def test_QuizStore_init(self):
        quiz_store = QuizStore()

        assert quiz_store.currentQuestionIndex == 0
        assert quiz_store.listQuestions == []
        assert quiz_store.isPlayerCheckInOpen is False
        assert quiz_store.isQuizOnGoing is False
        assert quiz_store.listContestants == []

    # ----- resetQuiz ----- #
    def test_resetQuiz_ok(self, mocker):
        mocker.patch(
            'apps.services.stores.QuizStore.readJson',
            return_value=TEST_QUESTION_LIST
        )

        quiz_store = QuizStore()
        quiz_store.resetQuiz()

        assert quiz_store.currentQuestionIndex == 0
        assert len(quiz_store.listQuestions) == len(TEST_QUESTION_LIST)
        assert quiz_store.isPlayerCheckInOpen is True
        assert quiz_store.isQuizOnGoing is False
        assert quiz_store.listContestants == []
