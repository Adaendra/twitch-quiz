from apps.services.utils.HttpUtils import doHttpPost
from apps.services.stores.UserConfigStore import user_config_store
from apps.constants.TwitchURLConstants import AUTH_TOKEN_GENERATION_URL

"""
TwitchAuthService
-----------------

Class which contains all that we need to retrieve auth token from twitch.
Documentation :
- Token generation : https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/#oauth-client-credentials-flow
- Auth scopes : https://dev.twitch.tv/docs/authentication/#scopes
"""


def generateRedemptionToken():
    """
    Generate a Twitch token for redemption scopes.
    :return: String - The Bearer Token.
    """

    response = doHttpPost(
        url=AUTH_TOKEN_GENERATION_URL,
        params={
            'client_id': user_config_store.getClientId(),
            'client_secret': user_config_store.getClientSecret(),
            'grant_type': 'client_credentials',
            'scope': 'channel:manage:redemptions channel:read:redemptions'
        }
    )

    # Return the token if the answer is correct, otherwise return an empty token.
    return response.json()['access_token'] if response.status_code == 200 else ''
