import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/housing.csv")

df.groupby("location_score")["price"].mean().plot(kind="bar")
plt.title("Location vs Price Trend")
plt.show()