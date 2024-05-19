import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import base64

# Set theme
st.set_page_config(
    page_title="Patient Diagnosis Prediction",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add background image
st.write(
    """
    <style>
    .stApp {
        background-image: url("https://datamotion.com/wp-content/uploads/2019/12/Header-Size-Crop-11-e1580747284645-600x237-1.png");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)




# Function to create a downloadable link for a DataFrame
def download_link(df, filename, text):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">{text}</a>'
    return href

# Set up Font Awesome icons for download and share
download_icon = '<i class="fas fa-download"></i>'
share_icon = '<i class="fas fa-share-alt"></i>'

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("hosp_data.csv")
    # Encoding categorical columns
    label_encoder = LabelEncoder()
    data['SEX'] = label_encoder.fit_transform(data['SEX'])
    data['SOURCE'] = label_encoder.fit_transform(data['SOURCE'])
    return data

# Create Streamlit web app
st.title("Patient Diagnosis Prediction")

# Function to predict patient type (outpatient or inpatient)
def predict_patient_type(haematocrit, haemoglobins, erythrocyte, leucocyte, thrombocyte, mch, mchc, mcv, age, sex):
    input_data = pd.DataFrame({
        'HAEMATOCRIT': [haematocrit],
        'HAEMOGLOBINS': [haemoglobins],
        'ERYTHROCYTE': [erythrocyte],
        'LEUCOCYTE': [leucocyte],
        'THROMBOCYTE': [thrombocyte],
        'MCH': [mch],
        'MCHC': [mchc],
        'MCV': [mcv],
        'AGE': [age],
        'SEX': [sex]
    })
    
    if 'model' not in st.session_state:
        st.warning("Please train the model first.")
        return None
    
    prediction = st.session_state.model.predict(input_data)
    return prediction[0]


# ABOUT section explaining the features
st.sidebar.markdown("## ABOUT")
st.sidebar.write("### Features Explanation:")
st.sidebar.write("- **Haematocrit**: The proportion of red blood cells in the blood.")
st.sidebar.write("- **Haemoglobins**: The protein in red blood cells that carries oxygen.")
st.sidebar.write("- **Erythrocyte**: Red blood cell count in a volume of blood.")
st.sidebar.write("- **Leucocyte**: White blood cell count, which is important for immune function.")
st.sidebar.write("- **Thrombocyte**: Platelet count, essential for blood clotting.")
st.sidebar.write("- **MCH (Mean Corpuscular Hemoglobin)**: Average amount of hemoglobin in red blood cells.")
st.sidebar.write("- **MCHC (Mean Corpuscular Hemoglobin Concentration)**: Concentration of hemoglobin in red blood cells.")
st.sidebar.write("- **MCV (Mean Corpuscular Volume)**: Average volume of red blood cells.")
st.sidebar.write("- **Age**: Age of the patient.")
st.sidebar.write("- **Sex**: Gender of the patient (Male or Female).")

# Sidebar inputs
st.sidebar.header("Patient Diagnosis")
haematocrit = st.sidebar.number_input("Haematocrit")
haemoglobins = st.sidebar.number_input("Haemoglobins")
erythrocyte = st.sidebar.number_input("Erythrocyte")
leucocyte = st.sidebar.number_input("Leucocyte")
thrombocyte = st.sidebar.number_input("Thrombocyte")
mch = st.sidebar.number_input("MCH")
mchc = st.sidebar.number_input("MCHC")
mcv = st.sidebar.number_input("MCV")
age = st.sidebar.number_input("Age")
sex_input = st.sidebar.selectbox("Sex", ["M", "F"])

# Encode the sex input
label_encoder = LabelEncoder()
sex = label_encoder.fit_transform([sex_input])[0]

# Load the data and train the model
data = load_data()

# Split data into features and target variable
X = data.drop(columns=["SOURCE"])
y = data["SOURCE"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
@st.cache_resource
def train_model():
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

# Save the trained model in session state
st.session_state.model = train_model()

# Predict button
if st.sidebar.button("Predict"):
    prediction = predict_patient_type(haematocrit, haemoglobins, erythrocyte, leucocyte, thrombocyte, mch, mchc, mcv, age, sex)
    if prediction is not None:
        if prediction == 0:
            st.write("**Predicted Patient Type: Outpatient**")
        else:
            st.write("**Predicted Patient Type: Inpatient**")

# Calculate feature importance
feature_importance = st.session_state.model.feature_importances_

# Display feature importance
st.subheader("Feature Importance")
feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importance})
st.write(feature_importance_df)

# Plot feature importance as a bar chart
st.bar_chart(feature_importance_df.set_index('Feature'))

