from flask import Blueprint, render_template
from app.models.modelUnsupervised.kmeansModel import run_kmeans, get_dataset_stats

kmeans_bp = Blueprint("kmeans", __name__)

@kmeans_bp.route("/kmeans")
def kmeans():
    results = run_kmeans()
    stats   = get_dataset_stats()
    return render_template("templateUnsupervised/kmeans.html", results=results, stats=stats)

@kmeans_bp.route('/kmeans/definition')
def kmeans_home():
    return render_template('templateUnsupervised/kmeansDefinition.html')