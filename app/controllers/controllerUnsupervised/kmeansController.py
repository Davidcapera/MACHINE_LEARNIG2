from flask import Blueprint, render_template, request
from app.models.modelUnsupervised.kmeansModel import (
    run_kmeans,
    get_dataset_stats,
    run_dynamic_kmeans
)

kmeans_bp = Blueprint("kmeans", __name__)


@kmeans_bp.route("/kmeans")
def kmeans():

    results = run_kmeans()
    stats = get_dataset_stats()

    return render_template(
        "templateUnsupervised/kmeans.html",
        results=results,
        stats=stats
    )


@kmeans_bp.route('/kmeans/definition')
def kmeans_home():

    return render_template(
        'templateUnsupervised/kmeansDefinition.html'
    )


# APPLICATION PAGE
@kmeans_bp.route('/kmeans/application', methods=['GET', 'POST'])
def kmeans_application():

    prediction = None

    # Dataset stats for Application section
    stats = get_dataset_stats()

    if request.method == 'POST':

        age = float(request.form['age'])
        income = float(request.form['income'])

        prediction = run_dynamic_kmeans(age, income)

    return render_template(
        'templateUnsupervised/kmeansApplication.html',
        prediction=prediction,
        stats=stats
    )