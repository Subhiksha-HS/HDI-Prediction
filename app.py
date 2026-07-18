from flask import Flask, render_template, request
import joblib
import numpy as np
import traceback
import webbrowser

# Create Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("hdi_model.pkl")

print("Model Loaded Successfully")
print(model)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():

    print("\n========== PREDICT BUTTON CLICKED ==========")

    try:
        # Get input values
        life = float(request.form["life"])
        mean = float(request.form["mean"])
        expected = float(request.form["expected"])
        gni = float(request.form["gni"])

        print("Inputs:")
        print("Life Expectancy =", life)
        print("Mean Years School =", mean)
        print("Expected Years School =", expected)
        print("GNI =", gni)

        # Prepare features
        features = np.array([[life, mean, expected, gni]])

        print("Features:", features)

        # Predict
        prediction = model.predict(features)[0]

        print("Prediction:", prediction)
        print("Prediction Type:", type(prediction))

        # Decide result text
        if prediction == "Very High":
            level = "🟢 Very High Human Development"

        elif prediction == "High":
            level = "🟡 High Human Development"

        elif prediction == "Medium":
            level = "🟠 Medium Human Development"

        elif prediction == "Low":
            level = "🔴 Low Human Development"

        else:
            level = "Unknown Category"

        return render_template(
            "index.html",
            prediction=prediction,
            level=level
        )

    except Exception as e:

        print("\n========== ERROR ==========")
        traceback.print_exc()

        return render_template(
            "index.html",
            prediction="Error",
            level=str(e)
        )


# Run Flask
if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True, use_reloader=False)