from apps.services.TwitchRedemptionService import getUnfulfilledRewardRedemptions, updateRewardRedemptionStatus
from apps.services.stores.RewardIdStore import reward_id_store
from apps.services.stores.QuizStore import quiz_store
from apps.constants.RewardsConstants import REGISTRATION_REWARD_STATUS_CANCELLED, REGISTRATION_REWARD_STATUS_FULFILLED
from apps.constants.QuizConstants import SELECTED_ANSWER_A, SELECTED_ANSWER_B, SELECTED_ANSWER_C, SELECTED_ANSWER_D
from apps.models.QuizContestant import QuizContestant
import time
import sys

sys.setrecursionlimit(150000)

"""
PlayerAnswerManagementService
-----------------------------

Contains methods to manage player answers.
"""


def saveContestantsAnswer(is_quiz_on_going, is_question_on_going) -> None:
    """
    If the quiz is ongoing, listen players answers.
    If a question is going, save the first answer for each player. Otherwise, cancel redemption.
    :param is_quiz_on_going: boolean - True if the quiz is ongoing.
    :param is_question_on_going: boolean - True if the quiz is ongoing
    """

    if is_quiz_on_going:
        answers_received = processPlayersAnswer(reward_id_store.getResponseARewardId(), is_question_on_going,
                                                SELECTED_ANSWER_A) + \
                           processPlayersAnswer(reward_id_store.getResponseBRewardId(), is_question_on_going,
                                                SELECTED_ANSWER_B) + \
                           processPlayersAnswer(reward_id_store.getResponseCRewardId(), is_question_on_going,
                                                SELECTED_ANSWER_C) + \
                           processPlayersAnswer(reward_id_store.getResponseDRewardId(), is_question_on_going,
                                                SELECTED_ANSWER_D)

        # Wait a little bit
        if answers_received < 25:
            time.sleep(0.5)
        else:
            time.sleep(0.2)

        saveContestantsAnswer(quiz_store.isQuizOnGoing, quiz_store.isQuestionOnGoing)


def processPlayersAnswer(answer_reward_id, is_question_on_going, selected_answer) -> int:
    """
    Retrieve redemptions of a specific answer and store information/
    :param answer_reward_id: str - Id of the answer reward to retrieve redemptions.
    :param is_question_on_going: boolean - True if a question is ongoing, otherwise false.
    :param selected_answer: Label of the answer associated to the answer reward id.
    :return: int - The number of redemptions processed.
    """
    redemption_list_to_treat = getUnfulfilledRewardRedemptions(answer_reward_id)

    for redemption in redemption_list_to_treat:
        # If question is not ongoing, cancel
        if not is_question_on_going:
            updateRewardRedemptionStatus(answer_reward_id, redemption.id, REGISTRATION_REWARD_STATUS_CANCELLED)

        else:
            list_filtered = filter(lambda contestant: contestant.contestant_name == redemption.user_name,
                                   quiz_store.listContestants)

            player: QuizContestant = next(iter(list_filtered or []), None)

            if player is None:
                updateRewardRedemptionStatus(answer_reward_id, redemption.id, REGISTRATION_REWARD_STATUS_CANCELLED)

            # Check is player already have an answer, if not save it.
            elif player.selected_answer is None:
                player.selected_answer = selected_answer
                updateRewardRedemptionStatus(answer_reward_id, redemption.id, REGISTRATION_REWARD_STATUS_FULFILLED)
            else:
                updateRewardRedemptionStatus(answer_reward_id, redemption.id, REGISTRATION_REWARD_STATUS_CANCELLED)

    return len(redemption_list_to_treat)
