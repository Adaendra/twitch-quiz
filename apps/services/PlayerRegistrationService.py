from apps.services.TwitchRedemptionService import getUnfulfilledRewardRedemptions, updateRewardRedemptionStatus
from apps.services.stores.RewardIdStore import reward_id_store
from apps.services.stores.QuizStore import quiz_store
from apps.models.QuizContestant import QuizContestant
from apps.services.stores.UserConfigStore import user_config_store
from apps.constants.RewardsConstants import REGISTRATION_REWARD_STATUS_FULFILLED, REGISTRATION_REWARD_STATUS_CANCELLED
from apps import emit
from apps.constants.SocketMessageTypeConstants import SOCKET_EVENT_STATS_CONSTESTANTS_CHECK_IN
import time
import sys
sys.setrecursionlimit(150000)

"""
PlayerRegistrationService
-------------------------

Contains all methods to manage Player registration.
"""


def registerPlayersFromRegistrationReward(is_check_in_open) -> None:
    """
    If the Check-in is open, check is there new contestants for the quiz from the registration reward.
    If they are not already registered, they will be added to the list.
    :param is_check_in_open: Boolean - True if open, False otherwise
    """

    # If the Check-In is open, check the new contestants.
    if is_check_in_open:
        redemption_list_to_treat = getUnfulfilledRewardRedemptions(reward_id_store.getRegistrationRewardId())

        for redemption in redemption_list_to_treat:
            player_name = redemption['broadcaster_name']

            # If user is not already registered, add the user the list and fulfill the redemption.
            if not any(filter(lambda contestant: contestant.contestant_name == player_name, quiz_store.listContestants)):
                quiz_store.listContestants.insert(
                    0,
                    QuizContestant(player_name, user_config_store.user_configs['quiz']['number_of_lives_per_contestant'])
                )
                updateRewardRedemptionStatus(
                    reward_id_store.getRegistrationRewardId(),
                    redemption['id'],
                    REGISTRATION_REWARD_STATUS_FULFILLED
                )

            else:
                # Already registered, cancel the redemption
                updateRewardRedemptionStatus(
                    reward_id_store.getRegistrationRewardId(),
                    redemption['id'],
                    REGISTRATION_REWARD_STATUS_CANCELLED
                )

        sendContestantCheckInStatistics()

        # Wait a little bit
        time.sleep(0.5)

        # Continue to register player
        registerPlayersFromRegistrationReward(quiz_store.isPlayerCheckInOpen)


def sendContestantCheckInStatistics() -> None:
    """
    Send contestants check-in statistics to front-end clients.
    """
    emit(SOCKET_EVENT_STATS_CONSTESTANTS_CHECK_IN, {
        "number_contestants": len(quiz_store.listContestants)
    })
