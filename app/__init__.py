from flask import Flask
from flask_mongoengine import MongoEngine
# from flask_debugtoolbar import DebugToolbarExtension
# app.config['DEBUG_TB_PANELS'] = ['flask_mongoengine.panels.MongoDebugPanel']

app = Flask(__name__)

app.config['MONGODB_DB'] = 'myFiles'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 32768
app.config['MONGODB_USERNAME'] = 'emre'
app.config['MONGODB_PASSWORD'] = 'emre123'

# app.config.from_object('config')
db = MongoEngine()
db.init_app(app)

# toolbar = DebugToolbarExtension(app)

from app import views
