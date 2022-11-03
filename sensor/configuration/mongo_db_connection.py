import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
import os
from sensor.constant.env_variable import MONGO_URL_KEY

ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            mongo_db_url = os.getenv("MONGO_URL_KEY")
            if MongoDBClient.client is None:
                print("Inside if block MongoDBClient file")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            print("MongoDBClient Database: ", self.database)
            self.database_name = database_name
            print("MongoDBClient DatabaseName: ", self.database_name)
        except Exception as e:
            raise e

