from flask import Blueprint, render_template, request
from app.models.weatherModel import predict, initial_data

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/caseWeather", methods=["GET"])
def home():
    temperature = 20
    humidity    = 34
    data   = {"temperature": temperature, "humidity": humidity}
    result = predict(temperature, humidity)
    return render_template("weather2.html", result=result,
                           data=data, initialData=initial_data)