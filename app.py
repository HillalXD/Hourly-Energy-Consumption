import pickle
import streamlit as st
from datetime import time, date
from calendar import month_abbr
from dateutil import parser
import pandas as pd



with open('xgboost.pkl', 'rb') as f:
    model = pickle.load(f)

def app():
    st.title('Energy Consumption Prediction')


    # Define app inputs
    inputs = {
        'hour': st.slider("Select Time (hour)", min_value=0, max_value=23),
        'day': st.slider("Select date", min_value=1, max_value=31),
        'month': st.slider('Select Month', min_value=1, max_value=12),
        'year': st.slider('Select Year', min_value=2004, max_value=2023)
    }

    # Preprocess input and make prediction
    df = pd.DataFrame(inputs, index=[0])
    prediction = model.predict(df)

    # Display prediction
    st.write("predicted energy consumption : {}".format(prediction[0]))

# Run Streamlit app
if __name__ == '__main__':
    app()
