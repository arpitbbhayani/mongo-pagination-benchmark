from pymongo import MongoClient


MONGO_HOST = 'localhost'
MONGO_PORT = 2700

client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = client['benchmark']
