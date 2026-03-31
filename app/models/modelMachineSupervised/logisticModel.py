import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             classification_report, roc_curve, roc_auc_score)
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("app/data/weatherconditions.csv")

FEATURES = ["Temperature", "Humidity", "Wind_Speed", "Cloud_Cover", "Pressure"]
TARGET   = "Rain"

x = df[FEATURES]
y = (df[TARGET] == "rain").astype(int)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

scaler  = StandardScaler()
x_train_sc = scaler.fit_transform(x_train)
x_test_sc  = scaler.transform(x_test)

model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(x_train_sc, y_train)


def predict_rain(temperature, humidity, wind_speed, cloud_cover, pressure):
    values    = [[temperature, humidity, wind_speed, cloud_cover, pressure]]
    scaled    = scaler.transform(values)
    pred      = model.predict(scaled)[0]
    proba     = model.predict_proba(scaled)[0]
    label     = "rain" if pred == 1 else "no rain"
    rain_prob = round(float(proba[1]) * 100, 1)
    return label, rain_prob


def get_stats():
    y_pred       = model.predict(x_test_sc)
    y_pred_train = model.predict(x_train_sc)
    cm           = confusion_matrix(y_test, y_pred)
    report       = classification_report(y_test, y_pred,
                                         target_names=["no rain", "rain"],
                                         output_dict=True)
    coef_dict = {feat: round(float(c), 4)
                 for feat, c in zip(FEATURES, model.coef_[0])}

    return {
        "total_samples" : len(df),
        "train_samples" : len(x_train),
        "test_samples"  : len(x_test),
        "rain_count"    : int(y.sum()),
        "no_rain_count" : int((y == 0).sum()),
        "accuracy_train": round(accuracy_score(y_train, y_pred_train), 4),
        "accuracy_test" : round(accuracy_score(y_test,  y_pred),       4),
        "precision_rain": round(report["rain"]["precision"], 4),
        "recall_rain"   : round(report["rain"]["recall"],    4),
        "f1_rain"       : round(report["rain"]["f1-score"],  4),
        "auc"           : round(roc_auc_score(y_test, model.predict_proba(x_test_sc)[:, 1]), 4),
        "cm"            : cm.tolist(),
        "coefficients"  : coef_dict,
        "intercept"     : round(float(model.intercept_[0]), 4),
    }


def get_feature_graph():
    stats = get_stats()
    fig, axes = plt.subplots(1, 5, figsize=(18, 4), facecolor="#f8f9fa")
    fig.suptitle("Feature Distribution — Rain vs No Rain", fontsize=12)

    colors = {"rain": "#0d6efd", "no rain": "#dc3545"}
    for ax, feat in zip(axes, FEATURES):
        ax.set_facecolor("#ffffff")
        for label, color in colors.items():
            subset = df[df[TARGET] == label][feat]
            ax.hist(subset, bins=25, alpha=0.6, color=color, label=label)
        ax.set_title(feat, fontsize=9)
        ax.set_xlabel(feat, fontsize=8)
        ax.set_ylabel("Count", fontsize=8)
        ax.legend(fontsize=7)
        for spine in ax.spines.values():
            spine.set_edgecolor("#dee2e6")

    plt.tight_layout()
    return _to_base64(fig)


def get_roc_graph():
    proba = model.predict_proba(x_test_sc)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, proba)
    auc = roc_auc_score(y_test, proba)

    fig, ax = plt.subplots(figsize=(5, 5), facecolor="#f8f9fa")
    ax.set_facecolor("#ffffff")
    ax.plot(fpr, tpr, color="#0d6efd", linewidth=2, label=f"AUC = {auc:.3f}")
    ax.plot([0, 1], [0, 1], "--", color="#adb5bd", linewidth=1)
    ax.set_xlabel("False Positive Rate", fontsize=10)
    ax.set_ylabel("True Positive Rate", fontsize=10)
    ax.set_title("ROC Curve", fontsize=11)
    ax.legend(fontsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor("#dee2e6")

    plt.tight_layout()
    return _to_base64(fig)


def get_confusion_matrix_graph():
    y_pred = model.predict(x_test_sc)
    cm     = confusion_matrix(y_test, y_pred)

    fig, ax = plt.subplots(figsize=(4, 4), facecolor="#f8f9fa")
    ax.set_facecolor("#ffffff")
    im = ax.imshow(cm, interpolation="nearest", cmap="Blues")
    plt.colorbar(im, ax=ax)
    labels = ["no rain", "rain"]
    ax.set_xticks([0, 1]); ax.set_xticklabels(labels, fontsize=9)
    ax.set_yticks([0, 1]); ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel("Predicted", fontsize=10)
    ax.set_ylabel("Actual", fontsize=10)
    ax.set_title("Confusion Matrix", fontsize=11)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, str(cm[i, j]), ha="center", va="center",
                    color="white" if cm[i, j] > cm.max() / 2 else "black",
                    fontsize=13, fontweight="bold")
    for spine in ax.spines.values():
        spine.set_edgecolor("#dee2e6")

    plt.tight_layout()
    return _to_base64(fig)


def _to_base64(fig):
    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=100, bbox_inches="tight")
    buf.seek(0)
    img = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    return img