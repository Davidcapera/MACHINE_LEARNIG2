import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io, base64
from sklearn.datasets import make_blobs

np.random.seed(42)
X_raw, _ = make_blobs(n_samples=100, centers=3, n_features=2,
                      cluster_std=1.5, random_state=42)

ages    = np.interp(X_raw[:, 0], (X_raw[:, 0].min(), X_raw[:, 0].max()), (20, 65)).round(1)
incomes = np.interp(X_raw[:, 1], (X_raw[:, 1].min(), X_raw[:, 1].max()), (1000, 8000)).round(1)
DATA = np.column_stack([ages, incomes])

COLORS        = ["#0d6efd", "#dc3545", "#198754"]
CLUSTER_NAMES = ["Cluster A", "Cluster B", "Cluster C"]
BADGE_COLORS  = ["primary",   "danger",    "success"]

def euclidean(a, b):
    return float(np.sqrt(np.sum((a - b) ** 2)))

def fig_to_b64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=110,
                facecolor=fig.get_facecolor())
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)
    return encoded

def run_kmeans():
    centroids = DATA[[10, 50, 85]].copy().astype(float)

    iterations_data  = []
    variance_history = []

    for it in range(3):
        
        distances   = np.array([[euclidean(p, c) for c in centroids] for p in DATA])
        assignments = np.argmin(distances, axis=1)

        
        variance = sum(
            float(np.sum((DATA[assignments == k] - centroids[k]) ** 2))
            for k in range(3) if (assignments == k).any()
        )
        variance_history.append(round(variance, 2))

        
        dist_table = [
            {
                "point":       i + 1,
                "age":         round(DATA[i, 0], 1),
                "income":      round(DATA[i, 1], 1),
                "d_c1":        round(distances[i, 0], 2),
                "d_c2":        round(distances[i, 1], 2),
                "d_c3":        round(distances[i, 2], 2),
                "cluster":     CLUSTER_NAMES[assignments[i]],
                "cluster_idx": int(assignments[i]),
            }
            for i in range(10)
        ]

        
        fig, ax = plt.subplots(figsize=(6, 4.5))
        fig.patch.set_facecolor("white")
        ax.set_facecolor("#f8f9fa")
        for k in range(3):
            mask = assignments == k
            ax.scatter(DATA[mask, 0], DATA[mask, 1],
                       color=COLORS[k], alpha=0.7, s=55, label=CLUSTER_NAMES[k])
            ax.scatter(centroids[k, 0], centroids[k, 1],
                       color=COLORS[k], marker="X", s=220,
                       edgecolors="black", linewidths=1.2, zorder=5)
        ax.set_xlabel("Age (years)", fontsize=11)
        ax.set_ylabel("Income ($)", fontsize=11)
        ax.set_title(f"Iteration {it + 1} — Cluster Assignment", fontsize=12, fontweight="bold")
        ax.legend(fontsize=9)
        ax.grid(True, linestyle="--", alpha=0.4)
        scatter_img = fig_to_b64(fig)

        new_centroids = np.array([
            DATA[assignments == k].mean(axis=0) if (assignments == k).any() else centroids[k]
            for k in range(3)
        ])

        iterations_data.append({
            "num":           it + 1,
            "centroids":     [{"x": round(c[0], 2), "y": round(c[1], 2)} for c in centroids],
            "dist_table":    dist_table,
            "scatter_img":   scatter_img,
            "cluster_sizes": [int((assignments == k).sum()) for k in range(3)],
            "variance":      round(variance, 2),
        })

        centroids = new_centroids

    fig2, ax2 = plt.subplots(figsize=(7, 3.8))
    fig2.patch.set_facecolor("white")
    ax2.set_facecolor("#f8f9fa")
    ax2.plot([1, 2, 3], variance_history, color="#0d6efd", marker="o",
             linewidth=2.5, markersize=9, markerfacecolor="#dc3545",
             label="Intra-cluster variance")
    for i, v in enumerate(variance_history):
        ax2.annotate(f"{v:,.0f}", (i + 1, v),
                     textcoords="offset points", xytext=(0, 11),
                     fontsize=9, ha="center", color="#0d6efd", fontweight="bold")
    ax2.set_xlabel("Iteration", fontsize=11)
    ax2.set_ylabel("Intra-cluster variance", fontsize=11)
    ax2.set_title("Convergence — Variance per Iteration", fontsize=12, fontweight="bold")
    ax2.set_xticks([1, 2, 3])
    ax2.grid(True, linestyle="--", alpha=0.4)
    ax2.legend(fontsize=9)
    variance_img = fig_to_b64(fig2)

    return {
        "iterations":    iterations_data,
        "variance":      variance_history,
        "variance_img":  variance_img,
        "cluster_names": CLUSTER_NAMES,
        "badge_colors":  BADGE_COLORS,
        "stats": {
            "total_samples": len(DATA),
        },
        "data_preview": [
            {"id": i + 1, "age": round(DATA[i, 0], 1), "income": round(DATA[i, 1], 1)}
            for i in range(10)
        ],
    }


def get_dataset_stats():
    return {"total_samples": len(DATA), "features": 2, "clusters": 3, "iterations": 3}