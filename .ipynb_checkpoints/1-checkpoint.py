# pokemon 
# Pokemon species
# ability
# pokemon forms
# pokemon type

import requests
import json

# Extracting pokemon data
def extract_pokemon():

    # Trying to Connect to the "pokemon" endpoint
    print("Trying to Connect to the \"pokemon\" endpoint")
    try:
        initial_response = requests.get("https://pokeapi.co/api/v2/pokemon/")
        initial_response.raise_for_status()
        total_pokemon_count = initial_response.json()["count"]

        for i in range(1, total_pokemon_count//500):
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{int(i)}")
            dictt = {"Pokemon_id":response.json}
            dictt = json.loads(json.dumps(response.json()["id"])) # [""]))
            print(dictt)

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred : {http_err}")
    
    except Exception as err:
        print(f"Other error occurred: {err}")
    
    else:
        print("Successfully connected!")

# -----------------------------------------------------------------------------------------------------
# Extracting species data

def extract_Species()







def extraction():
    extract_pokemon()

extraction()