from app import db
import datetime
from .items import Items


class Images(db.Document):
    path = db.StringField(max_length=60)
    item = db.ReferenceField(Items)
    pub_date = db.DateTimeField(default=datetime.datetime.now)


def __str__(self):
    return '<Images %r>' % (self.title)
