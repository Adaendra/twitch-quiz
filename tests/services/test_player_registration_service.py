from apps.services.PlayerRegistrationService import registerPlayersFromRegistrationReward, quiz_store, sendContestantCheckInStatistics


class TestPlayerRegistrationService:

    # ----- registerPlayersFromRegistrationReward ----- #
    def test_registerPlayersFromRegistrationReward_ok(self, mocker):
        quiz_store.isPlayerCheckInOpen = False
        quiz_store.listContestants = []
        mocker.patch(
            'apps.services.PlayerRegistrationService.getUnfulfilledRewardRedemptions',
            return_value=[
                {"broadcaster_name": "P1", "id": "1"},
                {"broadcaster_name": "P1", "id": "2"},
                {"broadcaster_name": "P2", "id": "3"},
            ]
        )
        mocker.patch(
            'apps.services.PlayerRegistrationService.updateRewardRedemptionStatus'
        )
        mocker.patch(
            'apps.services.PlayerRegistrationService.sendContestantCheckInStatistics'
        )

        registerPlayersFromRegistrationReward(True)

        assert len(quiz_store.listContestants) == 2

    # ----- sendContestantCheckInStatistics ----- #
    def test_sendContestantCheckInStatistics_ok(self, mocker):
        mocker.patch(
            'apps.services.PlayerRegistrationService.emit'
        )
        sendContestantCheckInStatistics()
