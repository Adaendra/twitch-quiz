from apps.services.utils.JsonUtils import readJson
from apps.constants.ResourcesConstants import QUESTION_LIST_FILE_PATH
from apps.models.QuizContestant import QuizContestant
from apps.models.Question import Question
import random


class QuizStore:
    """
    QuizStore
    ---------

    Store all data related to a quiz.
    """

    currentQuestionIndex: int = 0
    listQuestions: list[Question] = []
    isPlayerCheckInOpen: bool = False
    isQuizOnGoing: bool = False
    isQuestionOnGoing: bool = False
    listContestants: list[QuizContestant] = []

    def __init__(self):
        self.currentQuestionIndex = 0
        self.listQuestions = []
        self.isPlayerCheckInOpen = False
        self.isQuizOnGoing = False
        self.isQuestionOnGoing = False
        self.listContestants: list[QuizContestant] = []

    def resetQuiz(self) -> None:
        """
        Reset quiz store values.
        """
        self.currentQuestionIndex = 0
        self.listQuestions = readJson(QUESTION_LIST_FILE_PATH)
        self.isPlayerCheckInOpen = True
        self.isQuizOnGoing = False
        self.isQuestionOnGoing = False
        self.listContestants = []

        random.shuffle(self.listQuestions)


quiz_store = QuizStore()
