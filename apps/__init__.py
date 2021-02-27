__version__ = '0.1'
from flask import Flask, url_for, render_template, request, Response
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f06080df-5d2c-4c14-a97f-b6a832946d2f'
socketio = SocketIO(app)

# Import all routes
from apps.rest_routes import *
from apps.socket_routes import *