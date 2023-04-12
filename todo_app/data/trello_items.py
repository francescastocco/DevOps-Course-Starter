import os
import requests
from todo_app.data.item import Item


def get_all_items():
    base_url = f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}/lists'
    query_params = {
        'key': {os.getenv('API_KEY')},
        'token': {os.getenv('API_TOKEN')},
        'cards': 'open'
    }
    response = requests.get(base_url, params = query_params).json()
    return [
        Item.from_trello_card(card, list)
        for list in response
        for card in list['cards']
    ]

def create_item(title):
    base_url = 'https://api.trello.com/1/cards'
    query_params = {
        'key': {os.getenv('API_KEY')},
        'token': {os.getenv('API_TOKEN')},
        'name': title,
        'idList': {os.getenv('TO_DO_LIST_ID')}
    }
    response = requests.post(base_url, data = query_params)
    response.raise_for_status()

def update_item_status(item_id, item_status):
    base_url = f'https://api.trello.com/1/cards/{item_id}'
    list_id = get_next_list_id(item_status)
    query_params = {
        'key': {os.getenv('API_KEY')},
        'token': {os.getenv('API_TOKEN')},
        'idList': list_id
    }
    response = requests.put(base_url, data = query_params)
    response.raise_for_status()

def get_next_list_id(item_status):
    if item_status == str(os.getenv("TO_DO_LIST_ID")):
        return os.getenv("DOING_LIST_ID")
    else:
        return os.getenv("DONE_LIST_ID")
