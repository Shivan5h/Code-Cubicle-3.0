import openai
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from langchain_community.embeddings import HuggingFaceEmbeddings

from kpi_ner_extraction import extract_kpi_ner

import warnings

# Suppress the Pydantic warning about protected namespace conflict
warnings.filterwarnings("ignore", message="Field \"model_name\" in HuggingFaceInferenceAPIEmbeddings has conflict with protected namespace \"model_\".")


openai.api_key = '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'
# Function to analyze query and generate insights using OpenAI
def generate_insights(query, vectorized_data):
    context = vectorized_data

    prompt = f"Based on the following vectorized data, generate insights for the query: {query}\nContext:\n{context}"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=500
    )

    return response.choices[0].text.strip()

# Function to process KPI/NER and generate optional tabular output
def process_user_query(query, vectorized_data, serp_api_key=None):
    try:
        insights = generate_insights(query, vectorized_data)
        kpi_table = extract_kpi_ner(query, vectorized_data)
        return insights, kpi_table
    except Exception as e:
        print(f"Error: {e}. Resolving with SerpAPI...")
        serp_insights = resolve_query_with_serp(query, serp_api_key)
        return serp_insights, None
