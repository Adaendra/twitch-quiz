from apps.services.ErrorService import raiseError


class TestErrorService:

    def test_raise_error(self, mocker):
        mocker.patch(
            'apps.services.ErrorService.emit'
        )
        raiseError("Test error message")
