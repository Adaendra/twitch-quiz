from apps.services.utils.HttpUtils import doHttpPut,doHttpPatch,doHttpPost,doHttpDelete,doHttpGet


class TestHttpUtils:

    def test_do_http_get(self, mocker):
        mock_response = {
            "responseCode" : 200
        }

        mocker.patch(
            'apps.services.utils.HttpUtils.requests.get',
            return_value=mock_response
        )

        assert doHttpGet("", {}, {}) == mock_response

    def test_do_http_delete(self, mocker):
        mock_response = {
            "responseCode" : 200
        }

        mocker.patch(
            'apps.services.utils.HttpUtils.requests.delete',
            return_value=mock_response
        )

        assert doHttpDelete("", {}, {}) == mock_response

    def test_do_http_post(self, mocker):
        mock_response = {
            "responseCode" : 200
        }

        mocker.patch(
            'apps.services.utils.HttpUtils.requests.post',
            return_value=mock_response
        )

        assert doHttpPost("", {}, {}, {}) == mock_response

    def test_do_http_patch(self, mocker):
        mock_response = {
            "responseCode" : 200
        }

        mocker.patch(
            'apps.services.utils.HttpUtils.requests.patch',
            return_value=mock_response
        )

        assert doHttpPatch("", {}, {}, {}) == mock_response

    def test_do_http_put(self, mocker):
        mock_response = {
            "responseCode" : 200
        }

        mocker.patch(
            'apps.services.utils.HttpUtils.requests.put',
            return_value=mock_response
        )

        assert doHttpPut("", {}, {}, {}) == mock_response
