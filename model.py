import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# ==========================
# Load Dataset
# ==========================
data = pd.read_csv("hdi.csv")

# ==========================
# Check Missing Values
# ==========================
print("Missing Values:")
print(data.isnull().sum())

# Remove missing values (if any)
data.dropna(inplace=True)

# ==========================
# Select Features (Independent Variables)
# ==========================
X = data[[
    "LifeExpectancy",
    "MeanYearsSchool",
    "ExpectedYearsSchool",
    "GNI"
]]

# ==========================
# Select Target (Dependent Variable)
# ==========================
y = data["HDI"]

# ==========================
# Label Encoding
# ==========================
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# ==========================
# Split Dataset
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# Train Model
# ==========================
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# ==========================
# Save Model
# ==========================
joblib.dump(model, "hdi_model.pkl")

print("✅ Model trained and saved successfully!")