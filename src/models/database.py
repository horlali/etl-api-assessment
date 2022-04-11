from datetime import datetime
from flask_mongoengine import MongoEngine


db = MongoEngine()

class Data(db.EmbeddedDocument):
    content = db.ListField()


class Etl(db.Document):
    _id = db.SequenceField(primary_key=True)
    file_name = db.StringField()
    file_size = db.DecimalField()
    number_of_rows = db.IntField()
    number_of_columns = db.IntField()
    created_at = db.DateTimeField(default=datetime.now())
    updated_at = db.DateTimeField(default=datetime.now())
    data = db.EmbeddedDocumentField(Data)

    def to_json(self):
        return {
            "_id": self._id,
            "file_name": self.file_name,
            "file_size": self.file_size,
            "number_of_columns": self.number_of_columns,
            "number_of_rows": self.number_of_rows,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "data": self.data
        }



