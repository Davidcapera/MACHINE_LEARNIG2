def predict(advertising: float, price: float) -> float:
    """
    Simple linear regression model for sales forecasting
    """

    sales = (5.2 * advertising) - (1.8 * price) + 120

    return round(sales, 2)