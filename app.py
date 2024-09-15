import streamlit as st
import pandas as pd
import sqlite3
import main
from main import run_smart_query_ai
from main import run_smart_query_ai
from main import integrate_data
from main import store_data_in_chromadb
from main import analyze_query

st.image("your_logo.png", width=200)
# Title
st.title("INSIGHTFLOW")
st.header("Representing the seamless flow of insights from data")

# Input fields
csv_file = st.file_uploader("Upload CSV File", type=["csv"], key="csv_file")
db_file = st.file_uploader("Upload Database File", type=["db"], key="db_file")
api_url = st.text_input("API URL (Optional)", key="api_url")
api_key = st.text_input("API Key (Optional)", key="api_key")
user_query = st.text_area("Enter your query", key="user_query")

# Check if none of the files or API details are provided
if not csv_file and not db_file and not api_url and not api_key:
    st.warning("Please provide at least one of the following: CSV file, Database file, API URL, or API Key.")
else:
    # Submit button
    if st.button("Enter"):
        # Load CSV file if provided
        if csv_file:
            try:
                csv_data = pd.read_csv(csv_file)
            except Exception as e:
                st.error(f"Error loading CSV file: {e}")
                csv_data = None
        else:
            csv_data = None

        # Load database file if provided
        if db_file:
            try:
                conn = sqlite3.connect(db_file)
                db_data = pd.read_sql_query("SELECT * FROM your_table", conn)
                conn.close()
            except Exception as e:
                st.error(f"Error loading database file: {e}")
                db_data = None
        else:
            db_data = None

        # Run the main AI process
        try:
            # Use ChromaDB as the vectorization method
            result = run_smart_query_ai(csv_data, db_data, api_url, api_key, user_query)

            # Display results
            st.write("Textual Insights:")
            st.write(result.get('textual_insights', 'No insights available'))

            if result.get('tabular_output') is not None:
                st.write("Tabular Output:")
                st.table(result['tabular_output'])

            if result.get('visual_output') is not None:
                st.write("Visual Output:")
                st.plotly_chart(result['visual_output'])

        except Exception as e:
            st.error(f"Error during analysis: {e}")
