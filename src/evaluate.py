import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

model = joblib.load("models/model.pkl")

df = pd.read_csv("data/housing.csv")

X = df.drop("price", axis=1)
y = df["price"]

pred = model.predict(X)

rmse = np.sqrt(mean_squared_error(y, pred))

print("RMSE:", rmse)