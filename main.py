import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = { 'Content-type' : 'application/json',
            'trainer_token' : 'TRAINERTOKEN' }
TOKEN = 'f5b5f15c898089e9cf14d3cdb07b8872'
id = 2565
pokemon = 16521


body_create_pokemon = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change_name = {
    "pokemon_id": f'{pokemon}',
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_add_pokeball = {
    "pokemon_id":  f'{pokemon}',
}

response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADERS,  json = body_create_pokemon)
print(response_create_pokemon.text)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADERS,  json = body_change_name)
print(response_change_name.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS,  json = body_add_pokeball)
print(response_add_pokeball.text)