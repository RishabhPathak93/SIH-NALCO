# Aluminium Wire Rod Property Prediction

## Project Overview

This project aims to predict the physical properties (UTS, Elongation, and Conductivity) of aluminium wire rods using machine learning. By analyzing casting parameters like temperature, pressure, speed, and chemical composition, we aim to optimize the wire rod production process.

---

## Dataset Description

The dataset contains various dynamic parameters related to the aluminium wire rod casting process. These parameters include:

### Features:
- **Chemical_Composition**: Purity of aluminium.
- **Casting_Temp_C**: Casting temperature.
- **Cooling_Water_Temp_C**: Cooling water temperature.
- **Cooling_Water_Pressure_bar**: Cooling water pressure.
- **Casting_Speed_m_min**: Casting speed.
- **Cast_Bar_Entry_Temp_C**: Temperature of the cast bar entering the rolling mill.
- **Emulsion_Temp_C**: Emulsion temperature at the rolling mill.
- **Emulsion_Pressure_bar**: Emulsion pressure at the rolling mill.
- **Emulsion_Concentration_percent**: Emulsion concentration at the rolling mill.
- **Quench_Water_Pressure_bar**: Quench water pressure.

### Target Variables:
- **UTS_MPa**: Ultimate Tensile Strength (MPa).
- **Elongation_percent**: Elongation percentage.
- **Conductivity_MS_m**: Conductivity (MS/m).

---

## Project Structure

aluminium-wire-rod-prediction/
├── data/
│   └── aluminium_wire_rod_data.csv
├── model/
│   └── wire_rod_model_xgb.pkl (created after training)
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_utils.py
│   └── streamlit_app.py
└── README.md



---

## Preprocessing

Preprocessing involves:
1. **Data Loading**: Reading the dataset.
2. **Feature Engineering**: Normalizing or scaling the features, if needed.
3. **Handling Missing Data**: Removing or filling missing values.
4. **Splitting Data**: Splitting the data into features (`X`) and target variables (`y`).

Preprocessing is handled in `data_preprocessing.py`:

##Model training
Model training is done in model_training.py, which includes:

Loading the dataset.
Splitting the dataset into training and testing sets.
Tuning Hyperparameters using Optuna.
Training the XGBoost model.
Saving the trained model as wire_rod_model_xgb.pkl.
To train the model, run the following command:

'python src/model_training.py'

## Running the streamlit application

The Streamlit application allows you to input casting parameters and predict the properties of the wire rod (UTS, Elongation, and Conductivity) in real-time.

To run the application, use the following command:

'streamlit run streamlit_app.py'

## How to use application
Enter the required input parameters (Chemical Composition, Casting Temp, etc.) in the sidebar.
Click "Predict".
The application will display the predicted UTS, Elongation, and Conductivity.




