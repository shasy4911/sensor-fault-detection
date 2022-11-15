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
            #mongo_db_url = os.getenv("MONGO_URL_KEY")
            mongo_db_url = "mongodb+srv://<UserName>:<Password>@cluster0.6kpihcd.mongodb.net/?retryWrites=true&w=majority"
            if MongoDBClient.client is None:
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e

