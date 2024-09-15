def handle_missing(df):
    return df.fillna(df.mean(numeric_only=True))  # Replace numeric NaNs with mean
