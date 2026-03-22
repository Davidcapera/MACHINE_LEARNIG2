initial_data = [
    {"city": "Bogota",    "temp": 14, "humidity": 24, "weather": "Rainy"},
    {"city": "Medellin",  "temp": 20, "humidity": 34, "weather": "Sunny"},
    {"city": "Cartagena", "temp": 40, "humidity": 44, "weather": "Very Sunny"},
]

def predict(temperature: int, humidity: int) -> str:
    if (14 <= temperature < 20) and (24 <= humidity < 34):
        return "Rainy"
    elif (20 <= temperature < 40) and (34 <= humidity < 44):
        return "Sunny"
    elif temperature >= 40 and humidity >= 44:
        return "Very Sunny"
    return "Cloudy"