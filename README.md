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
## Entity Relationship (ER) Diagram

The following ER diagram represents the conceptual database design for the Human Development Index (HDI) Prediction System.

```mermaid
erDiagram

USER ||--o{ HDI_INPUT_DATA : submits
COUNTRY ||--o{ HDI_INPUT_DATA : has
HDI_INPUT_DATA ||--|| HDI_PREDICTION : generates
ML_MODEL ||--o{ HDI_PREDICTION : predicts
DATASET ||--o{ ML_MODEL : trains
HDI_PREDICTION ||--o{ VISUALIZATION_REPORT : creates
USER ||--o{ SESSION : starts

USER {
    int user_id PK
    string name
    string email
    string role
}

COUNTRY {
    int country_id PK
    string country_name
    string region
}

HDI_INPUT_DATA {
    int input_id PK
    float life_expectancy
    float mean_years_school
    float expected_years_school
    float gni
}

ML_MODEL {
    int model_id PK
    string algorithm
    float accuracy
}

HDI_PREDICTION {
    int prediction_id PK
    string predicted_category
}

DATASET {
    int dataset_id PK
    string dataset_name
}

VISUALIZATION_REPORT {
    int report_id PK
    string graph_type
}

SESSION {
    int session_id PK
    datetime login_time
}
```
## Entity Relationship (ER) Diagram

![ER Diagram](images/ER_Diagram.png)
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

## Project Output

![Project Output](images/output.png)

## Data Preprocessing

The dataset was preprocessed before model training by performing the following steps:

- Loaded the HDI dataset using Pandas.
- Checked for missing (null) values.
- Removed missing records using `dropna()`.
- Selected the independent variables:
  - Life Expectancy
  - Mean Years of Schooling
  - Expected Years of Schooling
  - Gross National Income (GNI)
- Selected the dependent variable:
  - HDI Category
- Applied Label Encoding to convert categorical HDI labels into numerical values.
- Split the dataset into training and testing sets using an 80:20 ratio.

## 🎥 Demo Video

Watch the complete project demonstration here:

**🔗 Demo Video:**  
https://drive.google.com/file/d/118ijjQp7VncXVvQUqEN9wlnky4swBv40/view?usp=drivesdk
## 👩‍💻 Author

**Subhiksha H.S.**
- GitHub: https://github.com/Subhiksha-HS

