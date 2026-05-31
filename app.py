import streamlit as st
import numpy as np
import pickle

# Loading both model and scaler
model = pickle.load(open('logistic_model.pkl', 'rb'))
scaler = pickle.load(open('logistic_scaler.pkl', 'rb'))

st.title("Diabetes Prediction App")

st.write("Enter patient details:")

# Inputs
preg = st.text_input("Pregnancies", placeholder="e.g. 2")
glucose = st.text_input("Glucose", placeholder="e.g. 120")
bp = st.text_input("Blood Pressure", placeholder="e.g. 80")
skin = st.text_input("Skin Thickness", placeholder="e.g. 20")
insulin = st.text_input("Insulin", placeholder="e.g. 85")
bmi = st.text_input("BMI", placeholder="e.g. 25.6")
dpf = st.text_input("DPF", placeholder="e.g. 0.5")
age = st.text_input("Age", placeholder="e.g. 30")

# Convert function
def to_float(val):
    try:
        return float(val)
    except:
        return None

# Prediction
if st.button("Predict"):
    values = [preg, glucose, bp, skin, insulin, bmi, dpf, age]

    if any(v == "" for v in values):
        st.warning("Please fill all fields")
    else:
        inputs = [to_float(v) for v in values]

        if None in inputs:
            st.error("Enter valid numbers")
        else:
            data = np.array([inputs])

            # scaling
            data_scaled = scaler.transform(data)

            prediction = model.predict(data_scaled)

            # Optional: probability
            prob = model.predict_proba(data_scaled)[0][1]

            if prediction[0] == 1:
                st.error("Diabetic")
            else:
                st.success("Not Diabetic")
            #Risk %
            st.write("Diabetes Risk:", round(prob * 100, 2), "%")
