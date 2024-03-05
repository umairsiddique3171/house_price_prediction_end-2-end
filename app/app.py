import streamlit as st
import pickle
import json
import numpy as np
from utils import predict, load_model , set_background


import warnings
warnings.filterwarnings("ignore")


# set background
set_background('background_img.jpg')


# set title
st.title("House Price Prediction Web App")


# getting input form user
col1, col2 = st.columns(2)
    
with col1:
    crim = st.text_input('per capita crime rate by town')
    
with col2:
    zn = st.text_input('proportion of lots over 25,000 sq.ft.')

with col1:
    indus = st.text_input('proportion of non-retail business acres per town')

with col2:
    chas = st.text_input('near charles river (0/1)')

with col1 : 
    nox = st.text_input('nitric oxides concentration (parts per 10 million)')

with col2:
    rm = st.text_input('average number of rooms per dwelling')

with col1:
    age = st.text_input('proportion of owner occupied units build prior to 1940')

with col2:
    dis = st.text_input('weighted distances to five Boston employment centres')

with col1:
    rad = st.text_input('index of accessibility to radial highways')

with col2:
    tax = st.text_input('full-value property-tax rate per $10,000')

with col1:
    ptratio = st.text_input('pupil-teacher ratio by town')

with col2:
    b = st.text_input('1000(Bk - 0.63)^2 where Bk is black people proportion')

with col1:
    lstat = st.text_input('lower status of the population')


# load classifier
model = load_model("linear_regression_model.p")


# classification
if st.button('Results'):
    input_ref = ["01","02","03","04","05","06","07","08","09","10","11","12","13"]
    input_list = [crim, zn, indus, chas, nox, rm, age, dis, rad, chas, ptratio, b, lstat]
    missing_values = [input_ref[i] for i, val in enumerate(input_list) if val is None or val == '']

    if missing_values:
        st.write("## Missing Values")
        for missing_value in missing_values:
            st.write(f"### Column '{missing_value}' missing.")
        st.write("## Please refresh and enter the values again")
    
    else: 
        result = predict([float(crim),float(zn),float(indus),float(chas),float(nox),float(rm),float(age),float(dis),float(rad),float(chas),float(ptratio),float(b),float(lstat)],model)

        # show results
        st.write("## Result")
        st.write(f"### Predicted Price : {result*1000:.2f} USD")

        