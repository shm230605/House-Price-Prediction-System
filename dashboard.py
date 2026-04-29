import streamlit as st
import requests

st.title("🏠 House Price Predictor")

area = st.number_input("Area", 500, 10000, 2000)
bedrooms = st.number_input("Bedrooms", 1, 10, 3)
bathrooms = st.number_input("Bathrooms", 1, 10, 2)
location_score = st.slider("Location Score", 1, 10, 7)
age = st.number_input("Age", 0, 100, 10)

if st.button("Predict Price"):

    payload = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "location_score": location_score,
        "age": age
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"🏡 Price: ₹ {result['predicted_price']:,}")
    else:
        st.error("API Error")