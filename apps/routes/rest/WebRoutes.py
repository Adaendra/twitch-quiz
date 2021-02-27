from apps import app, render_template

# Controller to display all web pages.
class WebRoutes(object):

    # Return the index.html of the Vue.js webapp.
    @app.route('/', methods=['GET'])
    def getWebApp():
        return render_template('twitch_quiz_frontend/index.html')
