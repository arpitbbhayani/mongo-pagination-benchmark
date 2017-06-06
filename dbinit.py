from dbutil import db


def init_collection():
    collection_name = 'students'
    # Drops the collection
    db.drop_collection(collection_name)
    # Creates a new collection with no index
    db.create_collection(collection_name)
