from apps import app, render_template


class Home(object):

    @app.route('/', methods=['GET', 'POST'])
    def Home():
        return render_template('twitch_quiz_frontend/index.html')
