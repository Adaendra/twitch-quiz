import pytest

from apps.services.TwitchRedemptionService import updateRewardRedemptionStatus, getUnfulfilledRewardRedemptions, createReward, deleteReward
from apps.services.stores.UserConfigStore import user_config_store


class TestTwitchRedemptionService:

    # ----- createReward ----- #
    def test_createReward_ok(self, mocker):
        mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken'
        )
        mockResponse = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpPost'
        )
        mockResponse.return_value.status_code = 200
        mockResponse.return_value.json.return_value = {'data': [{'id': 'random_id_test'}]}

        user_config_store.setBroadcasterId("id")

        assert createReward("title", 5000) == 'random_id_test'

    def test_createReward_nok(self, mocker):
        mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken'
        )
        mockResponse = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpPost'
        )
        mockResponse.return_value.status_code = 400
        mockResponse.return_value.json.return_value = {'data': [{'id': 'random_id_test'}]}

        user_config_store.setBroadcasterId("id")

        with pytest.raises(Exception) as err:
            createReward("title", 5000)
            assert err == 'An error occurs during the reward creation. Status code : 400'

    # ----- deleteReward ----- #
    def test_deleteReward_ok(self, mocker):
        mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken'
        )
        mockResponse = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpDelete'
        )
        mockResponse.return_value.status_code = 204

        user_config_store.setBroadcasterId("id")

        deleteReward("reward_id")

    def test_deleteReward_nok(self, mocker):
        mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken'
        )
        mockResponse = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpDelete'
        )
        mockResponse.return_value.status_code = 400

        user_config_store.setBroadcasterId("id")

        with pytest.raises(Exception) as err:
            deleteReward("reward_id")
            assert err == 'An error occurs during the reward deletion. Status code : 400'


