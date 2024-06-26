import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a7602ec6c887d78ef2ca53ce4fc3a380'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 4285



def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()["data"][0]["trainer_name"] == 'Elena'