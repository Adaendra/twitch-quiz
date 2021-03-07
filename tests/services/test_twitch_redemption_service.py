from unittest.mock import call

import pytest

from apps.services.TwitchRedemptionService import updateRewardRedemptionStatus, getUnfulfilledRewardRedemptions, createReward, deleteReward
from apps.services.stores.UserConfigStore import user_config_store
from apps.constants.TwitchURLConstants import CUSTOM_REWARD_URL, CUSTOM_REWARD_REGISTRATION_URL


class TestTwitchRedemptionService:

    # ----- createReward ----- #
    def test_createReward_ok(self, mocker):
        mock_token = mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken',
            return_value="bearer_token"
        )
        mock_broadcaster_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getBroadcasterId',
            return_value="broadcaster_id"
        )
        mock_client_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_http_post = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpPost'
        )
        mock_http_post.return_value.status_code = 200
        mock_http_post.return_value.json.return_value = {'data': [{'id': 'random_id_test'}]}

        user_config_store.setBroadcasterId("id")

        assert createReward("title", 5000) == 'random_id_test'

        assert mock_token.call_count == 1
        assert mock_token.call_args == call()

        assert mock_broadcaster_id.call_count == 1
        assert mock_broadcaster_id.call_args == call()

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_http_post.call_count == 1
        assert mock_http_post.call_args == call(
            uri=CUSTOM_REWARD_URL,
            params={
                "broadcaster_id": "broadcaster_id"
            },
            headers={
                "Client-id": "client_id",
                "Authorization": "Bearer bearer_token"
            },
            body={
                "title": "title",
                "cost": 5000
        })

    def test_createReward_nok(self, mocker):
        mock_token = mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken',
            return_value="bearer_token"
        )
        mock_broadcaster_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getBroadcasterId',
            return_value="broadcaster_id"
        )
        mock_client_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_http_post = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpPost'
        )
        mock_http_post.return_value.status_code = 400
        mock_http_post.return_value.json.return_value = {'data': [{'id': 'random_id_test'}]}

        user_config_store.setBroadcasterId("id")

        with pytest.raises(Exception) as err:
            createReward("title", 5000)
            assert err == 'An error occurs during the reward creation. Status code : 400'

        assert mock_token.call_count == 1
        assert mock_token.call_args == call()

        assert mock_broadcaster_id.call_count == 1
        assert mock_broadcaster_id.call_args == call()

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_http_post.call_count == 1
        assert mock_http_post.call_args == call(
            uri=CUSTOM_REWARD_URL,
            params={
                "broadcaster_id": "broadcaster_id"
            },
            headers={
                "Client-id": "client_id",
                "Authorization": "Bearer bearer_token"
            },
            body={
                "title": "title",
                "cost": 5000
        })

    # ----- deleteReward ----- #
    def test_deleteReward_ok(self, mocker):
        mock_token = mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken',
            return_value="bearer_token"
        )
        mock_broadcaster_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getBroadcasterId',
            return_value="broadcaster_id"
        )
        mock_client_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_http_delete = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpDelete'
        )
        mock_http_delete.return_value.status_code = 204

        user_config_store.setBroadcasterId("id")

        deleteReward("reward_id")

        assert mock_token.call_count == 1
        assert mock_token.call_args == call()

        assert mock_broadcaster_id.call_count == 1
        assert mock_broadcaster_id.call_args == call()

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_http_delete.call_count == 1
        assert mock_http_delete.call_args == call(
            url=CUSTOM_REWARD_URL,
            params={
                "broadcaster_id": "broadcaster_id",
                "id": "reward_id"
            },
            headers={
                "Client-id": "client_id",
                "Authorization": "Bearer bearer_token"
            })

    def test_deleteReward_nok(self, mocker):
        mock_token = mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken',
            return_value="bearer_token"
        )
        mock_broadcaster_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getBroadcasterId',
            return_value="broadcaster_id"
        )
        mock_client_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_http_delete = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpDelete'
        )
        mock_http_delete.return_value.status_code = 400

        user_config_store.setBroadcasterId("id")

        with pytest.raises(Exception) as err:
            deleteReward("reward_id")
            assert err == 'An error occurs during the reward deletion. Status code : 400'

        assert mock_token.call_count == 1
        assert mock_token.call_args == call()

        assert mock_broadcaster_id.call_count == 1
        assert mock_broadcaster_id.call_args == call()

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_http_delete.call_count == 1
        assert mock_http_delete.call_args == call(
            url=CUSTOM_REWARD_URL,
            params={
                "broadcaster_id": "broadcaster_id",
                "id": "reward_id"
            },
            headers={
                "Client-id": "client_id",
                "Authorization": "Bearer bearer_token"
            })

    # ----- getUnfulfilledRewardRedemptions ----- #
    def test_getUnfulfilledRewardRedemptions_ok(self, mocker):
        mock_token = mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken',
            return_value="bearer_token"
        )
        mock_broadcaster_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getBroadcasterId',
            return_value="broadcaster_id"
        )
        mock_client_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_http_get = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpGet'
        )
        mock_http_get.return_value.status_code = 200
        mock_http_get.return_value.json.return_value = {'data': [{'id': 'random_id_test'}]}

        user_config_store.setBroadcasterId("id")

        assert getUnfulfilledRewardRedemptions("reward_id") == [{'id': 'random_id_test'}]

        assert mock_token.call_count == 1
        assert mock_token.call_args == call()

        assert mock_broadcaster_id.call_count == 1
        assert mock_broadcaster_id.call_args == call()

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_http_get.call_count == 1
        assert mock_http_get.call_args == call(
            url=CUSTOM_REWARD_REGISTRATION_URL,
            params={
                "broadcaster_id": "broadcaster_id",
                "reward_id": "reward_id",
                "status": "UNFULFILLED"
            },
            headers={
                "Client-id": "client_id",
                "Authorization": "Bearer bearer_token"
            })

    def test_getUnfulfilledRewardRedemptions_nok(self, mocker):
        mock_token = mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken',
            return_value="bearer_token"
        )
        mock_broadcaster_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getBroadcasterId',
            return_value="broadcaster_id"
        )
        mock_client_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_http_get = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpGet'
        )
        mock_http_get.return_value.status_code = 400
        mock_http_get.return_value.json.return_value = {'data': [{'id': 'random_id_test'}]}

        user_config_store.setBroadcasterId("id")

        with pytest.raises(Exception) as err:
            getUnfulfilledRewardRedemptions("reward_id")
            assert err == 'An error occurs while retrieving the reward redemptions. Status code : 400'

        assert mock_token.call_count == 1
        assert mock_token.call_args == call()

        assert mock_broadcaster_id.call_count == 1
        assert mock_broadcaster_id.call_args == call()

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_http_get.call_count == 1
        assert mock_http_get.call_args == call(
            url=CUSTOM_REWARD_REGISTRATION_URL,
            params={
                "broadcaster_id": "broadcaster_id",
                "reward_id": "reward_id",
                "status": "UNFULFILLED"
            },
            headers={
                "Client-id": "client_id",
                "Authorization": "Bearer bearer_token"
            })

    # ----- updateRewardRedemptionStatus ----- #
    def test_updateRewardRedemptionStatus_ok(self, mocker):
        mock_token = mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken',
            return_value="bearer_token"
        )
        mock_broadcaster_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getBroadcasterId',
            return_value="broadcaster_id"
        )
        mock_client_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_http_patch = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpPatch'
        )
        mock_http_patch.return_value.status_code = 200

        user_config_store.setBroadcasterId("id")

        updateRewardRedemptionStatus("reward_id", "redemption_id", "CANCELLED")

        assert mock_token.call_count == 1
        assert mock_token.call_args == call()

        assert mock_broadcaster_id.call_count == 1
        assert mock_broadcaster_id.call_args == call()

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_http_patch.call_count == 1
        assert mock_http_patch.call_args == call(
            url=CUSTOM_REWARD_REGISTRATION_URL,
            params={
                "broadcaster_id": "broadcaster_id",
                "reward_id": "reward_id",
                "id": "redemption_id"
            },
            headers={
                "Client-id": "client_id",
                "Authorization": "Bearer bearer_token",
                "Content-Type": "application/json"
            },
            body={
                "status": "CANCELLED"
            })

    def test_updateRewardRedemptionStatus_nok(self, mocker):
        mock_token = mocker.patch(
            'apps.services.TwitchRedemptionService.generateRedemptionToken',
            return_value="bearer_token"
        )
        mock_broadcaster_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getBroadcasterId',
            return_value="broadcaster_id"
        )
        mock_client_id = mocker.patch(
            'apps.services.TwitchRedemptionService.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_http_patch = mocker.patch(
            'apps.services.TwitchRedemptionService.doHttpPatch'
        )
        mock_http_patch.return_value.status_code = 400

        user_config_store.setBroadcasterId("id")

        with pytest.raises(Exception) as err:
            updateRewardRedemptionStatus("reward_id", "redemption_id", "CANCELLED")
            assert err == 'An error occurs while updating the status of a reward redemption. Status code : 400'

        assert mock_token.call_count == 1
        assert mock_token.call_args == call()

        assert mock_broadcaster_id.call_count == 1
        assert mock_broadcaster_id.call_args == call()

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_http_patch.call_count == 1
        assert mock_http_patch.call_args == call(
            url=CUSTOM_REWARD_REGISTRATION_URL,
            params={
                "broadcaster_id": "broadcaster_id",
                "reward_id": "reward_id",
                "id": "redemption_id"
            },
            headers={
                "Client-id": "client_id",
                "Authorization": "Bearer bearer_token",
                "Content-Type": "application/json"
            },
            body={
                "status": "CANCELLED"
            })

