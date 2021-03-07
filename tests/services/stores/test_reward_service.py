from apps.services.RewardService import createQuizRegistrationReward, deleteQuizRegistrationReward
from apps.services.stores.RewardIdStore import reward_id_store


class TestRewardService:

    # ----- createQuizRegistrationReward ----- #
    def test_createQuizRegistrationReward_ok(self, mocker):
        mocker.patch(
            'apps.services.RewardService.createReward',
            return_value="id_test"
        )

        createQuizRegistrationReward()

        assert reward_id_store.getRegistrationRewardId() == "id_test"

    # ----- deleteQuizRegistrationReward ----- #
    def test_deleteQuizRegistrationReward(self, mocker):
        mocker.patch(
            'apps.services.RewardService.deleteReward'
        )

        deleteQuizRegistrationReward()

        assert reward_id_store.getRegistrationRewardId() is None
