import numpy as np
from sklearn.linear_model import LinearRegression

# Training dataset
# [advertising, price]
X = np.array([
    [100, 10],
    [200, 9],
    [300, 8],
    [400, 7],
    [500, 6],
    [600, 5],
    [700, 4],
    [800, 3],
    [900, 2],
    [1000, 1]
])

# sales
y = np.array([
    120,
    150,
    200,
    260,
    320,
    400,
    480,
    560,
    650,
    740
])

# Train model
model = LinearRegression()
model.fit(X, y)


def predict(advertising: float, price: float) -> float:
    prediction = model.predict([[advertising, price]])
    return round(prediction[0], 2)