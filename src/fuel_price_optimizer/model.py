import joblib
from sklearn.ensemble import RandomForestRegressor

def train_model(X_train, y_train, model_path):
    model = RandomForestRegressor(
        n_estimators=150, max_depth=12, random_state=42, n_jobs=-1
    )
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    return model

def load_model(model_path):
    return joblib.load(model_path)
