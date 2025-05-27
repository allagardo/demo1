from pydantic import BaseModel as PydanticBaseModel, ValidationError
from pymongo import MongoClient
from datetime import datetime
from uuid import uuid4

client = MongoClient("mongodb://localhost:27017/")
db = client.course  # Подключение к базе данных


class Validation422Exception(Exception):
    pass

class BaseModel:
    scheme = None
    validation = None


    @classmethod
    def get(cls, **kwargs):
        document = {key: value for key, value in kwargs.items()}
        try:
            return list(cls.scheme.find(document))[0]
        except:
            return None


    @classmethod
    def create(cls, **kwargs):
        try:
            cls.validation(**kwargs)
            if not kwargs.get('_id'):
                kwargs['_id'] = str(uuid4())
            document = {key: value for key, value in kwargs.items()}
            document['created_at'] = datetime.now().strftime('%d-%m-%Y %H:%M')
            cls.scheme.insert_one(document)
            return list(cls.scheme.find(document))[0]
        except ValidationError as e:
            print("Validation error:", e)
            raise Validation422Exception(e)
    

    @classmethod
    def find(cls, **kwargs):
        document = {key: value for key, value in kwargs.items()}
        return list(cls.scheme.find(document))
    

    @classmethod
    def update(cls, id: str, **kwargs):
        filter_query = {'_id': id}
        document = {key: value for key, value in kwargs.items()}
        return cls.scheme.update_one(filter_query, {'$set': document})
    

    @classmethod
    def delete(cls, **kwargs):
        document = {key: value for key, value in kwargs.items()}
        return cls.scheme.delete_many(document)


    @classmethod
    def by_date(cls, start_date_timestamp: float, end_date_timestamp: float):
        result = []
        if not start_date_timestamp or not end_date_timestamp:
            return []

        document = {}
        items = list(cls.scheme.find(document))

        for item in items:
            if item.get('created_at'):
                time = datetime.strptime(item['created_at'], '%d-%m-%Y %H:%M').timestamp()
                if start_date_timestamp <= time <= end_date_timestamp:
                    result.append(item)

        return result
