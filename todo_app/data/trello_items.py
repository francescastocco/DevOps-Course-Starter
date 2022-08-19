import os
import requests


def get_board():
    base_url = f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}'
    query_params = {
        "key": {os.getenv("API_KEY")},
        "token": {os.getenv("API_TOKEN")}
    }
    response = requests.get(base_url, params = query_params)
    if (response.status_code == 200):
        return response.json()
