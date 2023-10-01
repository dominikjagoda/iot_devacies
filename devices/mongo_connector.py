import pymongo

def insert_json_to_mongodb(json_data, mongo_uri, database_name, collection_name):
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[database_name]

        # Insert the authentication credentials in the MongoDB URI
        # Example: mongodb://username:password@localhost:27017/
        collection = db[collection_name]
        collection.insert_one(json_data)
        print("JSON data inserted into MongoDB successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()