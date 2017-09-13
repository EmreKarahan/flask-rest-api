from app import db
import datetime


class Items(db.Document):
    title = db.StringField(max_length=120)
    url = db.URLField()
    gsm = db.StringField()
    age = db.IntField()
    price = db.IntField()
    is_backdoor = db.BooleanField(default=False)
    location = db.StringFied()
    status = db.IntField()
    pub_date = db.DateTimeField(default=datetime.datetime.now)
