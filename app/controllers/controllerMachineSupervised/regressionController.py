from flask import Blueprint, render_template, request
from app.models.modelMachineSupervised.regressionModel import (
    calculateSales,
    getRegressionGraph,
    getCurrentvsPredictedGraph,
    getStats,
)

regression_bp = Blueprint("regression", __name__)


@regression_bp.route("/regression", methods=["GET", "POST"])
def index():
    result, error = None, None
    graph = getRegressionGraph()
    avpGraph = getCurrentvsPredictedGraph()
    stats = getStats()

    if request.method == "POST":
        try:
            tv = float(request.form["tv"])
            radio = float(request.form["radio"])
            newspaper = float(request.form["newspaper"])

            if tv < 0 or radio < 0 or newspaper < 0:
                raise ValueError("All budget values must be non-negative")

            result = calculateSales(tv, radio, newspaper)

        except (ValueError, KeyError) as e:
            error = str(e)

    return render_template(
        "templateMachineSupervised/linearRegression.html",
        resultFinal=result,
        fail=error,
        imaGraph=graph,
        TrainGraph=avpGraph,
        stats=stats
    )

@regression_bp.route("/regression/definition")
def regression_definition():
    return render_template(
        "templateMachineSupervised/linearRegressionDefinition.html"
    )


@regression_bp.route("/classification/definition")
def classification_definition():
    return render_template(
        "templateMachineSupervised/classificationModelDefinition.html"
    )


@regression_bp.route("/classification")
def classification_app():
    return render_template(
        "templateMachineSupervised/classificationModel.html"
    )