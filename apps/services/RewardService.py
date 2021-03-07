from apps.services.TwitchRedemptionService import createReward, deleteReward
from apps.constants.RewardsConstants import PLAYER_REGISTRATION_REWARD_PARAM_NAME, PLAYER_REGISTRATION_REWARD_TITLE
from apps.services.stores.UserConfigStore import user_config_store
from apps.services.stores.RewardIdStore import reward_id_store

"""
RewardService
-------------

Contains all methods related to Twitch Rewards.
"""


def createQuizRegistrationReward():
    """
    Create the registration reward to allow viewers to be a quiz contestant.
    """
    registration_reward_id = createReward(
        PLAYER_REGISTRATION_REWARD_TITLE,
        user_config_store.getRewardCost(PLAYER_REGISTRATION_REWARD_PARAM_NAME)
    )

    # Store the id of the newly created registration reward.
    reward_id_store.setRegistrationRewardId(registration_reward_id)


def deleteQuizRegistrationReward():
    """
    Delete the registration reward to allow viewers to be a quiz contestant.
    Then clear the value from the store.
    """
    deleteReward(reward_id_store.getRegistrationRewardId())

    reward_id_store.setRegistrationRewardId(None)

