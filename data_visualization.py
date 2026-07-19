import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder
os.makedirs("visualizations", exist_ok=True)

# Load dataset
df = pd.read_csv("hdi.csv")

# -----------------------------
# Convert HDI categories to numbers
# -----------------------------
mapping = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Very High": 4
}

df["HDI_Score"] = df["HDI"].map(mapping)

# -----------------------------
# 1. Histogram
# -----------------------------
plt.figure(figsize=(6,4))
sns.histplot(df["LifeExpectancy"], bins=5, kde=True)
plt.title("Distribution of Life Expectancy")
plt.savefig("visualizations/life_expectancy_distribution.png")
plt.close()

# -----------------------------
# 2. Scatter Plot
# -----------------------------
plt.figure(figsize=(6,4))
sns.scatterplot(
    x="LifeExpectancy",
    y="HDI_Score",
    data=df
)
plt.title("Life Expectancy vs HDI")
plt.savefig("visualizations/life_expectancy_vs_hdi.png")
plt.close()

# -----------------------------
# 3. Correlation Heatmap
# -----------------------------
numeric = df[[
    "LifeExpectancy",
    "MeanYearsSchool",
    "ExpectedYearsSchool",
    "GNI",
    "HDI_Score"
]]

plt.figure(figsize=(7,6))
sns.heatmap(numeric.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("visualizations/correlation_heatmap.png")
plt.close()

# -----------------------------
# 4. Box Plot
# -----------------------------
plt.figure(figsize=(6,4))
sns.boxplot(y=df["GNI"])
plt.title("GNI Distribution")
plt.savefig("visualizations/gni_boxplot.png")
plt.close()

print("Graphs created successfully!")