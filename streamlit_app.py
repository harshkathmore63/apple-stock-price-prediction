import streamlit as st
import pickle

# Load model
with open("tsmodel.pkl", "rb") as f:
    model = pickle.load(f)

# Page config
st.set_page_config(page_title="Apple Stock Predictor", layout="centered")

# Title
st.title("📈 Apple Stock Price Prediction")

st.markdown("""
This app predicts the **next stock price** of Apple using a trained time series model.
""")

# Inputs (UI only for now)
col1, col2, col3 = st.columns(3)

with col1:
    year = st.number_input("Year", 2000, 2100, 2024)
with col2:
    month = st.number_input("Month", 1, 12, 1)
with col3:
    day = st.number_input("Day", 1, 31, 1)

# Button
if st.button("Predict"):
    with st.spinner("Predicting..."):
        try:
            prediction = model.forecast(steps=1)
            value = float(prediction.iloc[0])
            st.success(f"💰 Predicted Price: ${value:.2f}")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.caption("Note: Prediction is based on historical trends and does not use selected date directly.")