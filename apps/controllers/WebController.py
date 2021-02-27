from apps import app, render_template

# Controller to display all web pages.
class WebController(object):

    def __init__(self):
        pass

    def getWebApp(self):
        return render_template('twitch_quiz_frontend/index.html')

webcontroller = WebController()