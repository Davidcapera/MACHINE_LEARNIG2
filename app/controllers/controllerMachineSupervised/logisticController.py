from flask import Blueprint, render_template, request
from app.models.modelMachineSupervised.logisticModel import (predict_rain, get_stats,
                                   get_feature_graph, get_roc_graph,
                                   get_confusion_matrix_graph)

logistic_bp = Blueprint("logistic", __name__)


@logistic_bp.route("/rain-prediction", methods=["GET", "POST"])
def rain_prediction():
    result      = None
    rain_prob   = None
    fail        = None

    if request.method == "POST":
        try:
            temperature = float(request.form["temperature"])
            humidity    = float(request.form["humidity"])
            wind_speed  = float(request.form["wind_speed"])
            cloud_cover = float(request.form["cloud_cover"])
            pressure    = float(request.form["pressure"])

            result, rain_prob = predict_rain(
                temperature, humidity, wind_speed, cloud_cover, pressure
            )
        except (ValueError, KeyError):
            fail = "Please enter valid numbers in all fields."

    return render_template(
        "templateMachineSupervised/logisticRegression.html",
        stats        = get_stats(),
        featureGraph = get_feature_graph(),
        rocGraph     = get_roc_graph(),
        cmGraph      = get_confusion_matrix_graph(),
        result       = result,
        rain_prob    = rain_prob,
        fail         = fail,
    )


@logistic_bp.route("/logistic/definition")
def logistic_definition():
    return render_template(
        "templateMachineSupervised/logisticRegressionDefinition.html"
    )