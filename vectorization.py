from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def vectorize_csv(csv_file):
    df = pd.read_csv(csv_file)
    tfidf_vectorizer = TfidfVectorizer()
    vectorized_data = tfidf_vectorizer.fit_transform(df.astype(str).values.flatten())
    return vectorized_data


