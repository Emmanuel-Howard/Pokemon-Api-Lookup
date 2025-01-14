# A pokémon search program connected to a pokémon API

# Import requests module
import requests

base_url = "https://pokeapi.co/api/v2/"   # Provide base_url of the API database

# Function that gets info from API by making a request to the url
def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

# If response code = 200 (ok), then return data in .json format
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else: # Print error status code
        print(f"Failed to retrieve data: {response.status_code}")

# Prompt User for pokémon input
pokemon_name = input("What pokemon would you like to look up?: ").lower().strip()

# Passes name into get_pokemon_info and returns pokemon_info
pokemon_info = get_pokemon_info(pokemon_name)

# "IF" handles API error and catches TypeError
if pokemon_info: # Print pokémon info
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

# Loops through each ability dictionary in the abilities list + returns name
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    print(f"Abilities: {', '.join(abilities)}")   # Joins the abilities to a string
