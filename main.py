import pandas as pd
import openai
import requests
import chromadb
import sqlite3
from integrated import main_pipeline
from query_analysis import process_user_query
from visualize import visualize_data
from vectorization import vectorize_csv


def main(csv_file=None, sql_details=None, nosql_details=None, api_details=None, user_query=None, serp_api_key=None):
    """
    Main function that integrates data, processes queries, and optionally visualizes results.
    Args:
        csv_file: CSV file provided by the user.
        sql_details: SQL database connection details (optional).
        nosql_details: NoSQL database connection details (optional).
        api_details: API connection details (optional).
        user_query: Natural language query from the user.
        serp_api_key: SerpAPI key for resolving complex queries.
    """

    # Step 1: Data Integration and Cleaning
    cleaned_data = main_pipeline(csv_file, sql_details, nosql_details, api_details)
    print("Data has been cleaned and saved.")

    # Step 2: Vectorization for Enhanced Query Analysis
    vectorized_data = vectorize_csv('cleaned_data.csv')
    print("Data has been vectorized for better query processing.")

    # Step 3: Query Analysis and KPI/NER-based tabular output
    if user_query:
        insights, kpi_table = process_user_query(user_query, vectorized_data, serp_api_key="505def43bedd0c545057748bfcd7666845801f882ae51a54b336b28d49648fd5")
        print("Insights:", insights)

        if kpi_table is not None:
            print("Tabular Output based on KPI/NER:", kpi_table)

    # Step 4 (Optional): Visualization using NER
    visualize_data('cleaned_data.csv', user_query)


def run_smart_query_ai(csv_data=None, db_data=None, api_url=None, api_key=None, user_query=None):
    # Integrate all data sources (if provided)
    integrated_data = integrate_data(csv_data, db_data, api_url, api_key)

    # Analyze the query using the integrated data and optional API inputs
    insights = analyze_query(integrated_data, user_query, api_url, api_key)

    # Return the output in the required formats
    result = {
        'textual_insights': insights['text'],
        'tabular_output': insights.get('table'),
        'visual_output': insights.get('graph')
    }

    return result


def integrate_data(csv_data=None, db_data=None, api_url=None, api_key=None):
    dataframes = []

    # If CSV data is provided, add to list
    if csv_data is not None:
        dataframes.append(csv_data)

    # If database data is provided, convert to DataFrame and add to list
    if db_data is not None:
        dataframes.append(db_data)

    # If API URL and API Key are provided, fetch data and add to list
    if api_url and api_key:
        try:
            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                api_data = pd.DataFrame(response.json())  # Assuming the API returns JSON
                dataframes.append(api_data)
            else:
                raise Exception(f"API request failed with status code {response.status_code}")
        except Exception as e:
            print(f"Error fetching API data: {e}")

    # Integrate all DataFrames into a single DataFrame
    if dataframes:
        final_data = pd.concat(dataframes, ignore_index=True)
    else:
        final_data = pd.DataFrame()

    # Save the final integrated data to CSV (optional)
    final_data.to_csv('final.csv', index=False)

    return final_data

# Initialize ChromaDB
client = chromadb.Client()

def store_data_in_chromadb(data):
    # Assuming 'data' contains some textual data to store as embeddings
    collection = client.create_collection("my_collection")
    collection.add(
        embeddings=[openai.embeddings(data[i]) for i in range(len(data))],
        metadatas=[{"index": i} for i in range(len(data))],
        ids=[str(i) for i in range(len(data))]
    )
    return collection


def analyze_query(data, user_query, vectorization_method='tfidf', api_url=None, api_key=None):
    # Preprocessing the data before vectorization
    text_data = data.astype(str).apply(lambda x: ' '.join(x), axis=1)

    # Vectorize the data using either TF-IDF or ChromaDB
    if vectorization_method == 'tfidf':
        tfidf_matrix = vectorize_data_with_tfidf(text_data)
    elif vectorization_method == 'chromadb':
        chromadb_collection = store_data_in_chromadb(text_data)

    # Use OpenAI API for query analysis
    openai.api_key = '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'
    # If no user API URL and key are provided, use SerpAPI
    if not api_url or not api_key:
        serp_api_key = '505def43bedd0c545057748bfcd7666845801f882ae51a54b336b28d49648fd5'
        try:
            serp_response = requests.get(f"https://serpapi.com/search.json?q={user_query}&api_key={serp_api_key}")
            serp_data = serp_response.json()
            # Process serp_data as needed
        except Exception as e:
            print(f"Error fetching data from SerpAPI: {e}")

    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Analyze this data: {data} and answer the query: {user_query}",
            max_tokens=500
        )
        textual_insights = response.choices[0].text.strip()

        # Placeholder for tabular and visual insights based on KPI/NER
        tabular_output = None
        visual_output = None

        return {
            'text': textual_insights,
            'table': tabular_output,
            'graph': visual_output
        }

    except Exception as e:
        return {"text": f"Error analyzing query: {e}"}


if __name__ == "__main__":
    main(csv_file="yourfile.csv", user_query="Show revenue trends", serp_api_key="serp_api_key")
