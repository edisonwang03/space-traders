import requests
import os
from dotenv import load_dotenv


def register_player(callsign, faction):
    url = 'https://api.spacetraders.io/v2/register'
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'symbol': callsign,
        'faction': faction,
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def get_agent(token):
    url = 'https://api.spacetraders.io/v2/my/agent'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(token),
    }
    
    response = requests.get(url, headers=headers)
    return response.json()

def get_waypoint(token, system, waypoint):
    url = 'https://api.spacetraders.io/v2/systems/{}/waypoints/{}'.format(system, waypoint)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(token),
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_contracts(token):
    url = 'https://api.spacetraders.io/v2/my/contracts'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(token),
    }
    response = requests.get(url, headers=headers)
    return response.json()

def accept_contract(token, contract_id):
    url = 'https://api.spacetraders.io/v2/my/contracts/{}/accept'.format(contract_id)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(token),
    }
    response = requests.post(url, headers=headers)
    return response.json()


if __name__ == '__main__':
    load_dotenv()
    callsign = os.getenv('CALLSIGN')
    faction = os.getenv('FACTION')
    token = os.getenv('API-ACCESS-TOKEN')
    response = accept_contract(token, 'cljx8d1coee4js60ck89clj3q')
    print(response)