from apps.services.utils.HttpUtils import doHttpGet

"""
TwitchStreamService
------------------

Contains all methods linked to streams
Documentation: https://dev.twitch.tv/docs/api/reference#get-streams
"""


def retrieveBroadcastId(bearer_token, client_id):
    """
    Retrieve the BroadcastId.
    :param bearer_token: String - Bearer auth token.
    :param client_id: String - Client Id.
    :return: String - The broadcast id.
    """
    return doHttpGet(
        url='https://api.twitch.tv/helix/streams',
        headers={
            'Authorization': 'Bearer ' + bearer_token,
            'Client-Id': client_id
        }
    ).json()['data'][0]['id']

