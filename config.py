import os
from app import app
basedir = os.path.abspath(os.path.dirname(__file__))

#app.config['MONGODB_DB'] = 'myfiles'
#app.config['MONGODB_HOST'] = 'localhost'
#app.config['MONGODB_HOST'] = 'ds135574.mlab.com'
#app.config['MONGODB_PORT'] = 32768
#app.config['MONGODB_PORT'] = 35574
#app.config['MONGODB_USERNAME'] = 'emre'
#app.config['MONGODB_PASSWORD'] = 'emre123'

app.config['MONGODB_SETTINGS'] = {
    'db': 'myfiles',
    'host': 'mongodb://emre:emre123@ds135574.mlab.com:35574/myfiles'
}

app.config['DEBUG_TB_PANELS'] = ['flask_mongoengine.panels.MongoDebugPanel']
