from unittest.mock import call

from apps.services.utils.HttpUtils import doHttpPut,doHttpPatch,doHttpPost,doHttpDelete,doHttpGet


class TestHttpUtils:

    # ----- doHttpGet ----- #
    def test_doHttpGet_ok(self, mocker):
        mock_response = {
            "responseCode": 200
        }

        mock_http = mocker.patch(
            'apps.services.utils.HttpUtils.requests.get',
            return_value=mock_response
        )

        assert doHttpGet("url", {"param" : "param1"}, {"header": "header1"}) == mock_response

        assert mock_http.call_count == 1
        assert mock_http.call_args == call(url="url", params={"param" : "param1"}, headers={"header": "header1"})

    # ------ doHttpDelete ----- #
    def test_doHttpDelete_ok(self, mocker):
        mock_response = {
            "responseCode": 200
        }

        mock_http = mocker.patch(
            'apps.services.utils.HttpUtils.requests.delete',
            return_value=mock_response
        )

        assert doHttpDelete("url", {"param" : "param1"}, {"header": "header1"}) == mock_response

        assert mock_http.call_count == 1
        assert mock_http.call_args == call(url="url", params={"param" : "param1"}, headers={"header": "header1"})

    # ----- doHttpPost ----- #
    def test_doHttpPost_ok(self, mocker):
        mock_response = {
            "responseCode": 200
        }

        mock_http = mocker.patch(
            'apps.services.utils.HttpUtils.requests.post',
            return_value=mock_response
        )

        assert doHttpPost("url", {"param" : "param1"}, {"header": "header1"}, {"body": "b1"}) == mock_response

        assert mock_http.call_count == 1
        assert mock_http.call_args == call(url="url", params={"param" : "param1"}, data={"body": "b1"}, headers={"header": "header1"})

    # ----- doHttpPatch ----- #
    def test_doHttpPatch_ok(self, mocker):
        mock_response = {
            "responseCode": 200
        }

        mock_http = mocker.patch(
            'apps.services.utils.HttpUtils.requests.patch',
            return_value=mock_response
        )

        assert doHttpPatch("url", {"param" : "param1"}, {"header": "header1"}, {"body": "b1"}) == mock_response

        assert mock_http.call_count == 1
        assert mock_http.call_args == call(url="url", params={"param" : "param1"}, data={"body": "b1"}, headers={"header": "header1"})

    # ----- doHttpPut ----- #
    def test_doHttpPut_ok(self, mocker):
        mock_response = {
            "responseCode": 200
        }

        mock_http = mocker.patch(
            'apps.services.utils.HttpUtils.requests.put',
            return_value=mock_response
        )

        assert doHttpPut("url", {"param" : "param1"}, {"header": "header1"}, {"body": "b1"}) == mock_response

        assert mock_http.call_count == 1
        assert mock_http.call_args == call(url="url", params={"param" : "param1"}, data={"body": "b1"}, headers={"header": "header1"})
