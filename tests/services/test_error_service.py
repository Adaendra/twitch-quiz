from apps.services.ErrorService import raiseError


class TestErrorService:

    # ----- raiseError ----- #
    def test_raiseError_ok(self, mocker):
        mocker.patch(
            'apps.services.ErrorService.emit'
        )
        raiseError("Test error message")
