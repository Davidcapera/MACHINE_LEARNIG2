import pandas as  pd 
import matplotlib as ma
import io
import base64 
from sklearn.linear_model import LinearRegression

data = {
    "Study Hours": [10, 15, 12, 8, 14, 5, 16, 7, 11, 13, 9, 4, 18, 3, 17, 6, 14, 2, 20, 1],
    "Final Grade": [3.8, 4.2, 3.6, 3, 4.5, 2.5, 4.8, 2.8, 3.7, 4, 3.2, 2.2, 5, 1.8, 4.9, 2.7, 4.4, 1.5, 5, 1]
}

df = pd.read_csv("app/data/advertising.csv")

x= df[["TV","radio","newspaper"]]
y= df[["sales"]]

model = LinearRegression()
model.fit(x,y)

def CalculateGrate (tv,radio,newspaper):
    result = model.predict([[tv,radio,newspaper]]) [0]
    return round(result,2)