from unittest.mock import call

from apps.services.RewardService import createQuizRegistrationReward, deleteQuizRegistrationReward, \
    createQuizAnswersReward, deleteQuizAnswersReward
from apps.services.stores.RewardIdStore import reward_id_store
from apps.constants.RewardsConstants import PLAYER_REGISTRATION_REWARD_PARAM_NAME, PLAYER_REGISTRATION_REWARD_TITLE, \
    RESPONSE_A_REWARD_TITLE, RESPONSE_B_REWARD_TITLE, RESPONSE_C_REWARD_TITLE, RESPONSE_D_REWARD_TITLE


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

    # ----- createQuizAnswersReward ----- #
    def test_createQuizAnswersReward_ok(self, mocker):
        mock_create_reward = mocker.patch(
            'apps.services.RewardService.createReward',
            return_value="id_test"
        )

        createQuizAnswersReward()

        assert reward_id_store.getResponseARewardId() == "id_test"
        assert reward_id_store.getResponseBRewardId() == "id_test"
        assert reward_id_store.getResponseCRewardId() == "id_test"
        assert reward_id_store.getResponseDRewardId() == "id_test"

        assert mock_create_reward.call_count == 4
        assert mock_create_reward.call_args_list == [
            call(RESPONSE_A_REWARD_TITLE, 0),
            call(RESPONSE_B_REWARD_TITLE, 0),
            call(RESPONSE_C_REWARD_TITLE, 0),
            call(RESPONSE_D_REWARD_TITLE, 0)
        ]

    # ----- deleteQuizAnswersReward ----- #
    def test_deleteQuizAnswersReward_ok(self, mocker):
        mock_delete_reward = mocker.patch(
            'apps.services.RewardService.deleteReward'
        )

        reward_id_store.setResponseARewardId("A")
        reward_id_store.setResponseBRewardId("B")
        reward_id_store.setResponseCRewardId("C")
        reward_id_store.setResponseDRewardId("D")

        deleteQuizAnswersReward()

        assert reward_id_store.getResponseARewardId() is None
        assert reward_id_store.getResponseBRewardId() is None
        assert reward_id_store.getResponseCRewardId() is None
        assert reward_id_store.getResponseDRewardId() is None

        assert mock_delete_reward.call_count == 4
        assert mock_delete_reward.call_args_list == [
            call("A"), call("B"), call("C"), call("D")
        ]
