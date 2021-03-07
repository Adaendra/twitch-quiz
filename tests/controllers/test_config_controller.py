from subprocess import call
from unittest.mock import call
from apps.constants.RewardsConstants import PLAYER_REGISTRATION_REWARD_PARAM_NAME

from apps.controllers.ConfigController import configController


class TestConfigController:

    # ----- isAllRequiredConfigDefined ----- #
    def test_isAllRequiredConfigDefined_ok(self, mocker):
        mock_client_id = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_client_secret = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientSecret',
            return_value="client_secret"
        )
        mock_reward_cost = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getRewardCost',
            return_value=5000
        )

        assert configController.isAllRequiredConfigDefined() is True

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_client_secret.call_count == 1
        assert mock_client_secret.call_args == call()

        assert mock_reward_cost.call_count == 1
        assert mock_reward_cost.call_args == call(PLAYER_REGISTRATION_REWARD_PARAM_NAME)

    def test_isAllRequiredConfigDefined_nok_clientId(self, mocker):
        mock_client_id = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientId',
            return_value=""
        )
        mock_client_secret = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientSecret',
            return_value="client_secret"
        )
        mock_reward_cost = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getRewardCost',
            return_value=5000
        )

        assert configController.isAllRequiredConfigDefined() is False

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_client_secret.call_count == 0

        assert mock_reward_cost.call_count == 0

    def test_isAllRequiredConfigDefined_nok_clientSecret(self, mocker):
        mock_client_id = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_client_secret = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientSecret',
            return_value=""
        )
        mock_reward_cost = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getRewardCost',
            return_value=5000
        )

        assert configController.isAllRequiredConfigDefined() is False

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_client_secret.call_count == 1
        assert mock_client_secret.call_args == call()

        assert mock_reward_cost.call_count == 0

    def test_isAllRequiredConfigDefined_nok_rewardCost(self, mocker):
        mock_client_id = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_client_secret = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientSecret',
            return_value="client_secret"
        )
        mock_reward_cost = mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getRewardCost',
            return_value=0
        )

        assert configController.isAllRequiredConfigDefined() is False

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_client_secret.call_count == 1
        assert mock_client_secret.call_args == call()

        assert mock_reward_cost.call_count == 1
        assert mock_reward_cost.call_args == call(PLAYER_REGISTRATION_REWARD_PARAM_NAME)
