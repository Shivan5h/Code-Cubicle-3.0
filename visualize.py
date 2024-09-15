import plotly.express as px
import pandas as pd
from kpi_ner_extraction import extract_ner

def visualize_data(csv_file='cleaned_data.csv', user_query=None):
    df = pd.read_csv(csv_file)
    ner_info = extract_ner(user_query)

    if ner_info:
        fig = px.line(df, x=ner_info['x_column'], y=ner_info['y_column'])
        fig.show()
    else:
        print("No NER-based visualizations available.")
