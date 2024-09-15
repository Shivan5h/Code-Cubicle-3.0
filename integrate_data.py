import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient
import requests

# Function to load data from CSV
def load_csv(file_path):
    return pd.read_csv(file_path)

# Function to load data from SQL database
def load_sql(db_uri, query):
    engine = create_engine(db_uri)
    with engine.connect() as connection:
        return pd.read_sql(query, connection)

# Function to load data from NoSQL (MongoDB)
def load_nosql(db_uri, db_name, collection_name):
    client = MongoClient(db_uri)
    db = client[db_name]
    collection = db[collection_name]
    return pd.DataFrame(list(collection.find()))

# Function to load data from an API
def load_api(api_url, api_key):
    response = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})
    return pd.json_normalize(response.json())

# Integrating all sources into a single DataFrame
def integrate_data(csv_file=None, sql_details=None, nosql_details=None, api_details=None):
    final_df = pd.DataFrame()

    if csv_file:
        csv_data = load_csv(csv_file)
        final_df = pd.concat([final_df, csv_data], axis=0)

    if sql_details:
        sql_data = load_sql(sql_details['db_uri'], sql_details['query'])
        final_df = pd.concat([final_df, sql_data], axis=0)

    if nosql_details:
        nosql_data = load_nosql(nosql_details['db_uri'], nosql_details['db_name'], nosql_details['collection_name'])
        final_df = pd.concat([final_df, nosql_data], axis=0)

    if api_details:
        api_data = load_api(api_details['api_url'], api_details['api_key'])
        final_df = pd.concat([final_df, api_data], axis=0)

    final_df.to_csv('final.csv', index=False)
    return final_df
