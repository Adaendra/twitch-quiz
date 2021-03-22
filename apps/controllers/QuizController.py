from apps.controllers.ConfigController import configController
from apps.services.ErrorService import raiseError
from apps.services.RewardService import createQuizRegistrationReward, deleteQuizRegistrationReward, \
    createQuizAnswersReward, deleteQuizAnswersReward, clearAnswerRewardId
from apps.services.stores.QuizStore import quiz_store
import logging
from apps.services.TwitchStreamService import retrieveBroadcastId
from apps.services.TwitchAuthService import generateRedemptionToken
from apps.services.stores.UserConfigStore import user_config_store
from apps.services.PlayerRegistrationService import registerPlayersFromRegistrationReward
from apps.services.PlayerAnswerManagementService import saveContestantsAnswer
from apps.services.FrontEndEventSenderService import sendNextQuestion, sendStatsAnswerQuestion, sendEventStopQuiz, \
    sendEventRevealAnswer, sendQuizRanking, sendEventStopQuizNoWinner, sendEventStopQuizWinner, \
    sendEventStopQuizNoMoreQuestions, sendEventContinueQuiz
from apps.services.AnswerProcessorService import processContestantAnswers
from apps.services.RankingService import calculateRankings
import time


class QuizController:
    """
    QuizController
    --------------

    Contains all methods related to the Quiz management.
    """
    logger = logging.getLogger('QuizController')

    def __init__(self):
        pass

    def init_quiz(self) -> None:
        """
        Initialize a quiz and open registrations.
        """
        # Block if account is not setup to connect to the twitch api
        if not configController.isAllRequiredConfigDefined():
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

                registerPlayersFromRegistrationReward(quiz_store.isPlayerCheckInOpen)
            except Exception as err:
                self.logger.error("{0}".format(err))
                raiseError("An error appears during the quiz initialization")

    def start_quiz(self) -> None:
        """
        Close registration and start a quiz.
        """
        # Close Player Registration
        deleteQuizRegistrationReward()

        # Start quiz
        quiz_store.isQuizOnGoing = True

        # Set the question index to 1
        quiz_store.currentQuestionIndex = 1

        # Create answers rewards to allow users to select their response.
        createQuizAnswersReward()

        # Send event to show the next question
        sendNextQuestion()

        # Start process to listen answers
        saveContestantsAnswer(quiz_store.isQuizOnGoing, quiz_store.isQuestionOnGoing)

    def stop_quiz(self) -> None:
        """
        Stop the quiz.
        """
        # Delete answers rewards
        deleteQuizAnswersReward()

        # Send event to close quiz
        sendEventStopQuiz()

        # Stop process to listen answers
        quiz_store.isQuestionOnGoing = False

        # Wait a little bit to manage all last redemptions received
        time.sleep(10)

        quiz_store.isQuizOnGoing = False

        # Clear answers rewards id
        clearAnswerRewardId()

    def reveal_answer(self) -> None:
        # Deny to save contestants answers
        quiz_store.isQuestionOnGoing = False

        # Send event to reveal the answer
        sendEventRevealAnswer()

        # Send statistics
        sendStatsAnswerQuestion()

        # Process the answers from players
        processContestantAnswers()

        # Calculate rankings
        ranking = calculateRankings()

        # Send ranking
        sendQuizRanking(ranking)

        # Send event to allow to go to the next question or not
        if len(quiz_store.listContestants) == 0:
            sendEventStopQuizNoWinner()
        elif len(quiz_store.listContestants) == 1:
            sendEventStopQuizWinner()
        elif quiz_store.currentQuestionIndex >= len(quiz_store.listQuestions):
            sendEventStopQuizNoMoreQuestions()
        else:
            sendEventContinueQuiz()

    def next_question(self) -> None:
        """
        Advance the quiz to the next question.
        """

        # Wait a little bit to reset the recursive count
        quiz_store.isQuizOnGoing = False
        time.sleep(1)

        # Update the index
        quiz_store.currentQuestionIndex = quiz_store.currentQuestionIndex + 1

        # Send event to show the next question
        sendNextQuestion()

        # Allow to save contestants answers
        quiz_store.isQuizOnGoing = True
        quiz_store.isQuestionOnGoing = True

        # Start process to listen answers
        saveContestantsAnswer(quiz_store.isQuizOnGoing, quiz_store.isQuestionOnGoing)


quizController = QuizController()
