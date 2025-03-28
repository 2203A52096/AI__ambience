# AI__ambience
# 🌍 ClimAIte: Predict. Adapt. Sustain. ⚡
# Dataset is taken from 'https://www.kaggle.com/datasets/ananthr1/weather-prediction'
## 🔥 Inspiration  
Climate change has caused extreme weather events, disrupting agriculture, transportation, and daily life. We wanted to build an **AI-powered climate prediction tool** that helps people understand and prepare for upcoming weather conditions. By leveraging **machine learning**, we provide accurate forecasts based on historical weather data.

## 🧠 What We Learned  
Throughout this project, we explored:  
- **Feature engineering** to extract meaningful insights from weather data.  
- **Support Vector Machines (SVM)** and how it performs in climate classification.  
- **Streamlit for building interactive web applications**.  
- Overcoming challenges in **weather data inconsistencies and missing values**.

## 🛠️ How We Built It  
We followed a structured approach:  

### **1️⃣ Data Collection & Preprocessing**  
- We used a **weather dataset** containing:  
  - `date` – Timestamp of the weather record.  
  - `precipitation` – Amount of rainfall in mm.  
  - `temp_max` – Maximum daily temperature.  
  - `temp_min` – Minimum daily temperature.  
  - `wind` – Wind speed in km/h.  
  - `weather` – Weather condition (e.g., sunny, rainy, foggy).  

- Handled **missing values** and normalized numerical features.  
- Converted **weather conditions into numerical labels** for model training.  

### **2️⃣ Model Training & Optimization**  
- Implemented **SVM** for **weather classification** based on input features.  
- Tuned **hyperparameters** to optimize prediction accuracy.  
- Evaluated the model using **precision, recall, and accuracy metrics**.

### **3️⃣ Building the Streamlit App**  
- Designed an **interactive UI** for easy user input.  
- Allowed users to enter **weather conditions (temperature, wind, precipitation, etc.)**.  
- Integrated real-time prediction visualization.
### 🌍 Streamlit App Features  
 
### **Home page:**
#### 🎨 **Enhanced UI & Design**  
- Improved **homepage design** with a better-aligned image for an **aesthetic and engaging look**.  
- Increased **font size** and optimized layout spacing for **better readability and user experience**.  

#### 🎭 **Fun Facts & Jokes**  
- The **Home Page** now features a **“Tell me a joke”** button, displaying a **random weather-related joke** for a fun user experience.  

### 🔮 **Climate Prediction**  
- Users can **input weather parameters** (temperature, wind speed, precipitation) to get **real-time weather predictions** using our trained ML model.  
- The app uses **Support Vector Machines (SVM)** to classify weather into categories like **Sun, Snow, Rain, Drizzle, and Fog**.  

#### 👕 **Clothing Recommendations**  
- Based on the predicted weather, the app suggests **two outfit ideas for men and women** to help users dress appropriately.  
- Example: For **Rainy Weather**, the recommendations include:  
  - **Men:** Raincoat with waterproof pants, boots, and an umbrella  
  - **Women:** Trench coat with waterproof leggings, boots, and an umbrella  

#### 🍲 **Food Recommendations**  
- Provides **detailed meal suggestions** based on weather conditions, ensuring users eat according to the climate.  
- Example: On **a cold snowy day**, the app suggests hot soups, stews, and warm drinks like spiced tea. 
---

## 🛠️ Built With  
- **Python** – Core programming language for data processing and machine learning.  
- **Pandas & NumPy** – For handling and preprocessing weather data.  
- **Matplotlib & Seaborn** – For visualizing trends in climate data.  
- **Scikit-learn** – For implementing and training the **SVM model**.  
- **Streamlit** – To build an **interactive web app** for real-time predictions.  
- **pickle** – To save and load the trained SVM model efficiently.  
- **Google Colab** – For model training and experimentation.  
- **Git & GitHub** – For version control and collaboration.  

## 🚧 Challenges We Faced  
- **Time-series Complexity** – Weather data is sequential, making it challenging for traditional ML models.  
- **Data Preprocessing** – Handling missing values and encoding categorical weather types.  
- **Balancing Performance & User Experience** – Ensuring real-time predictions without lag.  
- **Model Selection** – Testing different ML models before finalizing SVM.

## 🚀 Future Enhancements  
- **Advanced models (LSTMs, CNNs)** for improved forecasting.  
- **Live weather API integration** for real-time data inputs.  
- **Mobile-friendly app version** for wider accessibility.  
- **IoT integration** to pull sensor-based climate data directly.  

---

🌱 **ClimAIte** is just the beginning! By harnessing AI, we can drive sustainable decision-making and improve climate preparedness.  
