from flask import Blueprint, render_template, request
from app.models.modelUseCases.weatherModel import predict, initial_data

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/caseWeather", methods=["GET", "POST"])
def home():
    result, data = None, {}
    if request.method == "POST":
        temperature = int(request.form["temperature"])
        humidity    = int(request.form["humidity"])
        data   = {"temperature": temperature, "humidity": humidity}
        result = predict(temperature, humidity)
    return render_template("templateUseCases/weather.html", result=result,
                           data=data, initialData=initial_data)