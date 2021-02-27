from apps import app, render_template
from apps.controllers.WebController import webcontroller

# Routes to display all web pages.
class WebRoutes(object):

    # Return the index.html of the Vue.js webapp.
    @app.route('/', methods=['GET'])
    def getWebApp():
        return webcontroller.getWebApp()
