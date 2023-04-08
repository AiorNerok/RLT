import pymongo as db
from datetime import datetime
from config import Settings

class MongoDBTools:
    __mongod_client = db.MongoClient(
        Settings.MONGODB_URI
    )

    @classmethod
    def get_client(cls):
        return cls.__mongod_client

    @classmethod
    def select_range_collection(cls, from_date: str, to_date: str):
        client = cls.get_client()

        collection = client.RLT.Data
        from_date = str(int(datetime.fromisoformat(from_date).timestamp()*1000))
        to_date = str(int(datetime.fromisoformat(to_date).timestamp()*1000))
        result = collection.find({"dt": {"$gte": from_date, "$lte": to_date}})

        return result
