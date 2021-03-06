from apps.services.TwitchRedemptionService import createReward, deleteReward
from apps.constants.RewardsConstants import PLAYER_REGISTRATION_REWARD_PARAM_NAME, PLAYER_REGISTRATION_REWARD_TITLE, \
    RESPONSE_A_REWARD_TITLE, RESPONSE_B_REWARD_TITLE, RESPONSE_C_REWARD_TITLE, RESPONSE_D_REWARD_TITLE
from apps.services.stores.UserConfigStore import user_config_store
from apps.services.stores.RewardIdStore import reward_id_store

"""
RewardService
-------------

Contains all methods related to Twitch Rewards.
"""


# ----- Quiz Registration ----- #
def createQuizRegistrationReward() -> None:
    """
    Create the registration reward to allow viewers to be a quiz contestant.
    """
    registration_reward_id = createReward(
        PLAYER_REGISTRATION_REWARD_TITLE,
        user_config_store.getRewardCost(PLAYER_REGISTRATION_REWARD_PARAM_NAME)
    )

    # Store the id of the newly created registration reward.
    reward_id_store.setRegistrationRewardId(registration_reward_id)


def deleteQuizRegistrationReward() -> None:
    """
    Delete the registration reward to allow viewers to be a quiz contestant.
    Then clear the value from the store.
    """
    deleteReward(reward_id_store.getRegistrationRewardId())

    reward_id_store.setRegistrationRewardId(None)


# ----- Quiz Answers ----- #
def createQuizAnswersReward() -> None:
    """
    Create the quiz answers rewards to allow player to answer.
    """
    # -- A
    response_a_reward_id = createReward(
        RESPONSE_A_REWARD_TITLE,
        0
    )

    reward_id_store.setResponseARewardId(response_a_reward_id)

    # -- B
    response_b_reward_id = createReward(
        RESPONSE_B_REWARD_TITLE,
        0
    )

    reward_id_store.setResponseBRewardId(response_b_reward_id)

    # -- C
    response_c_reward_id = createReward(
        RESPONSE_C_REWARD_TITLE,
        0
    )

    reward_id_store.setResponseCRewardId(response_c_reward_id)

    # -- D
    response_d_reward_id = createReward(
        RESPONSE_D_REWARD_TITLE,
        0
    )

    reward_id_store.setResponseDRewardId(response_d_reward_id)


def deleteQuizAnswersReward() -> None:
    """
    Delete all quiz answers rewards.
    """
    deleteReward(reward_id_store.getResponseARewardId())
    deleteReward(reward_id_store.getResponseBRewardId())
    deleteReward(reward_id_store.getResponseCRewardId())
    deleteReward(reward_id_store.getResponseDRewardId())


def clearAnswerRewardId() -> None:
    """
    Clear responses reward id from the store.
    """
    reward_id_store.setResponseARewardId(None)
    reward_id_store.setResponseBRewardId(None)
    reward_id_store.setResponseCRewardId(None)
    reward_id_store.setResponseDRewardId(None)

