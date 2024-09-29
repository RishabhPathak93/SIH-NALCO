import pandas as pd

def load_data(file_path):
    data = pd.read_csv('../data/aluminium_wire_rod_data.csv')
    return data

def preprocess_data(data):
    data = data.dropna()
    
    features = [
        'Chemical_Composition', 'Casting_Temp_C', 'Cooling_Water_Temp_C', 
        'Cooling_Water_Pressure_bar', 'Casting_Speed_m_min', 'Cast_Bar_Entry_Temp_C', 
        'Emulsion_Temp_C', 'Emulsion_Pressure_bar', 'Emulsion_Concentration_percent', 
        'Quench_Water_Pressure_bar'
    ]
    
    targets = ['UTS_MPa', 'Elongation_percent', 'Conductivity_MS_m']
    
    X = data[features]
    y = data[targets]
    
    return X, y
