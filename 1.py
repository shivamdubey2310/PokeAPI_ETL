# pokemon https://pokeapi.co/api/v2/pokemon/{id or name}/ 
# Pokemon species https://pokeapi.co/api/v2/pokemon-species/{id or name}/
# ability https://pokeapi.co/api/v2/ability/{id or name}/
# pokemon forms https://pokeapi.co/api/v2/pokemon-form/{id or name}/
# pokemon type https://pokeapi.co/api/v2/type/{id or name}/

import requests
import json
import pandas as pd
import sqlalchemy as sal
import helperFunctions.json_explorer as helper
import time

# Extracting pokemon data
def extract_pokemon():

    # Trying to Connect to the "pokemon" endpoint
    print("Trying to Connect to the \"pokemon\" endpoint")
    try:
        initial_response = requests.get("https://pokeapi.co/api/v2/pokemon/")
        initial_response.raise_for_status()
        total_pokemon_count = initial_response.json()["count"]

        raw_json = []

        for i in range(1, total_pokemon_count // 200):
            if i == 1:
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{int(i)}")
                response.raise_for_status()
                raw_json.append(response.json()) # response in json format

                # Creating schema file for raw json response
                file_name = "pokemon_raw_schema.md"
                helper.json_describe_to_md(response.json(), file_name)
            else:
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{int(i)}")
                response.raise_for_status()
                raw_json.append(response.json()) # response in json format
            
            time.sleep(0.5)
            
        # Saving raw json 
        with open("pokemon_raw.json", "w") as file:
            json.dump(raw_json, file)
        
        # selecting only the required fields 
        dict1 = {}
        list_of_dict1 = []

        for i in range(0, len(raw_json)):
            dict1 = {
                "id": raw_json[i]["id"],
                "name": raw_json[i]["name"],
                "base_experience": raw_json[i]["base_experience"],
                "height": raw_json[i]["height"],
                "weight": raw_json[i]["weight"],
                "is_default": raw_json[i]["is_default"],
                "order": raw_json[i]["order"],
                "species_name": raw_json[i]["species"]["name"]
            }
            list_of_dict1.append(dict1)

        # Saving cleaned json
        with open("pokemon_cleaned.json", "w") as file:
            json.dump(list_of_dict1, file)

        # Creating schema file for cleaned json response
        with open("pokemon_cleaned.json", "r") as file:
            data = json.load(file)
            file_name = "pokemon_cleaned_schema.md"
            helper.json_describe_to_md(data[0], file_name)

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred : {http_err}")
    
    except Exception as err:
        print(f"Other error occurred: {err}")

# -----------------------------------------------------------------------------------------------------
# Extracting species data

def extract_species():
    # Trying to Connect to the "species" endpoint
    print("Trying to Connect to the \"species\" endpoint")
    try:
        initial_response = requests.get("https://pokeapi.co/api/v2/pokemon-species")
        initial_response.raise_for_status()
        total_species_count = initial_response.json()["count"]

        species_json_response = []

        for i in range(1, total_species_count // 500):
            if i == 1:
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{int(i)}")
                response.raise_for_status()
                species_json_response.append(response.json())
                
                # Creating schema file for json response
                file_name = "species_json_schema.md"
                helper.json_describe_to_md(response.json(), file_name)
            
            # response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{int(i)}")
            # response.raise_for_status()
            # species_json_response.append(response.json())

            # Saving response in json()
            # with open("species_data.json", "w") as file:
            #     json.dump(species_json_response, file)

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred : {http_err}")
    
    except Exception as err:
        print(f"Other error occurred: {err}")
    
# ----------------------------------------------------------------------------------------------

# Extracting abilities data
def extract_ability():
    # Trying to Connect to the "ability" endpoint
    print("Trying to Connect to the \"ability\" endpoint")
    try:
        initial_response = requests.get("https://pokeapi.co/api/v2/ability")
        initial_response.raise_for_status()
        total_species_count = initial_response.json()["count"]

        ability_json_response = []
        
        for i in range(1, total_species_count // 50):
            if i == 1:
                response = requests.get(f"https://pokeapi.co/api/v2/ability/{int(i)}")
                response.raise_for_status()
                ability_json_response.append(response.json())
                
                # Creating schema file for json response
                file_name = "ability_json_schema.md"
                helper.json_describe_to_md(response.json(), file_name)
            
            # response = requests.get(f"https://pokeapi.co/api/v2/ability/{int(i)}")
            # response.raise_for_status()
            # ability_json_response.append(response.json())

            # Saving response in json()
            # with open("ability_data.json", "w") as file:
            #     json.dump(ability_json_response, file)

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred : {http_err}")
    
    except Exception as err:
        print(f"Other error occurred: {err}")
    
# ----------------------------------------------------------------------------------------------

# Extracting pokemon-form data
def extract_form():
    # Trying to Connect to the "pokemon-form" endpoint
    print("Trying to Connect to the \"pokemon-form\" endpoint")
    try:
        initial_response = requests.get("https://pokeapi.co/api/v2/pokemon-form")
        initial_response.raise_for_status()
        total_species_count = initial_response.json()["count"]

        form_json_response = []

        for i in range(1, total_species_count // 500):
            if i == 1:
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon-form/{int(i)}")
                response.raise_for_status()
                form_json_response.append(response.json())
                
                # Creating schema file for json response
                file_name = "form_json_schema.md"
                helper.json_describe_to_md(response.json(), file_name)
            
            # response = requests.get(f"https://pokeapi.co/api/v2/pokemon-form/{int(i)}")
            # response.raise_for_status()
            # form_json_response.append(response.json())
            
            # Saving response in json()
            # with open("form_data.json", "w") as file:
            #     json.dump(form_json_response, file)

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred : {http_err}")
    
    except Exception as err:
        print(f"Other error occurred: {err}")
    
# ----------------------------------------------------------------------------------------------

# Extracting type data
def extract_type():
    # Trying to Connect to the "type" endpoint
    print("Trying to Connect to the \"type\" endpoint")
    try:
        initial_response = requests.get("https://pokeapi.co/api/v2/type")
        initial_response.raise_for_status()
        total_species_count = initial_response.json()["count"]
        
        type_json_response = []

        for i in range(1, total_species_count // 5):
            if i == 1:
                response = requests.get(f"https://pokeapi.co/api/v2/type/{int(i)}")
                response.raise_for_status()
                type_json_response.append(response.json())
                
                # Creating schema file for json response
                file_name = "type_json_schema.md"
                helper.json_describe_to_md(response.json(), file_name)
            
            # response = requests.get(f"https://pokeapi.co/api/v2/type/{int(i)}")
            # response.raise_for_status()
            # type_json_response.append(response.json())

            # Saving response in json()
            with open("type.json", "w") as file:
                json.dump(type_json_response, file)

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred : {http_err}")
    
    except Exception as err:
        print(f"Other error occurred: {err}")

# ------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------

# Transformation()

def initial_transformation():
    df = pd.read_json("pokemon_cleaned.json")
    print(df)

def transform():
    initial_transformation()


def extraction():
    extract_pokemon()
    # extract_species()
    # extract_ability()
    # extract_form()
    # extract_type()

extraction()
transform()