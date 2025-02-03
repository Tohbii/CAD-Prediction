import streamlit as st
import tensorflow as tf

# Load your trained model (make sure 'cad_model.h5' is in the same directory as this script)
model = tf.keras.models.load_model('cad_model.h5')

# Streamlit UI to collect user input for prediction
st.title("Coronary Artery Disease Prediction")

# Input fields for user data (based on Framingham model)
age = st.number_input('Age', min_value=20, max_value=120)
sex = st.selectbox('Sex', options=['Male', 'Female'])
cholesterol = st.number_input('Total Cholesterol (mg/dL)', min_value=100, max_value=500)
hdl_cholesterol = st.number_input('HDL Cholesterol (mg/dL)', min_value=20, max_value=100)
systolic_bp = st.number_input('Systolic Blood Pressure (mmHg)', min_value=80, max_value=200)
diastolic_bp = st.number_input('Diastolic Blood Pressure (mmHg)', min_value=50, max_value=120)
bp_treatment = st.selectbox('Under Blood Pressure Treatment?', options=['Yes', 'No'])
smoking_status = st.selectbox('Smoking Status', options=['Yes', 'No'])
diabetes = st.selectbox('Do you have Diabetes?', options=['Yes', 'No'])
bmi = st.number_input('Body Mass Index (BMI)', min_value=10.0, max_value=50.0)

# Convert categorical inputs to numerical format
sex = 1 if sex == 'Male' else 0
bp_treatment = 1 if bp_treatment == 'Yes' else 0
smoking_status = 1 if smoking_status == 'Yes' else 0
diabetes = 1 if diabetes == 'Yes' else 0

# Make the prediction when the user clicks the button
if st.button('Predict'):
    # Prepare the input data for the model
    features = [[age, sex, cholesterol, hdl_cholesterol, systolic_bp, diastolic_bp, bp_treatment, smoking_status, diabetes, bmi]]

    # Make prediction
    prediction = model.predict(features)

    # Show the result
    st.write(f'Prediction: {prediction[0][0]:.2f}% risk of coronary artery disease in the next 10 years.')
