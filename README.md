#  ML Interactive Ap

An interactive web application built with **Flask** that lets you explore and apply **supervised Machine Learning** algorithms through real-world use cases. Designed with MVC architecture and focused on hands-on learning.

---

##  Table of Contents

- [Description](#-description)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Modules & Use Cases](#-modules--use-cases)
- [Datasets](#-datasets)

---

##  Description

**ML Interactive App** is an educational and interactive platform for exploring Machine Learning concepts. Users can input data, visualize predictions, and understand model behavior through dynamically generated charts and detailed statistical metrics.

The app includes **Linear Regression**, **Logistic Regression**, and **Decision Tree** models, alongside applied real-world use cases.

---

##  Features

-  **Sales prediction** using Multiple Linear Regression trained on advertising data
-  **Rain prediction** using Logistic Regression on meteorological data
-  **Air quality classification** using a Decision Tree (PM2.5 / PM10 inputs)
-  Dynamic charts generated with **Matplotlib** (Base64-encoded and rendered inline)
-  Evaluation metrics: R², MAE, MSE, RMSE, AUC-ROC, Confusion Matrix
-  Clean **MVC architecture** with Flask Blueprints
-  Responsive interface with **Jinja2** templates

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.x, Flask |
| Machine Learning | scikit-learn, NumPy, pandas |
| Visualization | Matplotlib |
| Frontend | HTML5, CSS3, Jinja2 |
| Data | CSV files (advertising, weatherconditions) |

---

##  Project Structure

```
app/
├── __init__.py                                      # Flask app factory (registers all blueprints)
│
├── controllers/
│   ├── controllerIndex/
│   │   └── indexController.py                       # Home route
│   ├── controllerMachineSupervised/
│   │   ├── regressionController.py                  # Linear regression routes
│   │   └── logisticController.py                    # Logistic regression routes
│   └── controllersUseCases/
│       ├── airController.py                         # Air quality use case
│       ├── customerController.py                    # Customer spending use case
│       ├── salesController.py                       # Sales forecasting use case
│       └── weatherController.py                     # Weather prediction use case
│
├── models/
│   ├── modelMachineSupervised/
│   │   ├── regressionModel.py                       # Linear regression model + graphs
│   │   └── logisticModel.py                         # Logistic regression model + graphs
│   └── modelUseCases/
│       ├── airModel.py                              # Decision tree for air quality
│       ├── customerModel.py                         # Customer spending simulation
│       ├── salesModel.py                            # Sales formula model
│       └── weatherModel.py                          # Rule-based weather predictor
│
├── templates/
│   ├── base.html                                    # Base layout
│   ├── templateHome/
│   │   └── index.html
│   ├── templateMachineSupervised/
│   │   ├── linearRegression.html
│   │   ├── linearRegressionDefinition.html
│   │   ├── logisticRegression.html
│   │   ├── logisticRegressionDefinition.html
│   │   ├── classificationModel.html
│   │   └── classificationModelDefinition.html
│   └── templateUseCases/
│       ├── air.html
│       ├── customer.html
│       ├── sales.html
│       └── weather2.html
│
├── data/
│   ├── advertising.csv                              # TV / Radio / Newspaper → Sales
│   └── weatherconditions.csv                        # Meteorological features → Rain
│
└── static/
    └── *.png                                        # Static images and pre-generated plots
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ml-interactive-app.git
cd ml-interactive-app
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask scikit-learn pandas numpy matplotlib
```

### 4. Run the application

```bash
flask --app app run
```

Then open your browser at `http://127.0.0.1:5000`

---

##  Usage

Once the server is running, navigate to the home page to access all available modules. Each section includes an explanation of the model and an interactive form where you can input values and receive predictions along with visualizations.

---

##  Modules & Use Cases

###  Linear Regression — Sales Prediction
**Route:** `/regression`

Trains a **Multiple Linear Regression** model on the Advertising dataset. Given a budget split across TV, Radio, and Newspaper, the model predicts the expected sales volume.

- **Input:** TV budget, Radio budget, Newspaper budget
- **Output:** Predicted sales (numeric)
- **Metrics:** R² (train/test), MAE, MSE, RMSE
- **Charts:** Feature vs. Sales scatter plots, Actual vs. Predicted graph

---

###  Logistic Regression — Rain Prediction
**Route:** `/rain-prediction`

Trains a **Logistic Regression** classifier (with StandardScaler normalization) on a weather dataset to predict whether it will rain given current atmospheric conditions.

- **Input:** Temperature, Humidity, Wind Speed, Cloud Cover, Pressure
- **Output:** Rain / No Rain + probability percentage
- **Metrics:** Accuracy (train/test), Precision, Recall, F1-Score, AUC
- **Charts:** Feature distributions, ROC Curve, Confusion Matrix

---

###  Air Quality — Decision Tree
**Route:** `/classification`

Uses a **Decision Tree Classifier** to categorize air quality based on PM2.5 and PM10 particle concentration levels.

| PM2.5 | PM10 | Quality |
|-------|------|---------|
| 10 | 20 | Good |
| 25 | 50 | Moderate |
| 50 | 90 | Unhealthy |
| 120 | 150 | Hazardous |

---

###  Customer Spending Simulator
**Route:** `/customer`

Simulates estimated customer spending using a linear formula based on age, income, and store visits. Three customer profiles are compared: Low, Medium, and High.

```
spending = (0.1 × income) + (2 × visits) − age
```

---

### Sales Forecasting
**Route:** `/sales`

Models projected sales based on advertising investment, product price, and demand using a rule-based linear equation. Compares Low, Medium, and High scenarios.

```
sales = (0.4 × advertising) − (2 × price) + (1.5 × demand)
```

---

###  Weather Prediction
**Route:** `/weather`

A simple rule-based predictor that classifies weather conditions (Rainy, Sunny, Very Sunny, Cloudy) based on temperature and humidity ranges, using Colombian cities as reference points.

---

##  Datasets

| File | Rows | Features | Target |
|------|------|----------|--------|
| `advertising.csv` | 200 | TV, Radio, Newspaper | Sales |
| `weatherconditions.csv` | ~14,000 | Temperature, Humidity, Wind Speed, Cloud Cover, Pressure | Rain |

---

##  License

This project is for educational purposes. Feel free to fork, modify, and use it as a learning resource.****
