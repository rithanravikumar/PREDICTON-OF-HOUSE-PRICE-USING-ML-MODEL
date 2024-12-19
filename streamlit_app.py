import streamlit as st
import pandas as pd
import pickle
from datetime import date

# Load the trained model
def load_model():
    with open("chennai_sales.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Streamlit App Title
st.title("Predicting House Prices Based on Past Sales Data")
st.image("https://raw.githubusercontent.com/Hariprasath1911/sale-app/main/1.png")
st.write("Enter the required details below to predict the house price.")

# Input Fields
selected_AREA = st.selectbox("Area",["Karapakkam", "Anna Nagar", "Adyar","Velachery","Chrompet","KK Nagar","T Nagar"])
area_mapping={"Karapakkam":4.0, "Anna Nagar":1.0, "Adyar":0.0,"Velachery":6.0,"Chrompet":2.0,"KK Nagar":3.0,"T Nagar":5.0}
AREA=area_mapping.get(selected_AREA)
INT_SQFT = st.number_input("Total Square Feet", min_value=0, step=1, value=1000)
DIST_MAINROAD = st.number_input("Distance to Main Road (in meters)", min_value=0, step=1, value=100)
N_BEDROOM = st.number_input("Number of Bedrooms", min_value=1, step=1, value=2)
N_BATHROOM = st.number_input("Number of Bathrooms", min_value=1, step=1, value=1)
N_ROOM = st.number_input("Total Number of Rooms", min_value=1, step=1, value=4)
selected_SALE_COND = st.selectbox("Sale Condition", ["Ab Normal", "Family", "Partial","Adj Land","Normal Sale"])
sale_maping={"Ab Normal":0.0, "Family":2.0, "Partial":4.0,"Adj Land":1.0,"Normal Sale":3.0}
SALE_COND=sale_maping.get(selected_SALE_COND)
selcted_PARK_FACIL = st.selectbox("Parking Facility", ["Yes", "No"])
park_mapping={"Yes":1, "No":0}
PARK_FACIL=park_mapping.get(selcted_PARK_FACIL)
selected_BUILDTYPE = st.selectbox("Building Type", ["Commercial", "Others", "House"])
buildtype_mapping={"Commercial":0.0, "Others":2.0, "House":1.0}
BUILDTYPE=buildtype_mapping.get(selected_BUILDTYPE)
selected_UTILITY_AVAIL = st.selectbox("Utility Availability", ["All Pub", "ELO", "No Sewage"])
utility_mapping={"All Pub":0.0, "ELO":1.0, "No Sewage":2.0}
UTILITY_AVAIL=utility_mapping.get(selected_UTILITY_AVAIL)
select_STREET = st.selectbox("Street Type", ["Paved", "Gravel", "No Access"])
street_mapping={"Paved":2.0, "Gravel":0.0, "No Access":1.0}
STREET=street_mapping.get(select_STREET)
select_MZZONE = st.selectbox("Zone Classification", ["A", "RH", "RL","I","C","RM"])
mzzone_mapping={"A":0.0, "RH":3.0, "RL":4.0,"I":2.0,"C":1.0,"RM":5.0}
MZZONE=mzzone_mapping.get(select_MZZONE)
QS_ROOMS = st.slider("Quality Score for Rooms", min_value=0.0, max_value=5.0, step=0.1, value=3.0)
QS_BATHROOM = st.slider("Quality Score for Bathrooms", min_value=0.0, max_value=5.0, step=0.1, value=3.0)
QS_BEDROOM = st.slider("Quality Score for Bedrooms", min_value=0.0, max_value=5.0, step=0.1, value=3.0)
QS_OVERALL = st.slider("Overall Quality Score", min_value=0.0, max_value=5.0, step=0.1, value=3.0)
REG_FEE = st.number_input("Registration Fee", min_value=0.0, step=0.01, value=50000.0)
COMMIS = st.number_input("Commission", min_value=0.0, step=0.01, value=20000.0)
selected_date = st.date_input("Select a date")
if selected_date:
    month_date_sale = selected_date.day
    day_date_sale = selected_date.month
    year_date_sale = selected_date.year
    week_date_sale = selected_date.isocalendar()[1]
build_age = st.number_input("Building Age (in years)", min_value=0, step=1, value=10)

# Prepare Input Data
def preprocess_inputs():
    data = {
        "AREA": AREA,
        "INT_SQFT": INT_SQFT,
        "DIST_MAINROAD": DIST_MAINROAD,
        "N_BEDROOM": N_BEDROOM,
        "N_BATHROOM": N_BATHROOM,
        "N_ROOM": N_ROOM,
        "SALE_COND": SALE_COND,
        "PARK_FACIL": PARK_FACIL,
        "BUILDTYPE": BUILDTYPE,
        "UTILITY_AVAIL": UTILITY_AVAIL,
        "STREET": STREET,
        "MZZONE": MZZONE,
        "QS_ROOMS": QS_ROOMS,
        "QS_BATHROOM": QS_BATHROOM,
        "QS_BEDROOM": QS_BEDROOM,
        "QS_OVERALL": QS_OVERALL,
        "REG_FEE": REG_FEE,
        "COMMIS": COMMIS,
        "year_date_sale": year_date_sale,
        "month_date_sale": month_date_sale,
        "day_date_sale": day_date_sale,
        "week_date_sale": week_date_sale,
        "build_age": build_age,
    }
    return pd.DataFrame([data])

# Predict and Display Results
if st.button("Predict Price"):
    input_data = preprocess_inputs()
    prediction = model.predict(input_data)
    st.subheader("Predicted House Price")
    st.write(f"₹ {prediction[0]:,.2f}")
