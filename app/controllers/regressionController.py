from flask import Blueprint, render_template, request
from app.models.regressionModel import CalculateGrate

regression_bp = Blueprint("regression", __name__)

@regression_bp.route("/regression", methods=["GET", "POST"])
def index():
    result, error = None, None
    if request.method == "POST":
        try:
            tv = float(request.form["tv"])
            radio =float(request.form["radio"])
            newspaper =float(request.form["newspaper"])
            result = CalculateGrate(tv,radio,newspaper)
        except Exception as e:
            error=str(e)
        
    return render_template("linearRegression.html", resultFinal=result,fail=error)