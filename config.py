import os
from app import app
basedir = os.path.abspath(os.path.dirname(__file__))


app.config['MONGODB_DB'] = 'myFiles'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 32768
app.config['MONGODB_USERNAME'] = 'emre'
app.config['MONGODB_PASSWORD'] = 'emre123'