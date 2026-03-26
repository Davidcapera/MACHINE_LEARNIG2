from flask import Blueprint, render_template, request
from app.models.salesModel import low_sales, medium_sales, high_sales

sales_bp = Blueprint("sales", __name__)

@sales_bp.route("/sales")
def sales():

    case = request.args.get("case")
    example = None

    if case == "low":
        example = low_sales()
        example["name"] = "Low Advertising"

    elif case == "medium":
        example = medium_sales()
        example["name"] = "Medium Advertising"

    elif case == "high":
        example = high_sales()
        example["name"] = "High Advertising"

    return render_template("sales.html", example=example)