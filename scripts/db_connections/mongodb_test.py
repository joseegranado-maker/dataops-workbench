from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["demo"]
collection = db["healthcheck"]
collection.insert_one({"status": "ok"})
print(collection.find_one({"status": "ok"}))
