from flask import Blueprint, render_template
from app.models.modelMachineUnsupervised.kmeansModel import run_kmeans

kmeans_bp = Blueprint('kmeans', __name__)

@kmeans_bp.route('/kmeans')
def kmeans_home():
    return render_template('templateMachineUnsupervised/kmeans.html')

@kmeans_bp.route('/kmeans-manual')
def kmeans_manual():
    return render_template('templateMachineUnsupervised/kmeans_manual.html')


@kmeans_bp.route('/kmeans-app')
def kmeans_app():
    data, centroids = run_kmeans()

    centroids = centroids.tolist() if hasattr(centroids, "tolist") else centroids

    return render_template(
        'templateMachineUnsupervised/kmeans_app.html',
        data=data,
        centroids=centroids
    )