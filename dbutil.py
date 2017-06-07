from pymongo import MongoClient


MONGO_HOST = 'localhost'
MONGO_PORT = 27017

client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = client['benchmark']
