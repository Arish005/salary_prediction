import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
import os

# Check if the file exists before attempting to load it
def load_model():
    if os.path.exists('saved_steps.pkl'):
        with open('saved_steps.pkl', 'rb') as file:
            data = pickle.load(file)
        return data
    else:
        st.error("Model file 'saved_steps.pkl' not found.")
        return None

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    # Load the model only if it exists
    data = load_model()
    if data is not None:
        show_predict_page(data)
else:
    show_explore_page()
