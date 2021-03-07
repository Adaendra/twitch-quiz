from unittest.mock import call
from apps.constants.TwitchURLConstants import AUTH_TOKEN_GENERATION_URL
from apps.services.TwitchAuthService import generateRedemptionToken


class TestTwitchAuthService:

    # ----- generateRedemptionToken ----- #
    def test_generateRedemptionToken_ok(self, mocker):
        mock_http_post = mocker.patch(
            'apps.services.TwitchAuthService.doHttpPost'
        )
        mock_http_post.return_value.status_code = 200
        mock_http_post.return_value.json.return_value = {'access_token' : "test_token"}

        mock_client_id = mocker.patch(
            'apps.services.TwitchAuthService.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_client_secret = mocker.patch(
            'apps.services.TwitchAuthService.user_config_store.getClientSecret',
            return_value="client_secret"
        )

        assert generateRedemptionToken() == "test_token"

        assert mock_http_post.call_count == 1
        assert mock_http_post.call_args == call(
            url=AUTH_TOKEN_GENERATION_URL,
            params={
                'client_id': 'client_id',
                'client_secret': "client_secret",
                'grant_type': 'client_credentials',
                'scope': 'channel:manage:redemptions channel:read:redemptions'
            }
        )

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_client_secret.call_count == 1
        assert mock_client_secret.call_args == call()

    def test_generateRedemptionToken_nok(self, mocker):
        mock_http_post = mocker.patch(
            'apps.services.TwitchAuthService.doHttpPost'
        )
        mock_http_post.return_value.status_code = 400
        mock_http_post.return_value.json.return_value = {'access_token' : "test_token"}

        mock_client_id = mocker.patch(
            'apps.services.TwitchAuthService.user_config_store.getClientId',
            return_value="client_id"
        )
        mock_client_secret = mocker.patch(
            'apps.services.TwitchAuthService.user_config_store.getClientSecret',
            return_value="client_secret"
        )

        assert generateRedemptionToken() == ""

        assert mock_http_post.call_count == 1
        assert mock_http_post.call_args == call(
            url=AUTH_TOKEN_GENERATION_URL,
            params={
                'client_id': 'client_id',
                'client_secret': "client_secret",
                'grant_type': 'client_credentials',
                'scope': 'channel:manage:redemptions channel:read:redemptions'
            }
        )

        assert mock_client_id.call_count == 1
        assert mock_client_id.call_args == call()

        assert mock_client_secret.call_count == 1
        assert mock_client_secret.call_args == call()
