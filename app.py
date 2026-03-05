from flask import Flask, render_template, request

app = Flask(__name__)

datosIniciales = [
    {"ciudad": "Bogota",    "temp": 14, "humedad": 24, "clima": "Lluvioso"},
    {"ciudad": "Medellin",  "temp": 20, "humedad": 34, "clima": "Soleado"},
    {"ciudad": "Cartagena", "temp": 40, "humedad": 44, "clima": "Muy Soleado"},
]

def predecir(temperatura, humedad):

    if (temperatura >= 14 and temperatura < 20) and (humedad >= 24 and humedad < 34):
        return "Lluvioso"
    elif (temperatura >= 20 and temperatura < 40) and (humedad >= 34 and humedad < 44):
        return "Soleado"
    elif temperatura >= 40 and humedad > 44:
        return "Muy Soleado"
    else:
        return "Nublado"


@app.route("/", methods=["GET", "POST"])
def home():

    resultado = 0
    datos = {}

    if request.method == "POST":
        temperatura = int(request.form["temperatura"])
        humedad     = int(request.form["humedad"])
        datos = {"temperatura": temperatura,
                  "humedad": humedad}
        resultado = predecir(temperatura, humedad)

    return render_template("index.html",
        resultado      = resultado,
        datos          = datos,
        datosIniciales = datosIniciales
    )


@app.route('/FirstPage/<name>')
def firstPage(name = None):
        return render_template("index.html",
                               name=name)

