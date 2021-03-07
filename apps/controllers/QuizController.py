from apps.controllers.ConfigController import configController
from apps.services.ErrorService import raiseError
from apps.services.RewardService import createQuizRegistrationReward, deleteQuizRegistrationReward
from apps.services.stores.QuizStore import quiz_store
import logging
from apps.services.TwitchStreamService import retrieveBroadcastId
from apps.services.TwitchAuthService import generateRedemptionToken
from apps.services.stores.UserConfigStore import user_config_store
from apps.services.PlayerRegistrationService import registerPlayersFromRegistrationReward


class QuizController:
    """
    QuizController
    --------------

    Contains all methods related to the Quiz management.
    """
    logger = logging.getLogger('QuizController')

    def __init__(self):
        pass

    def init_quiz(self):
        """
        Initialize a quiz and open registrations.
        :return:
        """
        # Block if account is not setup to connect to the twitch api
        if configController.isAllRequiredConfigDefined():
            raiseError("At least one mandatory configuration is missing.")

        else:
            # Retrieve the broadcaster id
            user_config_store.setBroadcasterId(retrieveBroadcastId(
                generateRedemptionToken(),
                user_config_store.getClientId()
            ))

            quiz_store.resetQuiz()

            # Open player registration
            try:
                createQuizRegistrationReward()

            except Exception as err:
                self.logger.error("{0}".format(err))
                raiseError("An error appears during the quiz initialization")

            registerPlayersFromRegistrationReward(quiz_store.isPlayerCheckInOpen)

    def start_quiz(self):
        # Close Player Registration
        deleteQuizRegistrationReward()
        # TODO : Start quiz
        # TODO : Set the question index to 1
        # TODO : Start process to listen answers
        pass

    def stop_quiz(self): # TODO : To comment - Work in Progress
        # TODO : Stop quiz
        # TODO : Delete rewards
        pass

    def reveal_answer(self):
        # TODO : Stop process to listen answers
        # TODO : Send event to reveal the answer
        # TODO : Process the answers from players
        # TODO : Send statistics
        # TODO : Send event to allow to go to the next question
        pass

    def next_question(self):
        # TODO : Update the index
        # TODO : Send the new question
        # TODO : Start process to listen answers
        pass


quizController = QuizController()
