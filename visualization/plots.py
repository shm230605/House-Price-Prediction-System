import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/housing.csv")

plt.scatter(df["area"], df["price"])
plt.title("Area vs Price")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()