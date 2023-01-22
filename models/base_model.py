#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def _str_(self):
        return "[{}] ({}) {}".format(self._class.name, self.id, self.dict_)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        return_dict = self.__dict__.copy()
        return_dict["__class__"] = self.__class__.__name__
        return_dict["created_at"] = self.created_at.isoformat()
        return_dict["updated_at"] = self.updated_at.isoformat()
        return return_dict


