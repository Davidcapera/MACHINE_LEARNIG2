from flask import Blueprint, render_template, request
from app.models.airModel import predict, initial_data, generate_tree

air_bp = Blueprint('air', __name__)

@air_bp.route('/air-quality', methods=['GET', 'POST'])
def air_quality():
    result = None
    data = {}

    generate_tree()

    if request.method == 'POST':
        pm25 = int(request.form.get('pm25', 0))
        pm10 = int(request.form.get('pm10', 0))

        result = predict(pm25, pm10)

        data = {
            'pm25': pm25,
            'pm10': pm10
        }

    return render_template(
        'air.html',
        result=result,
        data=data,
        initialData=initial_data
    )