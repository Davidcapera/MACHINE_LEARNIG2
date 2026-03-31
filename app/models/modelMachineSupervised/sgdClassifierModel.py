from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc
from sklearn.datasets import load_iris
import numpy as np

# Dataset real
dataset = load_iris()

X = dataset.data
y = dataset.target

# Convertir a binario
y = (y == 0).astype(int)

# División
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modelo
model = SGDClassifier(max_iter=1000, tol=1e-3)
model.fit(X_train, y_train)

# Predicción
y_pred = model.predict(X_test)

# Probabilidades para ROC
y_scores = model.decision_function(X_test)

# ROC REAL
fpr, tpr, _ = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)

# Métricas
metrics = {
    "accuracy": float(round(accuracy_score(y_test, y_pred), 2)),
    "precision": float(round(precision_score(y_test, y_pred), 2)),
    "recall": float(round(recall_score(y_test, y_pred), 2)),
    "f1": float(round(f1_score(y_test, y_pred), 2)),
    "confusion": confusion_matrix(y_test, y_pred).tolist(),
    "fpr": fpr.tolist(),
    "tpr": tpr.tolist(),
    "auc": float(round(roc_auc, 2))
}

def predict(features):
    features_array = np.array(features).reshape(1, -1)
    return int(model.predict(features_array)[0])

def get_metrics():
    return metrics

def interpret_metrics(metrics):
    if metrics["accuracy"] > 0.8:
        return "The model shows excellent performance."
    elif metrics["accuracy"] > 0.6:
        return "The model has acceptable performance."
    else:
        return "The model performance is low and needs improvement."