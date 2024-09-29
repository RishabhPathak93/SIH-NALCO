import streamlit as st
import pandas as pd
from model_utils import load_model

model = load_model('model/wire_rod_model_xgb.pkl')

st.title("Aluminium Wire Rod Property Prediction")

st.sidebar.header("Input Parameters")

chemical_composition = st.sidebar.number_input('Chemical Composition', value=95.0, min_value=90.0, max_value=99.0, step=0.1)
casting_temp = st.sidebar.number_input('Casting Temp (°C)', value=700.0, min_value=600.0, max_value=750.0, step=1.0)
cooling_water_temp = st.sidebar.number_input('Cooling Water Temp (°C)', value=20.0, min_value=10.0, max_value=30.0, step=1.0)
cooling_water_pressure = st.sidebar.number_input('Cooling Water Pressure (bar)', value=5.0, min_value=1.0, max_value=10.0, step=0.1)
casting_speed = st.sidebar.number_input('Casting Speed (m/min)', value=10.0, min_value=5.0, max_value=20.0, step=0.1)
cast_bar_entry_temp = st.sidebar.number_input('Cast Bar Entry Temp (°C)', value=550.0, min_value=500.0, max_value=600.0, step=1.0)
emulsion_temp = st.sidebar.number_input('Emulsion Temp (°C)', value=40.0, min_value=30.0, max_value=50.0, step=1.0)
emulsion_pressure = st.sidebar.number_input('Emulsion Pressure (bar)', value=3.0, min_value=1.0, max_value=5.0, step=0.1)
emulsion_concentration = st.sidebar.number_input('Emulsion Concentration (%)', value=5.0, min_value=1.0, max_value=10.0, step=0.1)
quench_water_pressure = st.sidebar.number_input('Quench Water Pressure (bar)', value=3.0, min_value=1.0, max_value=5.0, step=0.1)

input_data = pd.DataFrame({
    'Chemical_Composition': [chemical_composition],
    'Casting_Temp_C': [casting_temp],
    'Cooling_Water_Temp_C': [cooling_water_temp],
    'Cooling_Water_Pressure_bar': [cooling_water_pressure],
    'Casting_Speed_m_min': [casting_speed],
    'Cast_Bar_Entry_Temp_C': [cast_bar_entry_temp],
    'Emulsion_Temp_C': [emulsion_temp],
    'Emulsion_Pressure_bar': [emulsion_pressure],
    'Emulsion_Concentration_percent': [emulsion_concentration],
    'Quench_Water_Pressure_bar': [quench_water_pressure]
})

if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write("Predicted Properties:")
    st.write(f"UTS (MPa): {prediction[0][0]:.2f}")
    st.write(f"Elongation (%): {prediction[0][1]:.2f}")
    st.write(f"Conductivity (MS/m): {prediction[0][2]:.2f}")
