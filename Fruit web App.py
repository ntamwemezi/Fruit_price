# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 10:36:18 2025

@author: pc
"""

import streamlit as st
import numpy as np
import pickle

# Load the model
with open('My_saved_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🍓 Fruit Price Prediction 🍇")

st.write("Enter fruit attributes to predict outcome")

# Input fields
RetailPrice = st.number_input("Retail Price", value=2.6064)
RetailPriceUnit = st.selectbox("Retail Price Unit", ['$/lb'])  # Optional
Yield = st.number_input("Yield", value=1.0)
CupEquivalentSize = st.number_input("Cup Equivalent Size", value=0.76)
CupEquivalentUnit = st.selectbox("Cup Equivalent Unit", ['cups'])  # Optional
Form_Canned = st.selectbox("Canned Form", [0, 1])
Form_Dried = st.selectbox("Dried Form", [0, 1])
Form_Frozen = st.selectbox("Frozen Form", [0, 1])
Form_Fresh = st.selectbox("Fresh Form", [0, 1])
Form_Juice = st.selectbox("Juice Form", [0, 1])

# Construct input array
input_data = np.array([
    27,
    RetailPrice,
    Yield,
    CupEquivalentSize,
    CupEquivalentSize * Yield,
    Form_Canned,
    Form_Dried,
    Form_Frozen,
    Form_Fresh,
    Form_Juice,
    0
])

shaped_data = input_data.reshape(1, -1)

# Predict
if st.button("Predict"):
    prediction = model.predict(shaped_data)

    st.success(f"Prediction: {prediction[0]}")

