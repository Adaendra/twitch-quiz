from unittest.mock import call
from apps.constants.SocketMessageTypeConstants import SOCKET_EVENT_STATS_CONSTESTANTS_CHECK_IN
from apps.services.stores.RewardIdStore import reward_id_store
from apps.services.PlayerRegistrationService import registerPlayersFromRegistrationReward, quiz_store, sendContestantCheckInStatistics
from apps.constants.RewardsConstants import REGISTRATION_REWARD_STATUS_FULFILLED, REGISTRATION_REWARD_STATUS_CANCELLED


class TestPlayerRegistrationService:

    # ----- registerPlayersFromRegistrationReward ----- #
    def test_registerPlayersFromRegistrationReward_ok(self, mocker):
        quiz_store.isPlayerCheckInOpen = False
        quiz_store.listContestants = []
        reward_id_store.setRegistrationRewardId("registration_reward_id")
        mock_list_redemptions = mocker.patch(
            'apps.services.PlayerRegistrationService.getUnfulfilledRewardRedemptions',
            return_value=[
                {"broadcaster_name": "P1", "id": "1"},
                {"broadcaster_name": "P1", "id": "2"},
                {"broadcaster_name": "P2", "id": "3"},
            ]
        )
        mock_update_status = mocker.patch(
            'apps.services.PlayerRegistrationService.updateRewardRedemptionStatus'
        )
        mock_send_stats = mocker.patch(
            'apps.services.PlayerRegistrationService.sendContestantCheckInStatistics'
        )

        registerPlayersFromRegistrationReward(True)

        assert len(quiz_store.listContestants) == 2

        assert mock_list_redemptions.call_count == 1
        assert mock_list_redemptions.call_args == call("registration_reward_id")

        assert mock_update_status.call_count == 3
        assert mock_update_status.call_args_list == [
            call("registration_reward_id", "1", REGISTRATION_REWARD_STATUS_FULFILLED),
            call("registration_reward_id", "2", REGISTRATION_REWARD_STATUS_CANCELLED),
            call("registration_reward_id", "3", REGISTRATION_REWARD_STATUS_FULFILLED)
        ]

        assert mock_send_stats.call_count == 1
        assert mock_send_stats.call_args == call()

    # ----- sendContestantCheckInStatistics ----- #
    def test_sendContestantCheckInStatistics_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.PlayerRegistrationService.emit'
        )
        quiz_store.listContestants = [{}, {}, {}, {}]

        sendContestantCheckInStatistics()

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_STATS_CONSTESTANTS_CHECK_IN, {
            "number_contestants": 4
        })
