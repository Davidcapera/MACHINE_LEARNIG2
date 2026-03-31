from flask import render_template, request
from app.models.modelMachineSupervised.sgdClassifierModel import predict, get_metrics, interpret_metrics

def sgdClassifier():

    result = None

    if request.method == "POST":
        f1 = float(request.form["f1"])
        f2 = float(request.form["f2"])
        f3 = float(request.form["f3"])
        f4 = float(request.form["f4"])

        prediction = predict([f1, f2, f3, f4])

        result = "🌧️ Rain Expected" if prediction == 1 else "☀️ No Rain"

    metrics = get_metrics()
    interpretation = interpret_metrics(metrics)

    return render_template(
        "templateMachineSupervised/sgdClassifier.html",
        result=result,
        metrics=metrics,
        interpretation=interpretation
    )