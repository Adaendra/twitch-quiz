from apps import render_template


class WebController(object):
    """
    WebController
    -------------

    Controller to display all web pages.
    """

    def __init__(self):
        pass

    def getWebApp(self):
        """
        :return: The render template of the webapp.
        """
        return render_template('twitch_quiz_frontend/index.html')


webController = WebController()
