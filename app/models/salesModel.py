def low_sales():
    advertising = 500
    price = 50
    demand = 60

    sales = (0.4 * advertising) - (2 * price) + (1.5 * demand)

    return {
        "advertising": advertising,
        "price": price,
        "demand": demand,
        "sales": round(sales, 2)
    }


def medium_sales():
    advertising = 1500
    price = 45
    demand = 75

    sales = (0.4 * advertising) - (2 * price) + (1.5 * demand)

    return {
        "advertising": advertising,
        "price": price,
        "demand": demand,
        "sales": round(sales, 2)
    }


def high_sales():
    advertising = 2500
    price = 40
    demand = 90

    sales = (0.4 * advertising) - (2 * price) + (1.5 * demand)

    return {
        "advertising": advertising,
        "price": price,
        "demand": demand,
        "sales": round(sales, 2)
    }