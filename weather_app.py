# -*- coding: utf-8 -*-
"""weather_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12ILnLnnKhd6oIT9ONxLZTFQXlwXjWqiI
"""
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import numpy as np
import os

@st.cache_data
def load_data():
    file_path = "seattle-weather.csv"  # Ensure correct filename

    if not os.path.exists(file_path):
        st.error(f"Dataset not found: {file_path}. Please upload the dataset.")
        return None  # Return None if file is missing

    return pd.read_csv(file_path)

df = load_data()

# Check if data loaded successfully
if df is None:
    st.stop() 

# Load trained SVM model
import pickle  
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as model_file:  # Open the model in binary read mode
        model = pickle.load(model_file)
    return model

model = load_model()
weather_mapping = {0: "Sun", 1: "Snow", 2: "Rain", 3: "Drizzle", 4: "Fog"}
# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "About"])

# Home Page
if page == "Home":
    st.title("🌍 Welcome to ClimAIte")
    image_path = "climate_image.png"
    st.markdown("""
        Climate change is a major challenge affecting our planet.
        Our **AI-powered climate prediction tool** helps analyze weather data
        to provide valuable insights into future climate trends.

        ### Why Climate Prediction Matters:
        - Helps farmers prepare for changing weather conditions.
        - Assists policymakers in environmental planning.
        - Supports businesses in mitigating weather-related risks.

        Navigate to the **Prediction** tab to see AI-powered weather forecasts!
    """)
    st.image(image_path, use_container_width=True)  

# Prediction Page
elif page == "Prediction":
    st.title("🔮 Climate Prediction")
    st.write("Enter weather conditions to predict the category of the climate.")

    # User inputs
    temp_max = st.slider("Max Temperature (°C)", df["temp_max"].min(), df["temp_max"].max(), df["temp_max"].median())
    temp_min = st.slider("Min Temperature (°C)", df["temp_min"].min(), df["temp_min"].max(), df["temp_min"].median())
    precipitation = st.number_input("Precipitation (mm)", df["precipitation"].min(), df["precipitation"].max(), df["precipitation"].median())
    wind = st.number_input("Wind Speed (km/h)", df["wind"].min(), df["wind"].max(), df["wind"].median())
    if st.button("Predict"):
        prediction = model.predict(input_data)
        st.success("Predicted Weather")
        if prediction[0]==0:
           st.success("Sun")
        elif prediction[0]==1:
            st.success("Snow")
        elif prediction[0]==2:
            st.success("rain")
        elif prediction[0]==3:
            st.success("drizzle")
        else:
            st.success("fog")
# About Page (Pre-Saved Data Visualizations)
elif page == "About":
    st.title("📊 Data Visualizations")
    st.write("Explore the dataset through **box plots** and **histograms**.")
    st.subheader("Box Plots")
    for column in df.select_dtypes(include=['int64', 'float64']).columns:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.boxplot(x=df[column], ax=ax)
        ax.set_title(f'Box Plot of {column}')
        st.pyplot(fig)  # Show the plot

    # Display Histograms
    st.subheader("Histograms")
    for column in df.select_dtypes(include=['int64', 'float64']).columns:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.histplot(df[column], bins=30, kde=True, ax=ax)
        ax.set_title(f'Histogram of {column}')
        st.pyplot(fig)  # Show the plot

