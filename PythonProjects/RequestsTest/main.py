import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a7602ec6c887d78ef2ca53ce4fc3a380'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
body_pokemons = {
    "name": "Pokemons",
    "photo_id": 2
}

body_name = {
    "pokemon_id": "36646",
    "name": "Newpok",
    "photo_id": 2
}


body_pokeball = {
    "pokemon_id": "36646"
}

respons_pokemons = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(respons_pokemons.text)

message = respons_pokemons.json()['message']
print(message)

respons_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(respons_name.text)

respons_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(respons_pokeball.text)