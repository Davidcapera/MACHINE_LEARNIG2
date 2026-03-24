from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt  
import numpy as np
import os
from typing import List, Dict, Union

X = np.array([
    [10, 20],
    [25, 50],
    [50, 90],
    [120, 150]
])

y = ["Good", "Moderate", "Unhealthy", "Hazardous"]
model = DecisionTreeClassifier()
model.fit(X, y)

def generate_tree() -> None:
    os.makedirs("app/static", exist_ok=True)

    plt.figure(figsize=(18, 12))
    plot_tree(
    model,
    feature_names=["PM2.5", "PM10"],
    class_names=["Good", "Moderate", "Unhealthy", "Hazardous"],
    filled=True,
    fontsize=10
)
    plt.savefig("app/static/tree.png")
    plt.close()

def predict(pm25: int, pm10: int) -> str:
    prediction = model.predict([[pm25, pm10]])
    return prediction[0]

initial_data: List[Dict[str, Union[int, str]]] = [
    {"pm25": 10, "pm10": 20, "quality": "Good"},
    {"pm25": 25, "pm10": 50, "quality": "Moderate"},
    {"pm25": 50, "pm10": 90, "quality": "Unhealthy"},
    {"pm25": 120, "pm10": 150, "quality": "Hazardous"},
]