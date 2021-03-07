from apps.services.utils.JsonUtils import readJson
from apps.constants.ResourcesConstants import QUESTION_LIST_FILE_PATH
import random


class QuizStore:
    """
    QuizStore
    ---------

    Store all data related to a quiz.
    """

    def __init__(self):
        self.currentQuestionIndex = 0
        self.listQuestions = []
        self.isPlayerCheckInOpen = False
        self.isQuizOnGoing = False
        self.listContestants = []

    def resetQuiz(self):
        self.currentQuestionIndex = 0
        self.listQuestions = readJson(QUESTION_LIST_FILE_PATH)
        self.isPlayerCheckInOpen = True
        self.listContestants = []

        random.shuffle(self.listQuestions)

        # TODO: To remove
        print("-- QUESTION LIST --")
        for question in self.listQuestions:
            print(question)


quiz_store = QuizStore()
