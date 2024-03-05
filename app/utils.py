import base64
import json
import pickle
import numpy as np
import streamlit as st


def predict(input,model):

    input = np.array(input)
    input = input.reshape(1,-1)
    predicted_price = model.predict(input)[0]
    return predicted_price


def load_model(model_path): 
    model = pickle.load(open(model_path, "rb"))
    return model


def set_background(img_file):

    with open(img_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)