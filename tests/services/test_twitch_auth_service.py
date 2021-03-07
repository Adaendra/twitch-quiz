from apps.services.TwitchAuthService import generateRedemptionToken


class TestTwitchAuthService:

    # ----- generateRedemptionToken ----- #
    def test_generateRedemptionToken_ok(self, mocker):
        mock_response = mocker.patch(
            'apps.services.TwitchAuthService.doHttpPost'
        )
        mock_response.return_value.status_code = 200
        mock_response.return_value.json.return_value = {'access_token' : "test_token"}

        assert generateRedemptionToken() == "test_token"

    def test_generateRedemptionToken_nok(self, mocker):
        mock_response = mocker.patch(
            'apps.services.TwitchAuthService.doHttpPost'
        )
        mock_response.return_value.status_code = 400
        mock_response.return_value.json.return_value = {'access_token' : "test_token"}

        assert generateRedemptionToken() == ""
