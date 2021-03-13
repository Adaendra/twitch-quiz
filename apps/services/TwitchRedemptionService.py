from apps.services.utils.HttpUtils import doHttpPost, doHttpDelete, doHttpGet, doHttpPatch
from apps.services.stores.UserConfigStore import user_config_store
from apps.services.TwitchAuthService import generateRedemptionToken
from apps.constants.TwitchURLConstants import CUSTOM_REWARD_URL, CUSTOM_REWARD_REGISTRATION_URL

"""
TwitchRedemptionService
-----------------------

Contains all methods linked to channel points (Under the redemption scope in the Twitch API)
Documentation: https://dev.twitch.tv/docs/api/reference
"""


def createReward(title, cost) -> str:
    """
    Create a custom reward.
    Documentation: https://dev.twitch.tv/docs/api/reference#create-custom-rewards
    :param title: String - Title of the reward to create.
    :param cost: Number - Cost of the reward
    :exception: Throws an Exception if the request failed.
    :return: String - The id of the custom reward
    """

    response = doHttpPost(
        uri=CUSTOM_REWARD_URL,
        params={
            "broadcaster_id": user_config_store.getBroadcasterId()
        },
        headers={
            "Client-id": user_config_store.getClientId(),
            "Authorization": "Bearer " + generateRedemptionToken()
        },
        body={
            "title": title,
            "cost": cost
        }
    )

    if response.status_code == 200:
        return response.json()['data'][0]['id']
    else:
        # TODO : Mieux gérer les erreurs
        raise Exception('An error occurs during the reward creation. Status code : {0}'.format(response.status_code))


def deleteReward(reward_id) -> None:
    """
    Delete a custom reward.
    Documentation: https://dev.twitch.tv/docs/api/reference#delete-custom-reward
    :exception: Throws an error if the request fails.
    """
    response = doHttpDelete(
        url=CUSTOM_REWARD_URL,
        params={
            "broadcaster_id": user_config_store.getBroadcasterId(),
            "id": reward_id
        },
        headers={
            "Client-id": user_config_store.getClientId(),
            "Authorization": "Bearer " + generateRedemptionToken()
        }
    )

    if response.status_code != 204:
        # TODO : Mieux gérer les erreurs
        raise Exception('An error occurs during the reward deletion. Status code : {0}'.format(response.status_code))


def getUnfulfilledRewardRedemptions(reward_id) -> list: # TODO: Définir la liste d'objets qu'elle retourne
    """
    Retrieve a list a reward redemptions which are not fulfilled or cancelled.
    Documentation: https://dev.twitch.tv/docs/api/reference#get-custom-reward-redemption
    :param reward_id: String - The id of the reward which we want redemptions.
    :exception: Throws an error if the request fails.
    :return: List of Object - The list of reward redemptions to manage.
    """
    response = doHttpGet(
        url=CUSTOM_REWARD_REGISTRATION_URL,
        params={
            "broadcaster_id": user_config_store.getBroadcasterId(),
            "reward_id": reward_id,
            "status": "UNFULFILLED"
        },
        headers={
            "Client-id": user_config_store.getClientId(),
            "Authorization": "Bearer " + generateRedemptionToken()
        }
    )

    if response.status_code != 200:
        # TODO : Mieux gérer les erreurs
        raise Exception('An error occurs while retrieving the reward redemptions. Status code : {0}'
                        .format(response.status_code))
    else:
        return response.json()['data']


def updateRewardRedemptionStatus(reward_id, redemption_id, new_redemption_status) -> None:
    """
    Update the status of a reward redemption.
    Documentation: https://dev.twitch.tv/docs/api/reference#update-redemption-status
    :param reward_id: String - Id of the reward link to the redemption.
    :param redemption_id: String - Id of the redemption to update.
    :param new_redemption_status: String - The new status of the redemption.
    :exception: Throws an error if the request fails.
    """
    response = doHttpPatch(
        url=CUSTOM_REWARD_REGISTRATION_URL,
        params={
             "broadcaster_id": user_config_store.getBroadcasterId(),
             "reward_id": reward_id,
             "id": redemption_id
        },
        headers={
            "Client-id": user_config_store.getClientId(),
            "Authorization": "Bearer " + generateRedemptionToken(),
            "Content-Type": "application/json"
        },
        body={
            "status": new_redemption_status
        }
    )

    if response.status_code != 200:
        # TODO : Mieux gérer les erreurs
        raise Exception('An error occurs while updating the status of a reward redemption. Status code : {0}'
                        .format(response.status_code))

