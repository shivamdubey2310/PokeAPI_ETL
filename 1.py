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

def extraction_1(endpoint):
    file_name = endpoint.replace("-", "_")  # filename for schema files
    
    # Trying to Connect to the endpoint
    print(f"Trying to Connect to the {endpoint} endpoint")
    try:
        initial_response = requests.get(f"https://pokeapi.co/api/v2/{endpoint}/")
        initial_response.raise_for_status()
        total_count = initial_response.json()["count"]

        raw_json = []

        for i in range(1, total_count // 50):
            if i == 1:
                response = requests.get(f"https://pokeapi.co/api/v2/{endpoint}/{int(i)}")
                response.raise_for_status()
                raw_json.append(response.json()) # response in json format

                # Creating schema file for raw json response
                md_file_name = f"raw_json/{file_name}_raw_schema.md"
                helper.json_describe_to_md(response.json(), md_file_name)
            else:
                response = requests.get(f"https://pokeapi.co/api/v2/{endpoint}/{int(i)}")
                response.raise_for_status()
                raw_json.append(response.json()) # response in json format
            time.sleep(0.5) # to avoid rate limits
            
        # Saving raw json 
        json_file_name = f"raw_json/{file_name}_raw.json"
        with open(json_file_name, "w") as file:
            json.dump(raw_json, file)

        # Logging
        print(f"{json_file_name} is saved successfully!!")
    
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred : {http_err}")
    
    except Exception as err:
        print(f"Other error occurred: {err}")

    print(f"Extraction of {endpoint} completed successfully")
    print("------------------------------------------------------\n\n")

# --------------------------------------------------------------------------------------------------------

# Transformation()
def cleaning_pokemon_data():
    
    # loading raw json
    endpoint = "pokemon"
    updated_endpoint = endpoint.replace("-", "_")
    file_name = f"raw_json/{updated_endpoint}_raw.json"
    
    with open(file_name, "r") as file:
        raw_json = json.load(file) 
    
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
                "species_name": raw_json[i]["species"]["name"] if raw_json[i]["species"] else None # Needs further transformation
            }
            list_of_dict1.append(dict1)
        
        # Saving cleaned json
        cleaned_file_name_json = f"cleaned_json/{updated_endpoint}_cleaned.json"
        with open(cleaned_file_name_json, "w") as file:
            json.dump(list_of_dict1, file)

        # Creating schema file for cleaned json response
        with open(cleaned_file_name_json, "r") as file:
            data = json.load(file)
            cleaned_file_name_md = f"cleaned_json/{updated_endpoint}_cleaned_schema.md"
            helper.json_describe_to_md(data[0], cleaned_file_name_md)

# -----------------------------------------------------------------------------------------------

def cleaning_pokemon_species_data():
    # loading raw json
    endpoint = "pokemon-species"
    updated_endpoint = endpoint.replace("-", "_")
    file_name = f"raw_json/{updated_endpoint}_raw.json"
    
    with open(file_name, "r") as file:
        raw_json = json.load(file) 
    
    # selecting only the required fields 
        dict1 = {}
        list_of_dict1 = []

        for i in range(0, len(raw_json)):
            dict1 = {
                "id": raw_json[i]["id"],
                "name": raw_json[i]["name"],
                "base_happiness": raw_json[i]["base_happiness"],
                "capture_rate": raw_json[i]["capture_rate"],
                "gender_rate": raw_json[i]["gender_rate"],
                "hatch_counter": raw_json[i]["hatch_counter"],
                "is_baby": raw_json[i]["is_baby"],
                "is_legendary": raw_json[i]["is_legendary"],
                "is_mythical": raw_json[i]["is_mythical"],
                "evolves_from_species_name": raw_json[i]["evolves_from_species"]["name"] if raw_json[i]["evolves_from_species"] else None, # Needs further transformation
                "growth_rate_name": raw_json[i]["growth_rate"]["name"] if raw_json[i]["growth_rate"] else None,
                "habitat_name": raw_json[i]["habitat"]["name"] if raw_json[i]["habitat"] else None,
                "generation_name": raw_json[i]["generation"]["name"] if raw_json[i]["generation"] else None,
                "shape_name": raw_json[i]["shape"]["name"] if raw_json[i]["shape"] else None,
                "color_name": raw_json[i]["color"]["name"] if raw_json[i]["color"] else None
            }
            list_of_dict1.append(dict1)
        
        # Saving cleaned json
        cleaned_file_name_json = f"cleaned_json/{updated_endpoint}_cleaned.json"
        with open(cleaned_file_name_json, "w") as file:
            json.dump(list_of_dict1, file)
        
        print(f"Data for the {endpoint} endpoint is cleaned!!!")

        # Creating schema file for cleaned json response
        with open(cleaned_file_name_json, "r") as file:
            data = json.load(file)
            cleaned_file_name_md = f"cleaned_json/{updated_endpoint}_cleaned_schema.md"
            helper.json_describe_to_md(data[0], cleaned_file_name_md)

def cleaning_ability_data():
    # loading raw json
    endpoint = "ability"
    updated_endpoint = endpoint.replace("-", "_")
    file_name = f"raw_json/{updated_endpoint}_raw.json"
    
    with open(file_name, "r") as file:
        raw_json = json.load(file) 
    
    # selecting only the required fields 
        dict1 = {}
        list_of_dict1 = []

        for i in range(0, len(raw_json)):
            dict1 = {
                "id": raw_json[i]["id"],
                "name": raw_json[i]["name"],
                "generation_name": raw_json[i]["generation"]["name"] if raw_json[i]["generation"] else None, 
                "is_main_series": raw_json[i]["is_main_series"]
            }
            list_of_dict1.append(dict1)
        
        # Saving cleaned json
        cleaned_file_name_json = f"cleaned_json/{updated_endpoint}_cleaned.json"
        with open(cleaned_file_name_json, "w") as file:
            json.dump(list_of_dict1, file)
        
        print(f"Data for the {endpoint} endpoint is cleaned!!!")

        # Creating schema file for cleaned json response
        with open(cleaned_file_name_json, "r") as file:
            data = json.load(file)
            cleaned_file_name_md = f"cleaned_json/{updated_endpoint}_cleaned_schema.md"
            helper.json_describe_to_md(data[0], cleaned_file_name_md)

# -----------------------------------------------------------------------------------------
def cleaning_pokemon_form_data():
    # loading raw json
    endpoint = "pokemon-form"
    updated_endpoint = endpoint.replace("-", "_")
    file_name = f"raw_json/{updated_endpoint}_raw.json"
    
    with open(file_name, "r") as file:
        raw_json = json.load(file) 
    
    # selecting only the required fields 
        dict1 = {}
        list_of_dict1 = []

        for i in range(0, len(raw_json)):
            dict1 = {
                "id": raw_json[i]["id"],
                "pokemon_name": raw_json[i]["pokemon"]["name"] if raw_json[i]["pokemon"] else None, # Needs further transformation
                "name": raw_json[i]["name"],
                "form_name": raw_json[i]["form_name"],
                "form_order": raw_json[i]["form_order"],
                "is_default": raw_json[i]["is_default"],
                "is_mega": raw_json[i]["is_mega"],
                "is_battle_only": raw_json[i]["is_battle_only"],
                "version_group_name": raw_json[i]["version_group"]["name"] if raw_json[i]["version_group"] else None
            }
            list_of_dict1.append(dict1)
        
        # Saving cleaned json
        cleaned_file_name_json = f"cleaned_json/{updated_endpoint}_cleaned.json"
        with open(cleaned_file_name_json, "w") as file:
            json.dump(list_of_dict1, file)
        
        print(f"Data for the {endpoint} endpoint is cleaned!!!")

        # Creating schema file for cleaned json response
        with open(cleaned_file_name_json, "r") as file:
            data = json.load(file)
            cleaned_file_name_md = f"cleaned_json/{updated_endpoint}_cleaned_schema.md"
            helper.json_describe_to_md(data[0], cleaned_file_name_md)

# ---------------------------------------------------------------------------------------------
def cleaning_type_data():
    # loading raw json
    endpoint = "type"
    updated_endpoint = endpoint.replace("-", "_")
    file_name = f"raw_json/{updated_endpoint}_raw.json"
    
    with open(file_name, "r") as file:
        raw_json = json.load(file) 
    
    # selecting only the required fields 
        dict1 = {}
        list_of_dict1 = []

        for i in range(0, len(raw_json)):
            dict1 = {
                "id": raw_json[i]["id"],
                "name": raw_json[i]["name"],
                "generation": raw_json[i]["generation"]["name"] if raw_json[i]["generation"] else None
            }
            list_of_dict1.append(dict1)
        
        # Saving cleaned json
        cleaned_file_name_json = f"cleaned_json/{updated_endpoint}_cleaned.json"
        with open(cleaned_file_name_json, "w") as file:
            json.dump(list_of_dict1, file)

        print(f"Data for the {endpoint} endpoint is cleaned!!!")

        # Creating schema file for cleaned json response
        with open(cleaned_file_name_json, "r") as file:
            data = json.load(file)
            cleaned_file_name_md = f"cleaned_json/{updated_endpoint}_cleaned_schema.md"
            helper.json_describe_to_md(data[0], cleaned_file_name_md)

# ------------------------------------------------------------------------------------------

def creating_ids(name_file, id_file, name_col, id_col):
    with open(name_file, "r") as file:
        df1 = pd.read_json(file)

    with open(id_file, "r") as file:
        df2 = pd.read_json(file)

    # getting the required columns
    new_df1 = df1[name_col]
    new_df2 = df2[id_col]

    # Merging it into a single df
    concat_df = pd.concat([new_df1, new_df2], axis=1)

    # resetting index and converting into a dict
    name_to_id = concat_df.set_index(name_col)[id_col].to_dict()

    # Mapping the dictionary
    df1[name_col] = df1[name_col].map(name_to_id)
    
    # Renaming the column
    new_name = name_col.replace("_name", "_id")
    df1 = df1.rename(columns = {name_col: new_name})

    # Removing the null (NaN) values
    df1[new_name] = df1[new_name].fillna(0)

    # Changing the datatype to int from float
    df1[new_name] = df1[new_name].astype('Int64')
    
    # Saving the dataFrame in json
    with open(name_file, "w") as file:
        df1.to_json(file)

# ---------------------------------------------------------------------------------------

def data_cleaning():
    # cleaning_pokemon_data()
    # cleaning_pokemon_species_data()
    # cleaning_ability_data()
    # cleaning_pokemon_form_data()
    # cleaning_type_data()
    pass

# ------------------------------------------------------------------------------------------

def extra_jsons():
    # Creating pokemon_ability table
    pokemon_df = pd.read_json("cleaned_json/pokemon_cleaned.json")
    ability_df = pd.read_json("cleaned_json/ability_cleaned.json")

    # Merging the dataframes
    print(pokemon_df)
    print(ability_df)

# ==========================================================================================
def transform():
    # Function to clean the data
    # data_cleaning()
    
    # Function to create ids from names
    # creating_ids("cleaned_json/pokemon_cleaned.json", "cleaned_json/pokemon_species_cleaned.json", "species_name", "id")
    # creating_ids("cleaned_json/pokemon_species_cleaned.json", "cleaned_json/pokemon_species_cleaned.json", "evolves_from_species_name", "id")
    # creating_ids("cleaned_json/pokemon_form_cleaned.json", "cleaned_json/pokemon_cleaned.json", "pokemon_name", "id")
    
    # Function to create extra jsons for database according to schema
    extra_jsons()
    
def extraction():
    endpointList = ["pokemon", "pokemon-species", "ability", "pokemon-form", "type"]
    for endpoint in endpointList:
        extraction_1(endpoint)

# extraction()

transform()
