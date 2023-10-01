from pymongo.mongo_client import MongoClient
from dataclasses import dataclass


MONGO_URI = "mongodb://root:examplePassword@localhost:27017/"


@dataclass
class MongoDBConnector:
    mongo_uri: str
    database_name: str
    collection_name: str
    db_client: MongoClient = MongoClient(mongo_uri)

    def insert_json_to_mongodb(
        self, db_client, database_name, collection_name, json_data: dict
    ):
        try:
            db = db_client[database_name]

            # Insert the authentication credentials in the MongoDB URI
            # Example: mongodb://username:password@localhost:27017/
            collection = db[collection_name]
            collection.insert_one(json_data)
            print("JSON data inserted into MongoDB successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            db_client.close()
