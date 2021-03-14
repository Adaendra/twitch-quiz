from apps.services.stores.UserConfigStore import user_config_store
from apps.constants.RewardsConstants import PLAYER_REGISTRATION_REWARD_PARAM_NAME


class ConfigController:
    """
    ConfigController
    ----------------

    Contains all methods related to the configs.
    """

    def __init__(self):
        pass

    def isAllRequiredConfigDefined(self) -> None:
        """
        Returns true if all the required configs are defined. If at least one config is missing, returns false.
        :param self:
        :return: boolean
        """
        return user_config_store.getClientId() != "" \
               and user_config_store.getClientSecret() != "" \
               and user_config_store.getRewardCost(PLAYER_REGISTRATION_REWARD_PARAM_NAME) != 0


configController = ConfigController()
