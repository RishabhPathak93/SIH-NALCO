import joblib

def load_model(model_path='model/wire_rod_model.pkl'):
    model = joblib.load(model_path)
    return model
