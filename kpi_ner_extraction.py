import pandas as pd
import spacy

# Load a pre-trained NLP model
nlp = spacy.load("en_core_web_sm")

def extract_kpi_ner(query, vectorized_data):
    doc = nlp(query)
    kpis = []
    for ent in doc.ents:
        if ent.label_ in ['MONEY', 'PERCENT', 'DATE']:
            kpis.append(ent.text)

    if kpis:
        df = pd.DataFrame(vectorized_data)
        return df[kpis]
    return None

def extract_ner(query):
    doc = nlp(query)
    ner_info = {}
    for ent in doc.ents:
        if ent.label_ == 'ORG':
            ner_info['x_column'] = 'Date'
        if ent.label_ == 'MONEY':
            ner_info['y_column'] = 'Revenue'
    return ner_info if ner_info else None
