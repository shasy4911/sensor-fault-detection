import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url  = "mongodb+srv://shashank:4911ssssdsad@cluster0.6kpihcd.mongodb.net/test"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e

#mongodb+srv://avnish:Aa327030@cluster0.or68e.mongodb.net/admin?authSource=admin&replicaSet=atlas-desfdx-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true
#mongodb+srv://shashank:4911ssssdsad@cluster0.6kpihcd.mongodb.net/test