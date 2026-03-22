from flask import Blueprint, render_template, request
from app.models.regressionModel import CalculateGrate

regression_bp = Blueprint("regression", __name__)

@regression_bp.route("/regression", methods=["GET", "POST"])
def index():
    result, error = None, None
    if request.method == "POST":
        hours = float(request.form["Hours"])
        if hours <= 50:
            result = CalculateGrate(hours)
        else:
            error = "Las horas deben ser menores a 50"
    return render_template("linearRegression.html", resultFinal=result)