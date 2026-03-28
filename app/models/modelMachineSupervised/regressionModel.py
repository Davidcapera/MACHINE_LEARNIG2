import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df: pd.DataFrame = pd.read_csv("app/data/advertising.csv")

X: pd.DataFrame = df[["TV", "radio", "newspaper"]]
y: pd.Series    = df["sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

model: LinearRegression = LinearRegression()
model.fit(X_train, y_train)

y_pred_test: np.ndarray = model.predict(X_test)

_mae:      float = mean_absolute_error(y_test, y_pred_test)
_mse:      float = mean_squared_error(y_test, y_pred_test)
_rmse:     float = np.sqrt(_mse)
_r2_test:  float = r2_score(y_test, y_pred_test)
_r2_train: float = model.score(X_train, y_train)


def calculateSales(tv: float, radio: float, newspaper: float) -> float:
    prediction: float = model.predict([[tv, radio, newspaper]])[0]
    return round(float(prediction), 2)


def getRegressionGraph() -> str:
    features: list[str] = ["TV", "radio", "newspaper"]
    colors:   list[str] = ["#6c63ff", "#ff6584", "#43d9ad"]
    means:    dict      = {f: df[f].mean() for f in features}

    fig, axes = plt.subplots(1, 3, figsize=(15, 4), facecolor="#0f1117")
    fig.suptitle("Linear Regression – Advertising Dataset",
                 color="white", fontsize=13, fontweight="bold")

    for ax, column, color in zip(axes, features, colors):
        ax.set_facecolor("#1a1d27")
        ax.scatter(df[column], df["sales"], color=color, alpha=0.55, s=40, zorder=3)

        x_range: np.ndarray = np.linspace(df[column].min(), df[column].max(), 200)
        input_grid: np.ndarray = np.column_stack([
            x_range if f == column else np.full(200, means[f])
            for f in features
        ])

        ax.plot(x_range, model.predict(input_grid), color="white", linewidth=2, zorder=4)
        ax.set_xlabel(column, color="white", fontsize=10)
        ax.set_ylabel("Sales",  color="white", fontsize=10)
        ax.tick_params(colors="white", labelsize=8)
        for spine in ax.spines.values():
            spine.set_edgecolor("#2a2d3e")

    plt.tight_layout()

    buf: io.BytesIO = io.BytesIO()
    plt.savefig(buf, format="png", dpi=100, bbox_inches="tight", facecolor="#0f1117")
    buf.seek(0)
    img: str = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    return img


def getCurrentvsPredictedGraph() -> str:
    fig, ax = plt.subplots(figsize=(5, 4), facecolor="#0f1117")
    ax.set_facecolor("#1a1d27")
    ax.scatter(y_test, y_pred_test, color="#6c63ff", alpha=0.7, s=45, zorder=3)

    lims: list[float] = [
        min(y_test.min(), y_pred_test.min()),
        max(y_test.max(), y_pred_test.max())
    ]
    ax.plot(lims, lims, color="#43d9ad", linewidth=1.5, linestyle="--",
            label="Perfect fit", zorder=4)

    ax.set_xlabel("Actual Sales",    color="white", fontsize=10)
    ax.set_ylabel("Predicted Sales", color="white", fontsize=10)
    ax.set_title("Actual vs Predicted (Test Set)",
                 color="white", fontsize=11, fontweight="bold")
    ax.tick_params(colors="white", labelsize=8)
    ax.legend(facecolor="#1a1d27", labelcolor="white", fontsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor("#2a2d3e")

    plt.tight_layout()

    buf: io.BytesIO = io.BytesIO()
    plt.savefig(buf, format="png", dpi=100, bbox_inches="tight", facecolor="#0f1117")
    buf.seek(0)
    img: str = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    return img


def getStats() -> dict:
    return {
        "coef_tv":        round(float(model.coef_[0]), 4),
        "coef_radio":     round(float(model.coef_[1]), 4),
        "coef_newspaper": round(float(model.coef_[2]), 4),
        "intercept":      round(float(model.intercept_), 4),
        "total_samples":  len(df),
        "train_samples":  len(X_train),
        "test_samples":   len(X_test),
        "r2_train":       round(float(_r2_train), 4),
        "r2_test":        round(float(_r2_test),  4),
        "mae":            round(float(_mae),  4),
        "mse":            round(float(_mse),  4),
        "rmse":           round(float(_rmse), 4),
    }