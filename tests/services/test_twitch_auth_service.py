from apps.services.TwitchAuthService import generateRedemptionToken


class TestTwitchAuthService:

    def test_generateRedemptionToken_ok(self, mocker):
        mockResponse = mocker.patch(
            'apps.services.TwitchAuthService.doHttpPost'
        )
        mockResponse.return_value.status_code = 200
        mockResponse.return_value.json.return_value = {'access_token' : "test_token"}

        assert generateRedemptionToken() == "test_token"

    def test_generateRedemptionToken_nok(self, mocker):
        mockResponse = mocker.patch(
            'apps.services.TwitchAuthService.doHttpPost'
        )
        mockResponse.return_value.status_code = 400
        mockResponse.return_value.json.return_value = {'access_token' : "test_token"}

        assert generateRedemptionToken() == ""
