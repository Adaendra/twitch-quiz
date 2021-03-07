from apps import emit
from apps.constants.SocketMessageTypeConstants import SOCKET_EVENT_NOTIFICATION_MESSAGE
from apps.constants.NotificationLevelConstants import NOTIFICATION_LEVEL_ERROR

"""
ErrorService
------------

Contains all methods associated to the error management.
"""


def raiseError(error_message):
    """
    Raise an error and send it to connected users.
    :param error_message: String - The error message to raise.
    """
    emit(SOCKET_EVENT_NOTIFICATION_MESSAGE, {
        "message": 'Error raised: ' + error_message,
        "level": NOTIFICATION_LEVEL_ERROR
    })

