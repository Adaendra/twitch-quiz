from unittest.mock import call
from apps.constants.SocketMessageTypeConstants import SOCKET_EVENT_NOTIFICATION_MESSAGE
from apps.constants.NotificationLevelConstants import NOTIFICATION_LEVEL_ERROR

from apps.services.ErrorService import raiseError


class TestErrorService:

    # ----- raiseError ----- #
    def test_raiseError_ok(self, mocker):
        mock_emit = mocker.patch(
            'apps.services.ErrorService.emit'
        )
        raiseError("Test error message")

        assert mock_emit.call_count == 1
        assert mock_emit.call_args == call(SOCKET_EVENT_NOTIFICATION_MESSAGE, {
            "message": 'Error raised: Test error message',
            "level": NOTIFICATION_LEVEL_ERROR
        })
