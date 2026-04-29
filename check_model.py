import joblib

model = joblib.load("models/model.pkl")

print("Features expected:", model.n_features_in_)