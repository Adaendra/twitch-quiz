__version__ = '0.1'
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f06080df-5d2c-4c14-a97f-b6a832946d2f'
socketio = SocketIO(app)

# Import all routes
from apps.routes.rest import *
from apps.routes.socket import *