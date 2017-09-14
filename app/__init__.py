from flask import Flask
from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config.from_object('config')
db = MongoEngine()
db.init_app(app)

toolbar = DebugToolbarExtension(app)

from app import views
