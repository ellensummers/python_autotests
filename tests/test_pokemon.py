import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'TRAINERTOKEN'
id = 2565

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : id})
    assert response.json()['data'][0]['trainer_name'] == 'Ария'
