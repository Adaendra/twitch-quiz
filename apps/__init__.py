__version__ = '0.1'
from flask import Flask, url_for, render_template, request, Response


app = Flask(__name__)

from apps.controllers import *