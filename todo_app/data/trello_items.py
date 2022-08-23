import os
import requests


def get_board():
    base_url = f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}'
    query_params = {
        "key": {os.getenv("API_KEY")},
        "token": {os.getenv("API_TOKEN")}
    }
    response = requests.get(base_url, params = query_params)
    return response.json()

def get_all_cards():
    base_url = f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}/lists'
    query_params = {
        "key": {os.getenv("API_KEY")},
        "token": {os.getenv("API_TOKEN")},
        "cards": "open"
    }
    response = requests.get(base_url, params = query_params)
    return response.json()

def create_card(title):
    base_url = 'https://api.trello.com/1/cards'
    card = {
        "key": {os.getenv("API_KEY")},
        "token": {os.getenv("API_TOKEN")},
        "name": title,
        "idList": {os.getenv("TO_DO_LIST_ID")}
    }
    response = requests.post(base_url, data=card)
    response.raise_for_status()