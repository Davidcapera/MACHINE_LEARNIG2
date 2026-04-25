import numpy as np
from sklearn.cluster import KMeans

def run_kmeans():
    ingresos = np.random.randint(1000, 5000, 1000)
    gastos = np.random.randint(200, 2000, 1000)

    X = np.column_stack((ingresos, gastos))

    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X)

    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    data = []
    for i in range(len(X)):
        data.append({
            "ingresos": int(X[i][0]),
            "gasto": int(X[i][1]),
            "cluster": int(labels[i])
        })

    return data, centroids.tolist() 