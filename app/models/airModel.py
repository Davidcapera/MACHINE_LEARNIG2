from typing import List, Dict

initial_data: List[Dict[str, int | str]] = [
    {"pm25": 10, "pm10": 20, "quality": "Good"},
    {"pm25": 25, "pm10": 50, "quality": "Moderate"},
    {"pm25": 50, "pm10": 100, "quality": "Unhealthy"},
]

def predict(pm25: int, pm10: int) -> str:
    if pm25 < 15 and pm10 < 30:
        return "Good"
    elif 15 <= pm25 < 40 and 30 <= pm10 < 80:
        return "Moderate"
    elif 40 <= pm25 < 70 or 80 <= pm10 < 120:
        return "Unhealthy"
    else:
        return "Hazardous"