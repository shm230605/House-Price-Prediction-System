# 🏠 House Price Prediction System (End-to-End Machine Learning Project)

## 🚀 Project Overview

This project is a complete **end-to-end Machine Learning system** that predicts house prices based on property features such as area, bedrooms, bathrooms, location score, and age.

It includes:
- Data preprocessing & feature engineering
- Machine Learning model training
- Model evaluation (RMSE, MAE, R²)
- FastAPI backend for real-time predictions
- Streamlit dashboard for interactive UI

---

## 🎯 Problem Statement

Real estate pricing is complex and influenced by multiple factors. Manual estimation often leads to:
- Overpricing (slow sales)
- Underpricing (loss of revenue)
- Lack of data-driven decision making

This project solves that by building a **data-driven house price prediction system**.

---

## 💡 Solution

We built a regression-based ML system that:
- Learns patterns from housing data
- Predicts accurate property prices
- Provides real-time API access
- Offers an interactive dashboard for users

---

## 🧠 Tech Stack

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- Random Forest Regressor
- FastAPI (Backend API)
- Streamlit (Frontend Dashboard)
- Joblib (Model Serialization)

---

## 📊 Features Used

- Area (sq ft)
- Number of bedrooms
- Number of bathrooms
- Location score
- Age of house

---

## 🤖 Machine Learning Model

- Algorithm: Random Forest Regressor
- Training Approach: Supervised Regression
- Evaluation Metrics:
  - RMSE (Root Mean Squared Error)
  - MAE (Mean Absolute Error)
  - R² Score

---

## 📁 Project Structure
```
House-Price-Prediction-System/
│
├── 📁 data/
│   ├── housing.csv
│   ├── cleaned_data.csv
│
├── 📁 src/
│   ├── train.py
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── evaluate.py
│
├── 📁 api/
│   ├── main.py
│   ├── schemas.py
│   ├── utils.py
│
├── 📁 models/
│   ├── model.pkl
│
├── 📁 dashboard/
│   ├── dashboard.py
│
├── 📁 notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_model_training.ipynb
│
│
├── requirements.txt
├── README.md
├── .gitignore
└── main.py   (optional entry file)
```
📈 Project Workflow
```
Data Collection → Preprocessing → Feature Engineering → Model Training → Evaluation → API Deployment → Dashboard 

```
📊 Business Impact
Helps real estate agents estimate property value instantly
Assists buyers in fair pricing decisions
Supports banks in loan valuation models
Useful for property investment analysis

🚀 Future Improvements
Add XGBoost / LightGBM models
Deploy on cloud (AWS / Render / HuggingFace)
Add map-based visualization
Improve UI with React/Next.js
Add explainable AI (SHAP)

👨‍💻 Author

Shresthaa Maiti
