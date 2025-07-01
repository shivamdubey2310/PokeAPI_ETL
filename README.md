# PokeAPI ETL Pipeline

This project builds a complete **ETL (Extract, Transform, Load)** pipeline using **Apache Airflow**, **Python**, and **MySQL**. The pipeline extracts data from the [PokeAPI](https://pokeapi.co/), performs data cleaning and transformation, and loads the processed data into a MySQL database.

---

## Project Structure

```
pokeapi_etl/
├── raw_json/                # Raw extracted JSONs from PokeAPI
├── Assets/
   └── SchemaDesign.md       # Schema design for MySQL Db                  
├── cleaned_json/            # Cleaned and transformed JSONs
├── dags/
│   └── pokeapi_etl.py       # Main Airflow DAG file
├── helper_functions         # Utility functions for transformation
│   └── json_explorer.py 
├── .env                     # Environment variables (MySQL credentials)
└── README.md                # Project documentation
```

---

## Features

- Extracts Pokémon data from the public PokeAPI.
- Cleans and transforms the data, handling relationships, missing values, and ID mappings.
- Stores structured data in a **MySQL** relational schema.
- Generates schema documentation in markdown.
- Fully automated using **Apache Airflow**.
- Includes error-handling and logging mechanisms.

---

## Technologies Used

- **Python 3.10+**
- **Apache Airflow**
- **MySQL**
- **Pandas**
- **SQLAlchemy**
- **PokeAPI**
- **Docker (recommended for Airflow)**

---

## Schema Overview

The ETL loads data into the following relational tables:

- `pokemon_species`
- `pokemon`
- `ability`
- `pokemon_ability`
- `pokemon_form`
- `type`
- `pokemon_types`

Relationships are preserved using foreign keys to maintain data integrity.

---

## DAG Overview

The Airflow DAG (`PokeAPI_ETL`) runs daily and consists of 3 tasks:

1. **Extract** - Calls `extraction()` to fetch data from PokeAPI.
2. **Transform** - Cleans and transforms the data using:
   - Field pruning
   - ID mapping
   - Missing value checks
3. **Load** - Creates MySQL schema and loads data via SQLAlchemy.

---

## Learnings

- Handling nested JSON transformations
- Designing relational schemas from semi-structured data
- Implementing Airflow DAGs for full ETL automation

---