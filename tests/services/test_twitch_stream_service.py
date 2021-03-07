from apps.services.TwitchStreamService import retrieveBroadcastId


class TestTwitchStreamService:

    # ----- retrieveBroadcastId ----- #
    def test_retrieveBroadcastId_ok(self, mocker):
        mock_response = mocker.patch(
            'apps.services.TwitchStreamService.doHttpGet'
        )
        mock_response.return_value.json.return_value = {'data': [{'id': 'random_id_test'}]}

        assert retrieveBroadcastId('bearer_token', 'client_id') == 'random_id_test'
