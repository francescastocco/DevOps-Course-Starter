import os
import pymongo

from todo_app.data.item import Item

def get_db():
    client = pymongo.MongoClient(f'{os.getenv("DATABASE_CONNECTION_STRING")}')
    return client[f'{os.getenv("DATABASE_NAME")}']

def get_all_items():
    db = get_db()
    collection =  db.items
    items = []
    for item in collection.find():
        items.append(Item.from_database(item))
    return items

def create_item(title):
    db = get_db()
    items = db.items
    item = {
        "name": title,
        "status": "To Do"
    }
    items.insert_one(item).inserted_id

def update_item_status(item_id, item_status):
    db = get_db()
    items = db.items
    new_status = get_next_status(item_status)
    items.update_one({'_id': item_id}, {'$set': {'status': new_status}})

def delete_item(item_id):
    db = get_db()
    items = db.items
    items.delete_one({'_id': item_id})

def get_next_status(item_status):
    print(item_status)
    if item_status == 'To':
        return 'Doing'
    else:
        return 'Done'
