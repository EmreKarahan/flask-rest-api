from app import db
import datetime


class Items(db.Document):
    title = db.StringField(max_length=120)
    url = db.URLField()
    gsm = db.StringField()
    age = db.IntField()
    price = db.IntField()
    isBackdoor = db.BooleanField(default=False)
    isFavorite = db.BooleanField(default=False)
    callCount = db.IntField(default=0)
    lastCallDate = db.DateTimeField(default=None)
    location = db.StringField()
    status = db.IntField()
    statusname = db.StringField()
    pub_date = db.DateTimeField(default=datetime.datetime.now)
