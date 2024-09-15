from sklearn.preprocessing import OneHotEncoder

def encode_categorical(df):
    categorical_columns = df.select_dtypes(include=['object']).columns
    encoder = OneHotEncoder(sparse=False)
    encoded_data = pd.DataFrame(encoder.fit_transform(df[categorical_columns]), columns=encoder.get_feature_names_out(categorical_columns))
    return pd.concat([df.drop(columns=categorical_columns), encoded_data], axis=1)
