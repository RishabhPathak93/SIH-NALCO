import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
import optuna
from optuna.samplers import TPESampler
from data_preprocessing import load_data, preprocess_data

def objective(trial):
    param = {
        'objective': 'reg:squarederror',
        'booster': 'gbtree',
        'eta': trial.suggest_float('eta', 0.01, 0.3, step=0.01),
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'subsample': trial.suggest_float('subsample', 0.6, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 1.0),
        'lambda': trial.suggest_float('lambda', 0.1, 1.0),
        'alpha': trial.suggest_float('alpha', 0.1, 1.0),
        'n_estimators': trial.suggest_int('n_estimators', 100, 1000, step=50)
    }
    
    model = xgb.XGBRegressor(**param, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    score = mean_squared_error(y_test, y_pred)
    return score

def train_model(X, y):
    global X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    study = optuna.create_study(direction='minimize', sampler=TPESampler())
    study.optimize(objective, n_trials=50)
    
    best_params = study.best_params
    print(f"Best parameters: {best_params}")
    
    model = xgb.XGBRegressor(**best_params, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    for i, target in enumerate(y.columns):
        print(f'\nEvaluation for {target}:')
        print(f'R^2 Score: {r2_score(y_test[target], y_pred[:, i])}')
        print(f'Mean Squared Error: {mean_squared_error(y_test[target], y_pred[:, i])}')
        
        plt.figure(figsize=(10, 5))
        sns.scatterplot(x=y_test[target], y=y_pred[:, i])
        plt.xlabel('Actual Values')
        plt.ylabel('Predicted Values')
        plt.title(f'Actual vs Predicted for {target}')
        plt.show()
    
    joblib.dump(model, 'model/wire_rod_model_xgb.pkl')
    print("Model saved to 'model/wire_rod_model_xgb.pkl'")

if __name__ == "__main__":
    data = load_data('data/aluminium_wire_rod_data.csv')
    X, y = preprocess_data(data)
    train_model(X, y)
