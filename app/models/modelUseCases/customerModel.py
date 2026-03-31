def low_customer():

    age = 20
    income = 1000
    visits = 2

    spending = (0.1 * income) + (2 * visits) - age

    return {
        "name": "Low",
        "age": age,
        "income": income,
        "visits": visits,
        "spending": round(spending, 2)
    }


def medium_customer():

    age = 30
    income = 2000
    visits = 5

    spending = (0.1 * income) + (2 * visits) - age

    return {
        "name": "Medium",
        "age": age,
        "income": income,
        "visits": visits,
        "spending": round(spending, 2)
    }


def high_customer():

    age = 40
    income = 4000
    visits = 10

    spending = (0.1 * income) + (2 * visits) - age

    return {
        "name": "High",
        "age": age,
        "income": income,
        "visits": visits,
        "spending": round(spending, 2)
    }