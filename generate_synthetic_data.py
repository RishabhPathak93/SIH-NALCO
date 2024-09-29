import pandas as pd
import numpy as np

# Parameters for synthetic data
num_samples = 1000000

# Generate synthetic data
np.random.seed(42)

# Chemical Composition: Normally distributed values between 95% and 99%
chemical_composition = np.random.uniform(95, 99, num_samples)

# Casting Temp (°C): Uniformly distributed values between 600°C and 750°C
casting_temp = np.random.uniform(600, 750, num_samples)

# Cooling Water Temp (°C): Uniformly distributed values between 10°C and 30°C
cooling_water_temp = np.random.uniform(10, 30, num_samples)

# Cooling Water Pressure (bar): Normally distributed values between 1 and 10 bar
cooling_water_pressure = np.random.uniform(1, 10, num_samples)

# Casting Speed (m/min): Uniformly distributed values between 5 m/min and 20 m/min
casting_speed = np.random.uniform(5, 20, num_samples)

# Cast Bar Entry Temp (°C): Uniformly distributed values between 500°C and 600°C
cast_bar_entry_temp = np.random.uniform(500, 600, num_samples)

# Emulsion Temp (°C): Uniformly distributed values between 30°C and 50°C
emulsion_temp = np.random.uniform(30, 50, num_samples)

# Emulsion Pressure (bar): Normally distributed values between 1 and 5 bar
emulsion_pressure = np.random.uniform(1, 5, num_samples)

# Emulsion Concentration (%): Uniformly distributed values between 1% and 10%
emulsion_concentration = np.random.uniform(1, 10, num_samples)

# Quench Water Pressure (bar): Uniformly distributed values between 1 and 5 bar
quench_water_pressure = np.random.uniform(1, 5, num_samples)

# Target variables (based on assumed relationships)
# UTS (MPa): Generally inversely proportional to chemical composition and temperature, and directly proportional to pressure
UTS_MPa = (100 - (chemical_composition - 95) * 0.5 + (emulsion_pressure - 1) * 2
            - (casting_temp - 600) * 0.1 + np.random.normal(0, 1, num_samples))

# Elongation (%): Directly proportional to chemical composition and temperature, and inversely proportional to pressure
elongation_percent = (5 + (chemical_composition - 95) * 0.3 + (casting_temp - 600) * 0.1
                      - (emulsion_pressure - 1) * 0.5 + np.random.normal(0, 1, num_samples))

# Conductivity (MS/m): Directly proportional to chemical composition and inversely proportional to temperature
conductivity_MS_m = (60 - (chemical_composition - 95) * 0.4 + (casting_temp - 600) * 0.05
                     + np.random.normal(0, 1, num_samples))

# Create DataFrame
data = pd.DataFrame({
    'Chemical_Composition': chemical_composition,
    'Casting_Temp_C': casting_temp,
    'Cooling_Water_Temp_C': cooling_water_temp,
    'Cooling_Water_Pressure_bar': cooling_water_pressure,
    'Casting_Speed_m_min': casting_speed,
    'Cast_Bar_Entry_Temp_C': cast_bar_entry_temp,
    'Emulsion_Temp_C': emulsion_temp,
    'Emulsion_Pressure_bar': emulsion_pressure,
    'Emulsion_Concentration_percent': emulsion_concentration,
    'Quench_Water_Pressure_bar': quench_water_pressure,
    'UTS_MPa': UTS_MPa,
    'Elongation_percent': elongation_percent,
    'Conductivity_MS_m': conductivity_MS_m
})

# Save to CSV
data.to_csv('data/aluminium_wire_rod_data.csv', index=False)
print("Synthetic dataset created and saved to 'data/aluminium_wire_rod_data.csv'")



