from flask import Blueprint, render_template
from app.models.modelUseCases.airModel import predict, initial_data, generate_tree

air_bp = Blueprint('air', __name__)

@air_bp.route('/air-quality')
def air_quality():

    generate_tree()
    data = {
        'pm25': 120,
        'pm10': 150
    }

    # predicción
    result = predict(data['pm25'], data['pm10'])

    return render_template(
        'templateUseCases/air.html',
        result=result,
        data=data,
        initialData=initial_data
    )