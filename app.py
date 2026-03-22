from flask import Flask, render_template, request

app = Flask(__name__)

initialData = [
    {"city": "Bogota",    "temp": 14, "humidity": 24, "weather": "Rainy"},
    {"city": "Medellin",  "temp": 20, "humidity": 34, "weather": "Sunny"},
    {"city": "Cartagena", "temp": 40, "humidity": 44, "weather": "very Sunny"},
]

def predit(temperature, humidity):

    if (temperature >= 14 and temperature < 20) and (humidity >= 24 and humidity < 34):
        return "Rainy"
    elif (temperature >= 20 and temperature < 40) and (humidity >= 34 and humidity < 44):
        return "Sunny"
    elif temperature >= 40 and humidity > 44:
        return "Very Sunny"
    else:
        return "Cloudy"


@app.route("/", methods=["GET", "POST"])
def home():

    result = 0
    data = {}

    if request.method == "POST":
        temperature = int(request.form["temperature"])
        humidity    = int(request.form["humidity"])
        data = {"temperature": temperature,
                  "humidity": humidity}
        result = predit(temperature, humidity)

    return render_template("index.html",
        result     = result,
        data          = data,
        initialData = initialData
    )


@app.route('/FirstPage/<name>')
def firstPage(name = None):
        return render_template("index.html",
                               name=name)

