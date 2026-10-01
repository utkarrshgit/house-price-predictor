import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/house_price_model.pkl")

# Page title
st.title("California House Price Predictor")
st.write("Enter the characteristics of a geographic area to predict its median house value.")

# User inputs
med_inc = st.number_input(
    "Median Income",
    min_value=0.4999,
    max_value=15.0001,
    value=5.0
)

house_age = st.number_input(
    "House Age",
    min_value=1.0,
    max_value=52.0,
    value=20.0
)

ave_rooms = st.number_input(
    "Average Rooms",
    min_value=0.8461,
    max_value=141.91,
    value=5.0
)

ave_bedrms = st.number_input(
    "Average Bedrooms",
    min_value=0.3333,
    max_value=34.07,
    value=1.0
)

population = st.number_input(
    "Population",
    min_value=3.0,
    max_value=35682.0,
    value=1000.0
)

ave_occup = st.number_input(
    "Average Occupancy",
    min_value=0.6923,
    max_value=1243.33,
    value=3.0
)

latitude = st.number_input(
    "Latitude",
    min_value=32.54,
    max_value=41.95,
    value=34.0
)

longitude = st.number_input(
    "Longitude",
    min_value=-124.35,
    max_value=-114.31,
    value=-118.0
)

# Prediction button
if st.button("Predict Price"):

    new_house = pd.DataFrame({
        "MedInc": [med_inc],
        "HouseAge": [house_age],
        "AveRooms": [ave_rooms],
        "AveBedrms": [ave_bedrms],
        "Population": [population],
        "AveOccup": [ave_occup],
        "Latitude": [latitude],
        "Longitude": [longitude]
    })

    prediction = model.predict(new_house)

    price = prediction[0] * 100000

    st.success(f"Predicted House Value: ${price:,.2f}")