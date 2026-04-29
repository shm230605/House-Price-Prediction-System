import numpy as np
import pandas as pd

np.random.seed(42)

n = 3000

df = pd.DataFrame({
    "area": np.random.randint(500, 5000, n),
    "bedrooms": np.random.randint(1, 6, n),
    "bathrooms": np.random.randint(1, 4, n),
    "location_score": np.random.randint(1, 10, n),
    "age": np.random.randint(0, 50, n)
})

df["price"] = (
    df["area"] * 120 +
    df["bedrooms"] * 50000 +
    df["bathrooms"] * 30000 +
    df["location_score"] * 80000 -
    df["age"] * 1000 +
    np.random.randint(-20000, 20000, n)
)

df.to_csv("data/housing.csv", index=False)

print("Dataset created successfully!")