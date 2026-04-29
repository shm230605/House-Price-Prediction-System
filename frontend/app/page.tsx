"use client";

import { useState } from "react";

export default function Home() {
  const [price, setPrice] = useState(null);

  const predict = async () => {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        area: 2000,
        bedrooms: 3,
        bathrooms: 2,
        location_score: 8,
        age: 10
      })
    });

    const data = await res.json();
    setPrice(data.predicted_price);
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>🏠 House Price Predictor</h1>

      <button onClick={predict} style={{ padding: 10, marginTop: 20 }}>
        Predict Price
      </button>

      {price && (
        <h2 style={{ marginTop: 20 }}>
          Predicted Price: ₹ {price}
        </h2>
      )}
    </div>
  );
}