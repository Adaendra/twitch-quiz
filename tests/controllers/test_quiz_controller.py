from unittest.mock import call
from apps.services.stores.QuizStore import quiz_store
from apps.controllers.QuizController import quizController
from apps.models.QuizContestant import QuizContestant
from apps.models.Ranking import Ranking
from apps.models.Question import Question


class TestQuizController:

    # ----- init_quiz ----- #
    def test_init_quiz_ok(self, mocker):
        mock_config_ctl = mocker.patch(
            'apps.controllers.QuizController.configController.isAllRequiredConfigDefined',
            return_value=True
        )
        mock_raise_error = mocker.patch(
            'apps.controllers.QuizController.raiseError'
        )
        mock_generate_token = mocker.patch(
            'apps.controllers.QuizController.generateRedemptionToken',
            return_value="token"
        )
        mock_client_id = mocker.patch(
            'apps.controllers.QuizController.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_retrieve_broadcast_id = mocker.patch(
            'apps.controllers.QuizController.retrieveBroadcastId',
            return_value=""
        )
        mock_reset_quiz = mocker.patch(
            'apps.controllers.QuizController.quiz_store.resetQuiz'
        )
        mock_create_reward = mocker.patch(
            'apps.controllers.QuizController.createQuizRegistrationReward'
        )
        mock_players_registration = mocker.patch(
            'apps.controllers.QuizController.registerPlayersFromRegistrationReward'
        )
        quiz_store.isPlayerCheckInOpen = True

        quizController.init_quiz()

        assert mock_config_ctl.call_count == 1
        assert mock_config_ctl.call_args == call()

        assert mock_raise_error.call_count == 0

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_generate_token.call_count == 1
        assert mock_generate_token.call_args == call()

        assert mock_retrieve_broadcast_id.call_count == 1
        assert mock_retrieve_broadcast_id.call_args == call("token", "client_id")

        assert mock_reset_quiz.call_count == 1
        assert mock_reset_quiz.call_args == call()

        assert mock_create_reward.call_count == 1
        assert mock_create_reward.call_args == call()

        assert mock_players_registration.call_count == 1
        assert mock_players_registration.call_args == call(True)

    def test_init_quiz_nok_missingConfig(self, mocker):
        mock_config_ctl = mocker.patch(
            'apps.controllers.QuizController.configController.isAllRequiredConfigDefined',
            return_value=False
        )
        mock_raise_error = mocker.patch(
            'apps.controllers.QuizController.raiseError'
        )
        mock_generate_token = mocker.patch(
            'apps.controllers.QuizController.generateRedemptionToken',
            return_value=""
        )
        mock_client_id = mocker.patch(
            'apps.controllers.QuizController.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_retrieve_broadcast_id = mocker.patch(
            'apps.controllers.QuizController.retrieveBroadcastId',
            return_value=""
        )
        mock_reset_quiz = mocker.patch(
            'apps.controllers.QuizController.quiz_store.resetQuiz'
        )
        mock_create_reward = mocker.patch(
            'apps.controllers.QuizController.createQuizRegistrationReward'
        )
        mock_players_registration = mocker.patch(
            'apps.controllers.QuizController.registerPlayersFromRegistrationReward'
        )
        quiz_store.isPlayerCheckInOpen = True

        quizController.init_quiz()

        assert mock_config_ctl.call_count == 1
        assert mock_config_ctl.call_args == call()

        assert mock_raise_error.call_count == 1
        assert mock_raise_error.call_args == call("At least one mandatory configuration is missing.")

        assert mock_client_id.call_count == 0

        assert mock_generate_token.call_count == 0

        assert mock_retrieve_broadcast_id.call_count == 0

        assert mock_reset_quiz.call_count == 0

        assert mock_create_reward.call_count == 0

        assert mock_players_registration.call_count == 0

    def test_init_quiz_nok_creationFailed(self, mocker):
        mock_config_ctl = mocker.patch(
            'apps.controllers.QuizController.configController.isAllRequiredConfigDefined',
            return_value=True
        )
        mock_raise_error = mocker.patch(
            'apps.controllers.QuizController.raiseError'
        )
        mock_generate_token = mocker.patch(
            'apps.controllers.QuizController.generateRedemptionToken',
            return_value="token"
        )
        mock_client_id = mocker.patch(
            'apps.controllers.QuizController.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_retrieve_broadcast_id = mocker.patch(
            'apps.controllers.QuizController.retrieveBroadcastId',
            return_value=""
        )
        mock_reset_quiz = mocker.patch(
            'apps.controllers.QuizController.quiz_store.resetQuiz'
        )
        mock_create_reward = mocker.patch(
            'apps.controllers.QuizController.createQuizRegistrationReward',
            side_effect=Exception('error')
        )
        mock_players_registration = mocker.patch(
            'apps.controllers.QuizController.registerPlayersFromRegistrationReward'
        )

        quizController.init_quiz()

        assert mock_config_ctl.call_count == 1
        assert mock_config_ctl.call_args == call()

        assert mock_raise_error.call_count == 1
        assert mock_raise_error.call_args == call("An error appears during the quiz initialization")

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_generate_token.call_count == 1
        assert mock_generate_token.call_args == call()

        assert mock_retrieve_broadcast_id.call_count == 1
        assert mock_retrieve_broadcast_id.call_args == call("token", "client_id")

        assert mock_reset_quiz.call_count == 1
        assert mock_reset_quiz.call_args == call()

        assert mock_create_reward.call_count == 1
        assert mock_create_reward.call_args == call()

        assert mock_players_registration.call_count == 0

    # ----- start_quiz ----- #
    def test_start_quiz_ok(self, mocker):
        mock_delete_quiz_registration_rewards = mocker.patch(
            'apps.controllers.QuizController.deleteQuizRegistrationReward'
        )
        mock_create_quiz_answer_rewards = mocker.patch(
            'apps.controllers.QuizController.createQuizAnswersReward'
        )
        mock_send_next_question = mocker.patch(
            'apps.controllers.QuizController.sendNextQuestion'
        )
        mock_save_constestant_answers = mocker.patch(
            'apps.controllers.QuizController.saveContestantsAnswer'
        )

        quiz_store.currentQuestionIndex = 0
        quiz_store.isQuizOnGoing = False
        quiz_store.isQuestionOnGoing = True

        quizController.start_quiz()

        assert quiz_store.currentQuestionIndex == 1
        assert quiz_store.isQuizOnGoing is True

        assert mock_delete_quiz_registration_rewards.call_count == 1
        assert mock_delete_quiz_registration_rewards.call_args == call()

        assert mock_create_quiz_answer_rewards.call_count == 1
        assert mock_create_quiz_answer_rewards.call_args == call()

        assert mock_send_next_question.call_count == 1
        assert mock_send_next_question.call_args == call()

        assert mock_save_constestant_answers.call_count == 1
        assert mock_save_constestant_answers.call_args == call(True, True)

    # ----- stop_quiz ----- #
    def test_stop_quiz_ok(self, mocker):
        mock_delete_quiz_answers_reward = mocker.patch(
            'apps.controllers.QuizController.deleteQuizAnswersReward'
        )
        mock_stop_quiz = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuiz'
        )
        mock_time_sleep = mocker.patch(
            'apps.controllers.QuizController.time.sleep'
        )
        mock_clear_answer_reward_id = mocker.patch(
            'apps.controllers.QuizController.clearAnswerRewardId'
        )

        quiz_store.isQuestionOnGoing = True
        quiz_store.isQuizOnGoing = True

        quizController.stop_quiz()

        assert quiz_store.isQuestionOnGoing is False
        assert quiz_store.isQuizOnGoing is False

        assert mock_delete_quiz_answers_reward.call_count == 1
        assert mock_delete_quiz_answers_reward.call_args == call()

        assert mock_stop_quiz.call_count == 1
        assert mock_stop_quiz.call_args == call()

        assert mock_time_sleep.call_count == 1
        assert mock_time_sleep.call_args == call(10)

        assert mock_clear_answer_reward_id.call_count == 1
        assert mock_clear_answer_reward_id.call_args == call()

    # ----- reveal_answer ----- #
    def test_reveal_answer_no_winner(self, mocker):
        ranking = Ranking()

        quiz_store.listContestants = []

        mock_send_event_reveal_answer = mocker.patch(
            'apps.controllers.QuizController.sendEventRevealAnswer'
        )
        mock_send_stats_answer_question = mocker.patch(
            'apps.controllers.QuizController.sendStatsAnswerQuestion'
        )
        mock_process_contestant_answers = mocker.patch(
            'apps.controllers.QuizController.processContestantAnswers'
        )
        mock_calculate_rankings = mocker.patch(
            'apps.controllers.QuizController.calculateRankings',
            return_value=ranking
        )
        mock_send_quiz_ranking = mocker.patch(
            'apps.controllers.QuizController.sendQuizRanking'
        )
        mock_send_event_stop_quiz_no_winner = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizNoWinner'
        )
        mock_send_event_stop_quiz_winner = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizWinner'
        )
        mock_send_event_stop_quiz_no_more_questions = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizNoMoreQuestions'
        )
        mock_send_event_continue_quiz = mocker.patch(
            'apps.controllers.QuizController.sendEventContinueQuiz'
        )

        quizController.reveal_answer()

        assert mock_send_event_reveal_answer.call_count == 1
        assert mock_send_event_reveal_answer.call_args == call()

        assert mock_send_stats_answer_question.call_count == 1
        assert mock_send_stats_answer_question.call_args == call()

        assert mock_process_contestant_answers.call_count == 1
        assert mock_process_contestant_answers.call_args == call()

        assert mock_calculate_rankings.call_count == 1
        assert mock_calculate_rankings.call_args == call()

        assert mock_send_quiz_ranking.call_count == 1
        assert mock_send_quiz_ranking.call_args == call(ranking)

        assert mock_send_event_stop_quiz_no_winner.call_count == 1
        assert mock_send_event_stop_quiz_no_winner.call_args == call()

        assert mock_send_event_stop_quiz_winner.call_count == 0
        assert mock_send_event_stop_quiz_winner.call_args is None

        assert mock_send_event_stop_quiz_no_more_questions.call_count == 0
        assert mock_send_event_stop_quiz_no_more_questions.call_args is None

        assert mock_send_event_continue_quiz.call_count == 0
        assert mock_send_event_continue_quiz.call_args is None

    def test_reveal_answer_winner(self, mocker):
        ranking = Ranking()

        quiz_store.listContestants = [
            QuizContestant("pouet", 2)
        ]

        mock_send_event_reveal_answer = mocker.patch(
            'apps.controllers.QuizController.sendEventRevealAnswer'
        )
        mock_send_stats_answer_question = mocker.patch(
            'apps.controllers.QuizController.sendStatsAnswerQuestion'
        )
        mock_process_contestant_answers = mocker.patch(
            'apps.controllers.QuizController.processContestantAnswers'
        )
        mock_calculate_rankings = mocker.patch(
            'apps.controllers.QuizController.calculateRankings',
            return_value=ranking
        )
        mock_send_quiz_ranking = mocker.patch(
            'apps.controllers.QuizController.sendQuizRanking'
        )
        mock_send_event_stop_quiz_no_winner = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizNoWinner'
        )
        mock_send_event_stop_quiz_winner = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizWinner'
        )
        mock_send_event_stop_quiz_no_more_questions = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizNoMoreQuestions'
        )
        mock_send_event_continue_quiz = mocker.patch(
            'apps.controllers.QuizController.sendEventContinueQuiz'
        )

        quizController.reveal_answer()

        assert mock_send_event_reveal_answer.call_count == 1
        assert mock_send_event_reveal_answer.call_args == call()

        assert mock_send_stats_answer_question.call_count == 1
        assert mock_send_stats_answer_question.call_args == call()

        assert mock_process_contestant_answers.call_count == 1
        assert mock_process_contestant_answers.call_args == call()

        assert mock_calculate_rankings.call_count == 1
        assert mock_calculate_rankings.call_args == call()

        assert mock_send_quiz_ranking.call_count == 1
        assert mock_send_quiz_ranking.call_args == call(ranking)

        assert mock_send_event_stop_quiz_no_winner.call_count == 0
        assert mock_send_event_stop_quiz_no_winner.call_args is None

        assert mock_send_event_stop_quiz_winner.call_count == 1
        assert mock_send_event_stop_quiz_winner.call_args == call()

        assert mock_send_event_stop_quiz_no_more_questions.call_count == 0
        assert mock_send_event_stop_quiz_no_more_questions.call_args is None

        assert mock_send_event_continue_quiz.call_count == 0
        assert mock_send_event_continue_quiz.call_args is None

    def test_reveal_answer_no_more_questions(self, mocker):
        ranking = Ranking()

        quiz_store.listContestants = [
            QuizContestant("pouet", 2),
            QuizContestant("pouet2", 2)
        ]
        quiz_store.listQuestions = []
        quiz_store.currentQuestionIndex = 2

        mock_send_event_reveal_answer = mocker.patch(
            'apps.controllers.QuizController.sendEventRevealAnswer'
        )
        mock_send_stats_answer_question = mocker.patch(
            'apps.controllers.QuizController.sendStatsAnswerQuestion'
        )
        mock_process_contestant_answers = mocker.patch(
            'apps.controllers.QuizController.processContestantAnswers'
        )
        mock_calculate_rankings = mocker.patch(
            'apps.controllers.QuizController.calculateRankings',
            return_value=ranking
        )
        mock_send_quiz_ranking = mocker.patch(
            'apps.controllers.QuizController.sendQuizRanking'
        )
        mock_send_event_stop_quiz_no_winner = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizNoWinner'
        )
        mock_send_event_stop_quiz_winner = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizWinner'
        )
        mock_send_event_stop_quiz_no_more_questions = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizNoMoreQuestions'
        )
        mock_send_event_continue_quiz = mocker.patch(
            'apps.controllers.QuizController.sendEventContinueQuiz'
        )

        quizController.reveal_answer()

        assert mock_send_event_reveal_answer.call_count == 1
        assert mock_send_event_reveal_answer.call_args == call()

        assert mock_send_stats_answer_question.call_count == 1
        assert mock_send_stats_answer_question.call_args == call()

        assert mock_process_contestant_answers.call_count == 1
        assert mock_process_contestant_answers.call_args == call()

        assert mock_calculate_rankings.call_count == 1
        assert mock_calculate_rankings.call_args == call()

        assert mock_send_quiz_ranking.call_count == 1
        assert mock_send_quiz_ranking.call_args == call(ranking)

        assert mock_send_event_stop_quiz_no_winner.call_count == 0
        assert mock_send_event_stop_quiz_no_winner.call_args is None

        assert mock_send_event_stop_quiz_winner.call_count == 0
        assert mock_send_event_stop_quiz_winner.call_args is None

        assert mock_send_event_stop_quiz_no_more_questions.call_count == 1
        assert mock_send_event_stop_quiz_no_more_questions.call_args == call()

        assert mock_send_event_continue_quiz.call_count == 0
        assert mock_send_event_continue_quiz.call_args is None

    def test_reveal_answer_continue(self, mocker):
        ranking = Ranking()

        quiz_store.listContestants = [
            QuizContestant("pouet", 2),
            QuizContestant("pouet2", 2)
        ]
        quiz_store.listQuestions = [
            Question("", [], "", ""),
            Question("", [], "", "")
        ]
        quiz_store.currentQuestionIndex = 0

        mock_send_event_reveal_answer = mocker.patch(
            'apps.controllers.QuizController.sendEventRevealAnswer'
        )
        mock_send_stats_answer_question = mocker.patch(
            'apps.controllers.QuizController.sendStatsAnswerQuestion'
        )
        mock_process_contestant_answers = mocker.patch(
            'apps.controllers.QuizController.processContestantAnswers'
        )
        mock_calculate_rankings = mocker.patch(
            'apps.controllers.QuizController.calculateRankings',
            return_value=ranking
        )
        mock_send_quiz_ranking = mocker.patch(
            'apps.controllers.QuizController.sendQuizRanking'
        )
        mock_send_event_stop_quiz_no_winner = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizNoWinner'
        )
        mock_send_event_stop_quiz_winner = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizWinner'
        )
        mock_send_event_stop_quiz_no_more_questions = mocker.patch(
            'apps.controllers.QuizController.sendEventStopQuizNoMoreQuestions'
        )
        mock_send_event_continue_quiz = mocker.patch(
            'apps.controllers.QuizController.sendEventContinueQuiz'
        )

        quizController.reveal_answer()

        assert mock_send_event_reveal_answer.call_count == 1
        assert mock_send_event_reveal_answer.call_args == call()

        assert mock_send_stats_answer_question.call_count == 1
        assert mock_send_stats_answer_question.call_args == call()

        assert mock_process_contestant_answers.call_count == 1
        assert mock_process_contestant_answers.call_args == call()

        assert mock_calculate_rankings.call_count == 1
        assert mock_calculate_rankings.call_args == call()

        assert mock_send_quiz_ranking.call_count == 1
        assert mock_send_quiz_ranking.call_args == call(ranking)

        assert mock_send_event_stop_quiz_no_winner.call_count == 0
        assert mock_send_event_stop_quiz_no_winner.call_args is None

        assert mock_send_event_stop_quiz_winner.call_count == 0
        assert mock_send_event_stop_quiz_winner.call_args is None

        assert mock_send_event_stop_quiz_no_more_questions.call_count == 0
        assert mock_send_event_stop_quiz_no_more_questions.call_args is None

        assert mock_send_event_continue_quiz.call_count == 1
        assert mock_send_event_continue_quiz.call_args == call()

    # ----- next_question ----- #
    def test_next_question_ok(self, mocker):
        mock_time_sleep = mocker.patch(
            'apps.controllers.QuizController.time.sleep'
        )
        mock_send_next_question = mocker.patch(
            'apps.controllers.QuizController.sendNextQuestion'
        )
        mock_save_constestant_answers = mocker.patch(
            'apps.controllers.QuizController.saveContestantsAnswer'
        )

        quiz_store.currentQuestionIndex = 5
        quiz_store.isQuizOnGoing = False
        quiz_store.isQuestionOnGoing = False

        quizController.next_question()

        assert quiz_store.currentQuestionIndex == 6
        assert quiz_store.isQuizOnGoing is True
        assert quiz_store.isQuestionOnGoing is True

        assert mock_time_sleep.call_count == 1
        assert mock_time_sleep.call_args == call(1)

        assert mock_send_next_question.call_count == 1
        assert mock_send_next_question.call_args == call()

        assert mock_save_constestant_answers.call_count == 1
        assert mock_save_constestant_answers.call_args == call(True, True)


