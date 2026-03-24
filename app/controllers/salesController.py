from flask import Blueprint, render_template, request
from app.models.salesModel import predict

sales_bp = Blueprint("sales", __name__)

@sales_bp.route("/sales", methods=["GET", "POST"])
def sales():

    prediction = None

    if request.method == "POST":
        advertising = float(request.form["advertising"])
        price = float(request.form["price"])

        prediction = predict(advertising, price)

    return render_template("sales.html", prediction=prediction)