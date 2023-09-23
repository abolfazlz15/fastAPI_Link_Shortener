from pymongo.mongo_client import MongoClient
from decouple import config


clinet = MongoClient(config('DB_ADDRESS'))

db = clinet.link_shortener
collection_name = db['link_collection']