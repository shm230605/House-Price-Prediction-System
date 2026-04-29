def add_features(df):
    df["total_rooms"] = df["bedrooms"] + df["bathrooms"]
    df["price_per_sqft"] = df["price"] / df["area"]
    df["density"] = df["bedrooms"] / df["area"]
    return df