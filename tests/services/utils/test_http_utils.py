from apps.services.utils.HttpUtils import doHttpPut,doHttpPatch,doHttpPost,doHttpDelete,doHttpGet


class TestHttpUtils:

    # ----- doHttpGet ----- #
    def test_doHttpGet_ok(self, mocker):
        mock_response = {
            "responseCode": 200
        }

        mocker.patch(
            'apps.services.utils.HttpUtils.requests.get',
            return_value=mock_response
        )

        assert doHttpGet("", {}, {}) == mock_response

    # ------ doHttpDelete ----- #
    def test_doHttpDelete_ok(self, mocker):
        mock_response = {
            "responseCode": 200
        }

        mocker.patch(
            'apps.services.utils.HttpUtils.requests.delete',
            return_value=mock_response
        )

        assert doHttpDelete("", {}, {}) == mock_response

    # ----- doHttpPost ----- #
    def test_doHttpPost_ok(self, mocker):
        mock_response = {
            "responseCode": 200
        }

        mocker.patch(
            'apps.services.utils.HttpUtils.requests.post',
            return_value=mock_response
        )

        assert doHttpPost("", {}, {}, {}) == mock_response

    # ----- doHttpPatch ----- #
    def test_doHttpPatch_ok(self, mocker):
        mock_response = {
            "responseCode": 200
        }

        mocker.patch(
            'apps.services.utils.HttpUtils.requests.patch',
            return_value=mock_response
        )

        assert doHttpPatch("", {}, {}, {}) == mock_response

    # ----- doHttpPut ----- #
    def test_doHttpPut_ok(self, mocker):
        mock_response = {
            "responseCode": 200
        }

        mocker.patch(
            'apps.services.utils.HttpUtils.requests.put',
            return_value=mock_response
        )

        assert doHttpPut("", {}, {}, {}) == mock_response
