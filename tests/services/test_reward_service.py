from unittest.mock import call

from apps.services.RewardService import createQuizRegistrationReward, deleteQuizRegistrationReward
from apps.services.stores.RewardIdStore import reward_id_store
from apps.constants.RewardsConstants import PLAYER_REGISTRATION_REWARD_PARAM_NAME, PLAYER_REGISTRATION_REWARD_TITLE


class TestRewardService:

    # ----- createQuizRegistrationReward ----- #
    def test_createQuizRegistrationReward_ok(self, mocker):
        mock_create_reward = mocker.patch(
            'apps.services.RewardService.createReward',
            return_value="id_test"
        )
        mock_reward_cost = mocker.patch(
            'apps.services.RewardService.user_config_store.getRewardCost',
            return_value=5000
        )

        createQuizRegistrationReward()

        assert reward_id_store.getRegistrationRewardId() == "id_test"

        assert mock_create_reward.call_count == 1
        assert mock_create_reward.call_args == call(PLAYER_REGISTRATION_REWARD_TITLE, 5000)

        assert mock_reward_cost.call_count == 1
        assert mock_reward_cost.call_args == call(PLAYER_REGISTRATION_REWARD_PARAM_NAME)

    # ----- deleteQuizRegistrationReward ----- #
    def test_deleteQuizRegistrationReward(self, mocker):
        mock_delete_reward = mocker.patch(
            'apps.services.RewardService.deleteReward'
        )
        reward_id_store.setRegistrationRewardId("registration_reward_id")

        deleteQuizRegistrationReward()

        assert reward_id_store.getRegistrationRewardId() is None

        assert mock_delete_reward.call_count == 1
        assert mock_delete_reward.call_args == call("registration_reward_id")
