from apps.services.TwitchStreamService import retrieveBroadcastId


class TestTwitchStreamService:

    def test_retrieveBroadcastId(self, mocker):
        mockResponse = mocker.patch(
            'apps.services.TwitchStreamService.doHttpGet'
        )
        mockResponse.return_value.json.return_value = {'data': [{'id': 'random_id_test'}]}

        assert retrieveBroadcastId('bearer_token', 'client_id') == 'random_id_test'
