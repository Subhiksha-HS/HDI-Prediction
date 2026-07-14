import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv("hdi.csv")

X = data.drop("HDI", axis=1)
y = data["HDI"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

joblib.dump(model, "hdi_model.pkl")

print("Model Saved Successfully")