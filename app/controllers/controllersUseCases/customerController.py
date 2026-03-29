from flask import Blueprint, render_template, request

from app.models.modelUseCases.customerModel import (
    low_customer,
    medium_customer,
    high_customer
)

customer_bp = Blueprint(
    "customer",
    __name__
)


@customer_bp.route("/customer")
def customer():

    case = request.args.get("case")

    example = None

    if case == "low":
        example = low_customer()

    elif case == "medium":
        example = medium_customer()

    elif case == "high":
        example = high_customer()

    return render_template(
        "templateUseCases/customer.html",
        example=example
    )