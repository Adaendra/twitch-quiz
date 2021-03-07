from apps import app
from apps.controllers.WebController import webController


class WebRoutes(object):
    """
    WebRoutes
    ---------

    Contains all routes which expose webpages.
    """

    @app.route('/', methods=['GET'])
    def getWebApp():
        """
        :return: Return the index.html of the Vue.js webapp.
        """
        return webController.getWebApp()
