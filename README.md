# 🌍 Human Development Index (HDI) Prediction

## 📌 Project Overview
This project predicts the Human Development Index (HDI) category of a country using Machine Learning. It uses a Random Forest Classifier trained on HDI-related indicators and provides predictions through a Flask web application.

## 🚀 Features
- Predicts HDI category from user inputs
- Interactive web interface built with Flask
- Fast and accurate Random Forest model
- User-friendly design

## 🛠 Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- Joblib

## 📂 Dataset
The model is trained using the `hdi.csv` dataset.

### Input Features
- Life Expectancy
- Mean Years of Schooling
- Expected Years of Schooling
- GNI Per Capita

### Output
The model predicts one of the following categories:
- 🟢 Very High
- 🟡 High
- 🟠 Medium
- 🔴 Low

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Subhiksha-HS/HDI-Prediction.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## 📁 Project Structure

```
HDI-Prediction/
│── app.py
│── model.py
│── hdi.csv
│── hdi_model.pkl
│── requirements.txt
│── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── hdi.png
```
## Data Visualization

This project includes exploratory data analysis using Matplotlib and Seaborn.

### Graphs

- Distribution of Life Expectancy
- Life Expectancy vs HDI
- Correlation Heatmap
- GNI Distribution (Box Plot)

### Outputs

![Life Expectancy Distribution](visualizations/life_expectancy_distribution.png)

![Life Expectancy vs HDI](visualizations/life_expectancy_vs_hdi.png)

![Correlation Heatmap](visualizations/correlation_heatmap.png)

![GNI Box Plot](visualizations/gni_boxplot.png)

## 🎥 Demo Video

Watch the complete project demonstration here:

**🔗 Demo Video:**  
https://drive.google.com/file/d/118ijjQp7VncXVvQUqEN9wlnky4swBv40/view?usp=drivesdk
## 👩‍💻 Author

**Subhiksha H.S.**
- GitHub: https://github.com/Subhiksha-HS

