from unittest.mock import call

from apps.services.PlayerAnswerManagementService import saveContestantsAnswer, processPlayersAnswer
from apps.services.stores.QuizStore import quiz_store
from apps.services.stores.RewardIdStore import reward_id_store
from apps.constants.QuizConstants import SELECTED_ANSWER_A, SELECTED_ANSWER_B, SELECTED_ANSWER_C, SELECTED_ANSWER_D
from apps.constants.RewardsConstants import REGISTRATION_REWARD_STATUS_CANCELLED, REGISTRATION_REWARD_STATUS_FULFILLED
from apps.models.QuizContestant import QuizContestant
from apps.models.RewardRedemption import RewardRedemption


class TestPlayerAnswerManagementService:

    # ----- saveContestantsAnswer ----- #
    def test_saveContestantsAnswer_ok_less25(self, mocker):
        mock_process_players_answer = mocker.patch(
            'apps.services.PlayerAnswerManagementService.processPlayersAnswer',
            return_value=5
        )

        mock_time_sleep = mocker.patch(
            'apps.services.PlayerAnswerManagementService.time.sleep'
        )

        mock_send_stats = mocker.patch(
            'apps.services.PlayerAnswerManagementService.sendStatsAnswersOngoing'
        )

        reward_id_store.setResponseARewardId("id_a")
        reward_id_store.setResponseBRewardId("id_b")
        reward_id_store.setResponseCRewardId("id_c")
        reward_id_store.setResponseDRewardId("id_d")

        quiz_store.isQuizOnGoing = False
        quiz_store.isQuestionOnGoing = False

        saveContestantsAnswer(True, True)

        assert mock_process_players_answer.call_count == 4
        assert mock_process_players_answer.call_args_list == [
            call("id_a", True, SELECTED_ANSWER_A),
            call("id_b", True, SELECTED_ANSWER_B),
            call("id_c", True, SELECTED_ANSWER_C),
            call("id_d", True, SELECTED_ANSWER_D),
        ]

        assert mock_time_sleep.call_count == 1
        assert mock_time_sleep.call_args == call(0.5)

        assert mock_send_stats.call_count == 1
        assert mock_send_stats.call_args == call()

    def test_saveContestantsAnswer_ok_more25(self, mocker):
        mock_process_players_answer = mocker.patch(
            'apps.services.PlayerAnswerManagementService.processPlayersAnswer',
            return_value=10
        )

        mock_time_sleep = mocker.patch(
            'apps.services.PlayerAnswerManagementService.time.sleep'
        )

        mock_send_stats = mocker.patch(
            'apps.services.PlayerAnswerManagementService.sendStatsAnswersOngoing'
        )

        reward_id_store.setResponseARewardId("id_a")
        reward_id_store.setResponseBRewardId("id_b")
        reward_id_store.setResponseCRewardId("id_c")
        reward_id_store.setResponseDRewardId("id_d")

        quiz_store.isQuizOnGoing = False
        quiz_store.isQuestionOnGoing = False

        saveContestantsAnswer(True, True)

        assert mock_process_players_answer.call_count == 4
        assert mock_process_players_answer.call_args_list == [
            call("id_a", True, SELECTED_ANSWER_A),
            call("id_b", True, SELECTED_ANSWER_B),
            call("id_c", True, SELECTED_ANSWER_C),
            call("id_d", True, SELECTED_ANSWER_D),
        ]

        assert mock_time_sleep.call_count == 1
        assert mock_time_sleep.call_args == call(0.2)

        assert mock_send_stats.call_count == 1
        assert mock_send_stats.call_args == call()

    # ----- processPlayersAnswer ----- #
    def test_processPlayersAnswer_ok_questionOngoing(self, mocker):
        mock_get_unfulfilled_redemptions = mocker.patch(
            'apps.services.PlayerAnswerManagementService.getUnfulfilledRewardRedemptions',
            return_value=[
                RewardRedemption('id_a1', 'player_a'),
                RewardRedemption('id_a2', 'player_a'),
                RewardRedemption('id_b', 'player_b'),
                RewardRedemption('id_c', 'player_c'),
                RewardRedemption('id_d', 'player_d')
            ]
        )
        mock_update_redemptions = mocker.patch(
            'apps.services.PlayerAnswerManagementService.updateRewardRedemptionStatus'
        )

        contestant_with_answer = QuizContestant("player_c", 2)
        contestant_with_answer.selected_answer = "B"

        quiz_store.listContestants = [
            QuizContestant("player_a", 2),
            QuizContestant("player_b", 2),
            contestant_with_answer
        ]

        response = processPlayersAnswer("answer_reward_id", True, "A")

        assert response == 5

        assert mock_get_unfulfilled_redemptions.call_count == 1
        assert mock_get_unfulfilled_redemptions.call_args == call("answer_reward_id")

        assert mock_update_redemptions.call_count == 5
        assert mock_update_redemptions.call_args_list == [
            call("answer_reward_id", "id_a1", REGISTRATION_REWARD_STATUS_FULFILLED),
            call("answer_reward_id", "id_a2", REGISTRATION_REWARD_STATUS_CANCELLED),
            call("answer_reward_id", "id_b", REGISTRATION_REWARD_STATUS_FULFILLED),
            call("answer_reward_id", "id_c", REGISTRATION_REWARD_STATUS_CANCELLED),
            call("answer_reward_id", "id_d", REGISTRATION_REWARD_STATUS_CANCELLED)
        ]

        assert next(iter(filter(lambda contestant: contestant.contestant_name == "player_a",
                                quiz_store.listContestants) or []), None).selected_answer == "A"
        assert next(iter(filter(lambda contestant: contestant.contestant_name == "player_b",
                                quiz_store.listContestants) or []), None).selected_answer == "A"
        assert next(iter(filter(lambda contestant: contestant.contestant_name == "player_c",
                                quiz_store.listContestants) or []), None).selected_answer == "B"

    def test_processPlayersAnswer_ok_questionNotOngoing(self, mocker):
        mock_get_unfulfilled_redemptions = mocker.patch(
            'apps.services.PlayerAnswerManagementService.getUnfulfilledRewardRedemptions',
            return_value=[
                RewardRedemption('id_a1', 'player_a'),
                RewardRedemption('id_a2', 'player_a'),
                RewardRedemption('id_b', 'player_b'),
                RewardRedemption('id_c', 'player_c'),
                RewardRedemption('id_d', 'player_d')
            ]
        )
        mock_update_redemptions = mocker.patch(
            'apps.services.PlayerAnswerManagementService.updateRewardRedemptionStatus'
        )

        contestant_with_answer = QuizContestant("player_c", 2)
        contestant_with_answer.selected_answer = "B"

        quiz_store.listContestants = [
            QuizContestant("player_a", 2),
            QuizContestant("player_b", 2),
            contestant_with_answer
        ]

        response = processPlayersAnswer("answer_reward_id", False, "A")

        assert response == 5

        assert mock_get_unfulfilled_redemptions.call_count == 1
        assert mock_get_unfulfilled_redemptions.call_args == call("answer_reward_id")

        assert mock_update_redemptions.call_count == 5
        assert mock_update_redemptions.call_args_list == [
            call("answer_reward_id", "id_a1", REGISTRATION_REWARD_STATUS_CANCELLED),
            call("answer_reward_id", "id_a2", REGISTRATION_REWARD_STATUS_CANCELLED),
            call("answer_reward_id", "id_b", REGISTRATION_REWARD_STATUS_CANCELLED),
            call("answer_reward_id", "id_c", REGISTRATION_REWARD_STATUS_CANCELLED),
            call("answer_reward_id", "id_d", REGISTRATION_REWARD_STATUS_CANCELLED)
        ]

        assert next(iter(filter(lambda contestant: contestant.contestant_name == "player_a",
                                quiz_store.listContestants) or []), None).selected_answer is None
        assert next(iter(filter(lambda contestant: contestant.contestant_name == "player_b",
                                quiz_store.listContestants) or []), None).selected_answer is None
        assert next(iter(filter(lambda contestant: contestant.contestant_name == "player_c",
                                quiz_store.listContestants) or []), None).selected_answer == "B"
