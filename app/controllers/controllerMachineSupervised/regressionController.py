from flask import Blueprint, render_template, request
from app.models.regressionModel import CalculateGrate

regression_bp = Blueprint("regression", __name__)

# Linear Regression - Application
@regression_bp.route("/regression", methods=["GET", "POST"])
def regression():

    result, error = None, None

    if request.method == "POST":
        hours = float(request.form["Hours"])

        if hours <= 50:
            result = CalculateGrate(hours)
        else:
            error = "Hours must be less than 50"

    return render_template(
        "linearRegression.html",
        resultFinal=result
    )


# Linear Regression - Definition
@regression_bp.route("/regression/definition")
def regression_definition():
    return render_template("linearRegressionDefinition.html")