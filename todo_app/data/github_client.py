import os
import requests


def get_access_token(auth_code):
    url = 'https://github.com/login/oauth/access_token'
    headers = {
        'Accept': 'application/json'
    }
    data = {
        'client_id': {os.getenv('CLIENT_ID')},
        'client_secret': {os.getenv('CLIENT_SECRET')},
        'code': auth_code,
    }
    response = requests.post(url, headers=headers, data=data)

    if response.status_code != 200:
        return None
    else:
        json_data = response.json()
        return json_data['access_token']

def get_authenticated_github_user(access_token):
    url = f'https://api.github.com/user'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    return response.json()
