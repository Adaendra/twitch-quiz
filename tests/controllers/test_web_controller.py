from unittest.mock import call

from apps.controllers.WebController import webController


class TestWebController:

    # ----- getWebApp ----- #
    def test_getWebApp_ok(self, mocker):
        mock_render_template = mocker.patch(
            'apps.controllers.WebController.render_template'
        )

        webController.getWebApp()

        assert mock_render_template.call_count == 1
        assert mock_render_template.call_args == call('twitch_quiz_frontend/index.html')
