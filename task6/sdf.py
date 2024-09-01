#importing the necessary libraries
import streamlit as st
import joblib
import numpy as np

#Loading the model
model = joblib.load('model.pkl')

# adding the title and description
st.title("Customer Churn Prediction")
st.write("Please select from the given variables to predict whether the person will churn or not.")

# Creating the input fields for all features/variables
st.write("**Personal Info:**")
gender = st.radio("**Gender**", ["Male", "Female"])
senior_citizen = st.checkbox("**Senior Citizen**")
partner = st.checkbox("**Partner**")
dependents = st.checkbox("**Dependents**")
st.write("**Service Info:**")
phone_service = st.checkbox("**Phone Service**")
multiple_lines = st.radio("**Multiple Lines**", ["No phone service", "No", "Yes"])
internet_service = st.radio("**Internet Service**", ["No", "DSL", "Fiber optic"])
online_security = st.radio("**Online Security**", ["No internet service", "No", "Yes"])
online_backup = st.radio("**Online Backup**", ["No internet service", "No", "Yes"])
device_protection = st.radio("**Device Protection**", ["No internet service", "No", "Yes"])
tech_support = st.radio("**Tech Support**", ["No internet service", "No", "Yes"])
streaming_tv = st.radio("**Streaming TV**", ["No internet service", "No", "Yes"])
streaming_movies = st.radio("**Streaming Movies**", ["No internet service", "No", "Yes"])
st.write("**Billing Info:**")
contract_type = st.radio("**Contract Type**", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.checkbox("**Paperless Billing**")
payment_method = st.selectbox("**Payment Method**", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
monthly_charges = st.number_input("**Monthly Charges**", min_value=0.0, value=50.0)
total_charges = st.number_input("**Total Charges**", min_value=0.0, value=100.0)
tenure = st.slider("**Tenure (months)**", min_value=0, max_value=72, value=12)

# Convert categorical features to numerical if necessary
gender_mapping = {"Male": 0, "Female": 1}
yes_no_mapping = {"Yes": 1, "No": 0}
internet_mapping = {"No": 0, "DSL": 1, "Fiber optic": 2}
multi_lines_mapping = {"No phone service": 0, "No": 1, "Yes": 2}
contract_mapping = {"Month-to-month": 0, "One year": 1, "Two year": 2}
payment_mapping = {"Electronic check": 0, "Mailed check": 1, "Bank transfer (automatic)": 2, "Credit card (automatic)": 3}

# Apply mappings
gender = gender_mapping[gender]
multiple_lines = multi_lines_mapping[multiple_lines]
internet_service = internet_mapping[internet_service]
online_security = yes_no_mapping.get(online_security, 0)
online_backup = yes_no_mapping.get(online_backup, 0)
device_protection = yes_no_mapping.get(device_protection, 0)
tech_support = yes_no_mapping.get(tech_support, 0)
streaming_tv = yes_no_mapping.get(streaming_tv, 0)
streaming_movies = yes_no_mapping.get(streaming_movies, 0)
contract_type = contract_mapping[contract_type]
payment_method = payment_mapping[payment_method]

# Combine all features into a single input array
input_data = np.array([[gender, senior_citizen, partner, dependents, tenure,
                        phone_service, multiple_lines, internet_service, online_security,
                        online_backup, device_protection, tech_support, streaming_tv,
                        streaming_movies, contract_type, paperless_billing, payment_method,
                        monthly_charges, total_charges]])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    
    # Display prediction
    if prediction[0] == 1:
        st.write("This customer is likely to churn.")
    else:
        st.write("This customer is not likely to churn.")
