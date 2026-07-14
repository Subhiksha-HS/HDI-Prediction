from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("hdi_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    life = float(request.form["life"])

    mean = float(request.form["mean"])

    expected = float(request.form["expected"])

    gni = float(request.form["gni"])

    prediction = model.predict([[life, mean, expected, gni]])

    return render_template(
        "index.html",
        prediction=prediction[0]
    )

if __name__ == "__main__":
    app.run(debug=True)