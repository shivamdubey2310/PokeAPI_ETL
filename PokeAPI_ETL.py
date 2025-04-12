# Astro CLI is not used... Airflow is used directly.
# Extraction is done for a small data.

import requests
import json
import pandas as pd
import sqlalchemy as sal
import helperFunctions.json_explorer as helper
import time
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# To import all .env variables
from dotenv import load_dotenv
load_dotenv()


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
    print("\n")

# --------------------------------------------------------------------------------------------------------

# Transformation()
def cleaning_pokemon_data():    
    # loading raw json
    endpoint = "pokemon"
    print(f"!!!Cleaning {endpoint} data...")

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

        print(f"Data for the {endpoint} endpoint is cleaned!!!")

        # Creating schema file for cleaned json response
        with open(cleaned_file_name_json, "r") as file:
            data = json.load(file)
            cleaned_file_name_md = f"cleaned_json/{updated_endpoint}_cleaned_schema.md"
            helper.json_describe_to_md(data[0], cleaned_file_name_md)

# -----------------------------------------------------------------------------------------------

def cleaning_pokemon_species_data():
    # loading raw json
    endpoint = "pokemon-species"
    print(f"!!!Cleaning {endpoint} data...")
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

# -----------------------------------------------------------------------------------------------

def cleaning_ability_data():
    # loading raw json
    endpoint = "ability"
    print(f"!!!Cleaning {endpoint} data...")

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
    print(f"!!!Cleaning {endpoint} data...")

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
                "form_name": raw_json[i]["name"],
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
    print(f"!!!Cleaning {endpoint} data...")

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
    print(f"\nConverting names to ids for {name_file} : {name_col}")
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

    print(f"names to ids for {name_file} : {name_col} Converted successfully")

# ---------------------------------------------------------------------------------------
def creating_pokemon_ability_table():
    # Creating pokemon_ability table
    print("Creating pokemon_ability table")
    
    with open("raw_json/pokemon_raw.json", "r") as file:
        raw_pokemon_json = json.load(file)

     # selecting only the required fields 
        dict1 = {}
        list_of_dict1 = []

        for i in range(0, len(raw_pokemon_json) - 1):
            dict1 = {
                "pokemon_id": raw_pokemon_json[i]["id"],
                "ability_name": raw_pokemon_json[i]["abilities"][0]["ability"]["name"] if raw_pokemon_json[i]["abilities"][0]["ability"] else None, # Needs further transformation
                "is_hidden": raw_pokemon_json[i]["abilities"][0]["is_hidden"],
                "slot": raw_pokemon_json[i]["abilities"][0]["slot"]
            }
            list_of_dict1.append(dict1)
        
        # Saving cleaned json
        cleaned_file_name_json = f"cleaned_json/pokemon_ability_cleaned.json"
        with open(cleaned_file_name_json, "w") as file:
            json.dump(list_of_dict1, file)

        print(f"Data for the pokemon_ability table is created!!!")

        # Creating schema file for cleaned json response
        with open(cleaned_file_name_json, "r") as file:
            data = json.load(file)
            cleaned_file_name_md = f"cleaned_json/pokemon_ability_cleaned_schema.md"
            helper.json_describe_to_md(data[0], cleaned_file_name_md)

# ------------------------------------------------------------------------------------------------------

def creating_pokemon_type_table():
    # Creating pokemon_type table
    print("Creating pokemon_type table")
    with open("raw_json/pokemon_raw.json", "r") as file:
        raw_pokemon_json = json.load(file)

     # selecting only the required fields 
        dict1 = {}
        list_of_dict1 = []

        for i in range(0, len(raw_pokemon_json) - 1):
            dict1 = {
                "pokemon_id": raw_pokemon_json[i]["id"],
                "type_name": raw_pokemon_json[i]["types"][0]["type"]["name"] if raw_pokemon_json[i]["types"][0]["type"] else None, # Needs further transformation
                "slot": raw_pokemon_json[i]["types"][0]["slot"]
            }
            list_of_dict1.append(dict1)
        
        # Saving cleaned json
        cleaned_file_name_json = f"cleaned_json/pokemon_types_cleaned.json"
        with open(cleaned_file_name_json, "w") as file:
            json.dump(list_of_dict1, file)

        print(f"Data for the pokemon_ability table is created!!!")

        # Creating schema file for cleaned json response
        with open(cleaned_file_name_json, "r") as file:
            data = json.load(file)
            cleaned_file_name_md = f"cleaned_json/pokemon_types_cleaned_schema.md"
            helper.json_describe_to_md(data[0], cleaned_file_name_md)

# ----------------------------------------------------------------------------------------
def count_missing_values(file_name):
    print(f"\nCounting missing values for {file_name}")

    df = pd.read_json(f"cleaned_json/{file_name}_cleaned.json")
    column_names = df.columns
    count_dict = {}
    missing_value_count = {}

    for column in column_names:
        count = df[column].isna().sum()
        count_dict[column] = count
    
    # Generating missing_Value count dictionary 
    missing_value_count = {column: count for column, count in count_dict.items() if count != 0}
    
    # printing the dictionary of missing values
    if missing_value_count is {}:
        print(f"Count of Missing values in {file_name} : {count_dict}\n\n")
    else:
        print(f"No missing values in {file_name}! ")

# ----------------------------------------------------------------------------------------
def create_extra_tables():
    creating_pokemon_ability_table()
    print("\n")
    creating_pokemon_type_table()
    print("\n")

# -----------------------------------------------------------------------------------------------------
def data_cleaning():
    cleaning_pokemon_data()
    print("\n")
    cleaning_pokemon_species_data()
    print("\n")
    cleaning_ability_data()
    print("\n")
    cleaning_pokemon_form_data()
    print("\n")
    cleaning_type_data()
    print("\n")

# ------------------------------------------------------------------------------------------

def detecting_missing_values():
    file_names = ["pokemon", "pokemon_species", "ability", "pokemon_form", "type", "pokemon_ability", "pokemon_types"]    

    for name in file_names:
        count_missing_values(name)

# -------------------------------------------------------------------------------------------
def creating_database(db_name): 
    # Getting Mysql credentials from .env
    MySQL_User = os.getenv("MySQL_User")
    MySQL_Pass = os.getenv("MySQL_Pass")
    MySQL_Host = os.getenv("MySQL_Host")
    print("Connecting to Mysql")

    engine = sal.create_engine(f"mysql+pymysql://{MySQL_User}:{MySQL_Pass}@{MySQL_Host}", echo=True)
    
    with engine.connect() as connection:
        connection.execute(sal.text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        result = connection.execute("SHOW DATABASES")
        for db in result:
            if db[0] == db_name:
                print(f"___Database {db_name} created successfully____")
            break
        else:
            print(f"Error in creating {db_name}")

# ------------------------------------------------------------------------------------------

def creating_tables(db_name):
    # Getting Mysql credentials from .env
    MySQL_User = os.getenv("MySQL_User")
    MySQL_Pass = os.getenv("MySQL_Pass")
    MySQL_Host = os.getenv("MySQL_Host")
    print("Connecting to Mysql")

    engine = sal.create_engine(f"mysql+pymysql://{MySQL_User}:{MySQL_Pass}@{MySQL_Host}/{db_name}", echo=True)
    
    table_list = ["pokemon_species", "pokemon", "ability", "pokemon_ability", "pokemon_form", "type", "pokemon_types"]
    table_count = 0

    with engine.connect() as connection:
        query_list = [
                        """
                        CREATE TABLE pokemon_species (
                            id INT PRIMARY KEY,
                            name VARCHAR(100),
                            base_happiness INT,
                            capture_rate INT,
                            gender_rate INT,
                            hatch_counter INT,
                            is_baby BOOLEAN,
                            is_legendary BOOLEAN,
                            is_mythical BOOLEAN,
                            evolves_from_species_id INT,
                            growth_rate_name VARCHAR(50),
                            habitat_name VARCHAR(50),
                            generation_name VARCHAR(50),
                            shape_name VARCHAR(50),
                            color_name VARCHAR(50),
                            FOREIGN KEY (evolves_from_species_id) REFERENCES pokemon_species(id)
                        )
                        """,
                        
                        """
                        CREATE TABLE pokemon (
                            id INT PRIMARY KEY,
                            name VARCHAR(100),
                            base_experience INT,
                            height INT,
                            weight INT,
                            is_default BOOLEAN,
                            `order` INT,
                            species_id INT,
                            FOREIGN KEY (species_id) REFERENCES pokemon_species(id)
                        )
                        """,

                        """
                        CREATE TABLE ability (
                            id INT PRIMARY KEY,
                            name VARCHAR(100),
                            generation_name VARCHAR(50),
                            is_main_series BOOLEAN
                        )
                        """,

                        """
                        CREATE TABLE pokemon_ability (
                            pokemon_id INT,
                            ability_id INT,
                            is_hidden BOOLEAN,
                            slot INT,
                            PRIMARY KEY (pokemon_id, ability_id),
                            FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
                            FOREIGN KEY (ability_id) REFERENCES ability(id)
                        )
                        """,

                        """
                        CREATE TABLE pokemon_form (
                            id INT PRIMARY KEY,
                            pokemon_id INT,
                            name VARCHAR(100),
                            form_name VARCHAR(100),
                            form_order INT,
                            is_default BOOLEAN,
                            is_mega BOOLEAN,
                            is_battle_only BOOLEAN,
                            version_group_name VARCHAR(50),
                            FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
                        )
                        """,

                        """
                        CREATE TABLE type (
                            id INT PRIMARY KEY,
                            name VARCHAR(50),
                            generation VARCHAR(50)
                        )
                        """,

                        """
                        CREATE TABLE pokemon_types (
                            pokemon_id INT,
                            type_id INT,
                            slot INT,
                            PRIMARY KEY (pokemon_id, type_id),
                            FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
                            FOREIGN KEY (type_id) REFERENCES type(id)
                        )
                        """ ]
        
        for table_name, query in zip(table_list, query_list):
            try:
                connection.execute(sal.text(query))
            except Exception as err:
                print(f"Error creating table '{table_name}': {err}")
            else:
                print(f"Successfully created table '{table_name}'")

        
        # Verifying table creation
        query = "SHOW TABLES ;"
        result = connection.execute(sal.text(query))

        db_table_list = []

        for table_name in result:
            db_table_list.append(table_name[0])
        
        for table in table_list:
            if table in db_table_list:
                print(f"Table {table} created successfully!!!")
            else:
                print(f"Table {table} is not created due to any error.")
                exit(0)
        
        print("\n___All the tables are created successfully___")  
# ---------------------------------------------------------------------------------------------


def schema_design(database_name):
    creating_database(database_name)
    print("\n")
    print("--" * 40)
    creating_tables(database_name)
    print("\n")
    print("--" * 40)

def loading_data(db_name):
    files_list = ["pokemon_species", "pokemon", "ability", "pokemon_ability", "pokemon_form", "type", "pokemon_types"]

    table_list = ["pokemon_species", "pokemon", "ability", "pokemon_ability", "pokemon_form", "type", "pokemon_types"]

    # Appending "cleaned_json/" in file names
    for i in range(len(files_list)):
        files_list[i] = f"cleaned_json/{files_list[i]}_cleaned.json"
    
    # Loading jsons into df
    pokemon_species_df = pd.read_json(files_list[0])
    pokemon_df = pd.read_json(files_list[1])
    ability_df = pd.read_json(files_list[2])
    pokemon_ability_df = pd.read_json(files_list[3])
    pokemon_form_df = pd.read_json(files_list[4])
    type_df = pd.read_json(files_list[5])
    pokemon_types_df = pd.read_json(files_list[6])
    

    # Establishing connection to database
    MySQL_User = os.getenv("MySQL_User")
    MySQL_Pass = os.getenv("MySQL_Pass")
    MySQL_Host = os.getenv("MySQL_Host")
    print("Connecting to Mysql")

    engine = sal.create_engine(f"mysql+pymysql://{MySQL_User}:{MySQL_Pass}@{MySQL_Host}/{db_name}", echo=True)

    with engine.begin() as connection:
        connection.execute(sal.text("SET FOREIGN_KEY_CHECKS = 0;"))
        pokemon_species_df.to_sql(table_list[0], connection, if_exists="append", index=False)
        pokemon_df.to_sql(table_list[1], connection, if_exists="append", index=False)
        ability_df.to_sql(table_list[2], connection, if_exists="append", index=False)
        pokemon_ability_df.to_sql(table_list[3], connection, if_exists="append", index=False)
        pokemon_form_df.to_sql(table_list[4], connection, if_exists="append", index=False)
        type_df.to_sql(table_list[5], connection, if_exists="append", index=False)
        pokemon_types_df.to_sql(table_list[6], connection, if_exists="append", index=False)
        connection.execute(sal.text("SET FOREIGN_KEY_CHECKS = 0;"))

        # Verification
        for table in table_list:
            query = f"SELECT * FROM {table} LIMIT 10;"
            result = connection.execute(sal.text(query))
            first_row = result.fetchone() # Fetching the first row
            
            if first_row is None:
                print(f"{table} is empty!!!")
            else:
                print(f"{table} loaded successfully!!!")

        print("\n\nData Loading successful!!!")

# ==========================================================================================

def load():
    database_name = "PokeAPI_17"
    schema_design(database_name)
    loading_data(database_name)

def transform():
    # Function to clean the data
    data_cleaning()
    
    print("_____Data cleaning is successful!!_____\n")
    print("--" * 40)

    # Function to create ids from names
    creating_ids("cleaned_json/pokemon_cleaned.json", "cleaned_json/pokemon_species_cleaned.json", "species_name", "id")
    creating_ids("cleaned_json/pokemon_species_cleaned.json", "cleaned_json/pokemon_species_cleaned.json", "evolves_from_species_name", "id")
    creating_ids("cleaned_json/pokemon_form_cleaned.json", "cleaned_json/pokemon_cleaned.json", "pokemon_name", "id")
    
    print("_____Name to Id conversion is successful!!_____\n")
    print("--" * 40)
    
    # # Function to create extra jsons for database according to schema
    create_extra_tables()
    
    print("_____Extra table creation is successful!!!_____\n")
    print("--" * 40)

    # # Function to create ids from names 
    creating_ids("cleaned_json/pokemon_ability_cleaned.json", "cleaned_json/ability_cleaned.json", "ability_name", "id")
    creating_ids("cleaned_json/pokemon_types_cleaned.json", "cleaned_json/type_cleaned.json", "type_name", "id")

    print("\n______Name to Id conversion for new tables is successful!!_____\n")
    print("--" * 40)

    # Detecting missing values 
    detecting_missing_values()
    
    print("\n_____Detection of missing values is done successfully!!_____\n")
    print("--" * 40)
    print("\n\n")
    print("*****Data Transformation is completed successfully!!*****\n")
    print("==" * 40)
    print("\n")
    
# ------------------------------------------------------------------------------------------------
def extraction():
    print("\n!!!Extracting data!!!\n")
    endpointList = ["pokemon", "pokemon-species", "ability", "pokemon-form", "type"]
    # for endpoint in endpointList:
    #     extraction_1(endpoint)
    #     print("--" * 40)
    extraction_1(endpointList[-2])
    print("\n*****Extraction completed successfully!!!*****\n")
    print("==" * 40)

# ========================================================================================================
# Airflow part

with DAG(
    dag_id = "PokeAPI_ETL",
    description = "ETL from API to MySQL",
    tags = ["ETL", "MySQL", "API"],
    start_date = datetime(2025, 1, 1),
    schedule_interval = "@daily",
    catchup = False
) as dag:
    
    task_1 = PythonOperator(
        task_id = "Extract",
        python_callable = extraction
    )

    task_2 = PythonOperator(
        task_id = "Transform",
        python_callable = transform
    )

    task_3 = PythonOperator(
        task_id = "Load",
        python_callable = load
    )

    task_1 >> task_2 >> task_3
