from apps.services.stores.UserConfigStore import UserConfigStore
from tests.TestsConstants import TEST_USER_CONFIGS
from apps.constants.RewardsConstants import PLAYER_REGISTRATION_REWARD_PARAM_NAME
import pytest


class TestUserConfigStore:

    def test_init_values(self, mocker):
        mocker.patch(
            'apps.services.stores.UserConfigStore.readJson',
            return_value=TEST_USER_CONFIGS
        )

        user_config_store = UserConfigStore()

        assert user_config_store.getClientId() == "test_client_id"
        assert user_config_store.getClientSecret() == "test_client_secret"
        assert user_config_store.getRewardCost(PLAYER_REGISTRATION_REWARD_PARAM_NAME) == 5000
        with pytest.raises(KeyError):
            user_config_store.getBroadcasterId()
