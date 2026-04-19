import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("ids_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Network Intrusion Detection System (Real-Time)")

st.write("Enter 41 feature values separated by comma")

input_data = st.text_area("Input Features")

if st.button("Predict"):

    try:
        data = list(map(float, input_data.split(",")))

        if len(data) != 41:
            st.error("Please enter exactly 41 values")
        else:
            data = np.array(data).reshape(1, -1)
            data = scaler.transform(data)

            result = model.predict(data)

            if result[0] == 0:
                st.success("Normal Traffic")
            else:
                st.error("Attack Detected")

    except:
        st.error("Invalid input format")
