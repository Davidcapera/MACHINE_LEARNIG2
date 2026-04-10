import pandas as pd
from flask import Blueprint, render_template, request

from app.models.modelMachineSupervised.sgdClassifierModel import (
    predict,
    get_metrics,
    interpret_metrics,
    get_dataset_stats
)

sgdClassifier_bp = Blueprint("sgdClassifier", __name__)


@sgdClassifier_bp.route("/sgd-classifier", methods=["GET", "POST"])
def sgdClassifier():

    result = None

    if request.method == "POST":

        f1 = float(request.form["f1"])
        f2 = float(request.form["f2"])
        f3 = float(request.form["f3"])
        f4 = float(request.form["f4"])

        X = pd.DataFrame(
            [[f1, f2, f3, f4]],
            columns=["MinTemp", "MaxTemp", "Rainfall", "Humidity3pm"]
        )

        prediction = predict(X)

        result = " Rain Expected" if prediction == 1 else " No Rain"

    metrics = get_metrics()
    interpretation = interpret_metrics(metrics)
    stats = get_dataset_stats()

    return render_template(
        "templateMachineSupervised/classificationModel.html",
        result=result,
        metrics=metrics,
        interpretation=interpretation,
        stats=stats
    )


@sgdClassifier_bp.route("/classification/definition")
def classification_definition():
    return render_template(
        "templateMachineSupervised/classificationModelDefinition.html"
    )


@sgdClassifier_bp.route("/classification", methods=["GET", "POST"])
def classification_app():
    return render_template(
        "templateMachineSupervised/classificationModel.html"
    )