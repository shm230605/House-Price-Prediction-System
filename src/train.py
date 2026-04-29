import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# -----------------------
# Synthetic dataset
# -----------------------
np.random.seed(42)

data = pd.DataFrame({
    "area": np.random.randint(500, 5000, 500),
    "bedrooms": np.random.randint(1, 6, 500),
    "bathrooms": np.random.randint(1, 4, 500),
    "location_score": np.random.randint(1, 10, 500),
    "age": np.random.randint(0, 50, 500),
})

# Target (fake pricing formula)
data["price"] = (
    data["area"] * 300 +
    data["bedrooms"] * 50000 +
    data["bathrooms"] * 30000 +
    data["location_score"] * 80000 -
    data["age"] * 10000
)

X = data.drop("price", axis=1)
y = data["price"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "models/model.pkl")

print("✅ Model trained & saved")