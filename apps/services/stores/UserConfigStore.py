from apps.services.utils.JsonUtils import readJson
from apps.constants.ResourcesConstants import USER_CONFIGS_FILE_PATH


class UserConfigStore:
    """
    UserConfigStore
    ---------------

    Contains all user configurations parameters.
    Load default configs from JSON. They can be updated.
    """

    def __init__(self):
        self.user_configs = readJson(USER_CONFIGS_FILE_PATH)

    def getClientId(self):
        """
        Returns the ClientId stored.
        :return: String
        """
        return self.user_configs['clientId']

    def getClientSecret(self):
        """
        Returns the ClientSecret stored.
        :return: String
        """
        return self.user_configs['clientSecret']

    def getBroadcasterId(self):
        """
        Returns the BroadcasterId of the user.
        :return: String
        """
        return self.user_configs['broadcasterId']

    def setBroadcasterId(self, new_broadcaster_id):
        """
        Declare the new broadcaster id.
        :param new_broadcaster_id: String
        """
        self.user_configs['broadcasterId'] = new_broadcaster_id

    def getRewardCost(self, reward_name):
        """
        Returns the cost of a reward.
        :param reward_name: String - Name of the reward to retrieve the cost.
        :return: Number
        """
        return self.user_configs['rewardsCosts'][reward_name]


user_config_store = UserConfigStore()
