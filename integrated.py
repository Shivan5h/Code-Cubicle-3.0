import pandas as pd
from integrate_data import integrate_data
from normalize_data import normalize_data
from handling import handle_missing
from duplicate import remove_duplicates
from cat import encode_categorical

def main_pipeline(csv_file=None, sql_details=None, nosql_details=None, api_details=None):
    # Step 1: Integrate data from all sources
    final_df = integrate_data(csv_file, sql_details, nosql_details, api_details)

    # Step 2: Clean data
    final_df = normalize_data(final_df)
    final_df = handle_missing(final_df)
    final_df = remove_duplicates(final_df)
    final_df = encode_categorical(final_df)

    # Save cleaned data
    final_df.to_csv('cleaned_data.csv', index=False)
    return final_df

if __name__ == "__main__":
    main_pipeline(csv_file="yourfile.csv")  # Modify according to inputs
