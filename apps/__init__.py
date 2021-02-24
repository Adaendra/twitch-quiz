__version__ = '0.1'
from flask import Flask, url_for, render_template, request, Response
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from apps.controllers import *