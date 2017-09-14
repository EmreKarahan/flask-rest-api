from app import db
import datetime


class Images(db.Document):
    path = db.StringField(max_length=60)
    pub_date = db.DateTimeField(default=datetime.datetime.now)


def __str__(self):
    return '<Images %r>' % (self.path)


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
    status = db.IntField(default=1)
    pub_date = db.DateTimeField(default=datetime.datetime.now)
    images = db.ListField(db.ReferenceField(Images))


def __str__(self):
    return '<Images %r>' % (self.title)
