import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_curve,
    auc
)

df = pd.read_csv("app/data/weatherAUS.csv")
df = df.dropna()

X = df[["MinTemp", "MaxTemp", "Rainfall", "Humidity3pm"]]
y = df["RainTomorrow"].map({"No": 0, "Yes": 1})

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = SGDClassifier(loss="log_loss")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_scores = model.decision_function(X_test)

fpr, tpr, _ = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)

metrics = {
    "accuracy": float(np.round(accuracy_score(y_test, y_pred), 3)),
    "precision": float(np.round(precision_score(y_test, y_pred, zero_division=0), 3)),
    "recall": float(np.round(recall_score(y_test, y_pred, zero_division=0), 3)),
    "f1": float(np.round(f1_score(y_test, y_pred, zero_division=0), 3)),
    "auc": float(np.round(roc_auc, 3))
}

# ROC Curve
plt.figure()
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - SGD Classifier")
plt.legend()
plt.savefig("app/static/generated/sgd_roc.png")
plt.close()

# Confusion Matrix sin seaborn
cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots()
im = ax.imshow(cm, interpolation="nearest", cmap="Blues")
plt.colorbar(im, ax=ax)

classes = ["No Rain", "Rain"]
tick_marks = np.arange(len(classes))
ax.set_xticks(tick_marks)
ax.set_xticklabels(classes)
ax.set_yticks(tick_marks)
ax.set_yticklabels(classes)

# Anotar cada celda con su valor
thresh = cm.max() / 2.0
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, format(cm[i, j], "d"),
                ha="center", va="center",
                color="white" if cm[i, j] > thresh else "black")

ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
ax.set_title("Confusion Matrix")
fig.tight_layout()
plt.savefig("app/static/generated/sgd_confusion.png")
plt.close()


def predict(features):
    prediction = model.predict(features)
    return prediction[0]


def get_metrics():
    return metrics


def interpret_metrics(metrics):
    interpretation = {
        "accuracy": "Overall correctness of the model",
        "precision": "Correct rain predictions",
        "recall": "Rain detection capability",
        "f1": "Balance precision-recall",
        "auc": "ROC curve performance"
    }
    return interpretation


def get_dataset_stats():
    total_samples = len(X)
    train_samples = len(X_train)
    test_samples = len(X_test)
    return {
        "total_samples": total_samples,
        "train_samples": train_samples,
        "test_samples": test_samples
    }