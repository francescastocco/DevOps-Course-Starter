import os
import pymongo

from todo_app.data.item import Item

def get_collection():
    client = pymongo.MongoClient(f'{os.getenv("DATABASE_CONNECTION_STRING")}')
    db = client[f'{os.getenv("DATABASE_NAME")}']
    return db.items

def get_all_items():
    collection = get_collection()
    items = []
    for item in collection.find():
        items.append(Item.from_database(item))
    return items

def create_item(title):
    collection = get_collection()
    item = {
        "name": title,
        "status": "To Do"
    }
    collection.insert_one(item).inserted_id

def update_item_status(item_id, item_status):
    collection = get_collection()
    new_status = get_next_status(item_status)
    collection.update_one({'_id': item_id}, {'$set': {'status': new_status}})

def delete_item(item_id):
    collection = get_collection()
    collection.delete_one({'_id': item_id})

def get_next_status(item_status):
    print(item_status)
    if item_status == 'To':
        return 'Doing'
    else:
        return 'Done'
