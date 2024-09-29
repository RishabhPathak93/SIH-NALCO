import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model_utils import load_model
import os
import joblib

# Load the prediction model
model = load_model(r'C:\Users\RISHABH\OneDrive\Desktop\New folder\SIH-nalco-problem-statement\src\model\wire_rod_model_xgb.pkl')

# Load the dataset for visualization
df = pd.read_csv(r'C:\Users\RISHABH\OneDrive\Desktop\New folder\SIH-nalco-problem-statement\src\Aluminium-Sheet1.csv', header=1)
df.columns = df.columns.str.strip()  # Clean up column names
sorted_df = pd.DataFrame()
for col in df.columns:
    sorted_df[col] = sorted(df[col])  # Sort values for visualization

# App title
st.title("Aluminium Wire Rod Dashboard")

# Add a Home button with a link
if st.button('Home'):
    st.markdown("<a href='https://aluminium-inky.vercel.app/' target='_blank'>Go to Home</a>", unsafe_allow_html=True)


# Create tabs for different functionalities
tab1, tab2 = st.tabs(["Prediction", "Visualization"])

# ===================== Prediction Tab ===========================
with tab1:
    st.header("Wire Rod Property Prediction")

    # Sidebar for input parameters
    st.sidebar.header("Input Parameters")

    chemical_composition = st.sidebar.number_input('Chemical Composition (%)', value=95.0, min_value=90.0, max_value=99.0, step=0.1)
    casting_temp = st.sidebar.number_input('Casting Temp (°C)', value=700.0, min_value=600.0, max_value=750.0, step=1.0)
    cooling_water_temp = st.sidebar.number_input('Cooling Water Temp (°C)', value=20.0, min_value=10.0, max_value=30.0, step=1.0)
    cooling_water_pressure = st.sidebar.number_input('Cooling Water Pressure (bar)', value=5.0, min_value=1.0, max_value=10.0, step=0.1)
    casting_speed = st.sidebar.number_input('Casting Speed (m/min)', value=10.0, min_value=5.0, max_value=20.0, step=0.1)
    cast_bar_entry_temp = st.sidebar.number_input('Cast Bar Entry Temp (°C)', value=550.0, min_value=500.0, max_value=600.0, step=1.0)
    emulsion_temp = st.sidebar.number_input('Emulsion Temp (°C)', value=40.0, min_value=30.0, max_value=50.0, step=1.0)
    emulsion_pressure = st.sidebar.number_input('Emulsion Pressure (bar)', value=3.0, min_value=1.0, max_value=5.0, step=0.1)
    emulsion_concentration = st.sidebar.number_input('Emulsion Concentration (%)', value=5.0, min_value=1.0, max_value=10.0, step=0.1)
    quench_water_pressure = st.sidebar.number_input('Quench Water Pressure (bar)', value=3.0, min_value=1.0, max_value=5.0, step=0.1)

    # Prepare input data for prediction
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

    # Predict and display the results
    if st.button('Predict'):
        prediction = model.predict(input_data)
        st.write("Predicted Properties:")
        st.write(f"UTS (MPa): {prediction[0][0]:.2f}")
        st.write(f"Elongation (%): {prediction[0][1]:.2f}")
        st.write(f"Conductivity (MS/m): {prediction[0][2]:.2f}")

# ===================== Visualization Tab ===========================
with tab2:
    st.header("UTS, Elongation, and Conductivity vs Parameters")

    # Selectbox for metric selection
    metrics = ['UTS_MPa', 'Elongation_percent', 'Conductivity_MS_m']
    selected_metric = st.selectbox("Select a Metric to Plot", metrics, key='metric_selection')

    # Selectbox for parameter selection
    param_options = sorted_df.columns.tolist()
    selected_param = st.selectbox("Select a Parameter to Plot Against", param_options, key='parameter_selection')

    # Function to plot the selected metric against the chosen parameter
    def plot_metric_vs_parameter(metric, parameter):
        plt.figure(figsize=(10, 6))
        plt.plot(sorted_df[parameter], sorted_df[metric], label=f'{metric}', color='black', linewidth=2)
        plt.title(f'{metric} vs {parameter}')
        plt.xlabel(parameter)
        plt.ylabel(metric)
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

    # Button to generate the plot
    if st.button("Generate Graph"):
        plot_metric_vs_parameter(selected_metric, selected_param)


