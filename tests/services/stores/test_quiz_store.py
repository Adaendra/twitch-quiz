from apps.services.stores.QuizStore import quiz_store
from tests.TestsConstants import TEST_QUESTION_LIST


class TestQuizStore:

    def test_quiz_store_init(self):
        assert quiz_store.currentQuestionIndex == 0
        assert quiz_store.listQuestions == []
        assert quiz_store.isPlayerCheckInOpen == False
        assert quiz_store.isQuizOnGoing == False
        assert quiz_store.listContestants == []

    def test_reset_quiz(self, mocker):
        mocker.patch(
            'apps.services.stores.QuizStore.readJson',
            return_value=TEST_QUESTION_LIST
        )

        quiz_store.resetQuiz()

        assert quiz_store.currentQuestionIndex == 0
        assert len(quiz_store.listQuestions) == len(TEST_QUESTION_LIST)
        assert quiz_store.isPlayerCheckInOpen is True
        assert quiz_store.isQuizOnGoing is False
        assert quiz_store.listContestants == []
