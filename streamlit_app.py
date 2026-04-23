import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("💼 Salary Prediction App")

st.write("Enter your details:")

# Inputs
experience = st.slider("Years of Experience", 0, 10, 1)
skills = st.slider("Skill Level", 1, 10, 5)

# Predict button
if st.button("Predict Salary"):
    input_data = np.array([[experience, skills]])
    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Salary: ₹{round(prediction,2)}")