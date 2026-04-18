from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.controllers.controllersUseCases.weatherController import weather_bp
    from app.controllers.controllerMachineSupervised.regressionController import regression_bp
    from app.controllers.controllerIndex.indexController import index_bp
    from app.controllers.controllersUseCases.airController import air_bp 
    from app.controllers.controllersUseCases.salesController import sales_bp
    from app.controllers.controllersUseCases.customerController import customer_bp
    from app.controllers.controllerMachineSupervised.logisticController import logistic_bp
    from app.controllers.controllerMachineSupervised.sgdClassifierController import sgdClassifier_bp

    app.register_blueprint(weather_bp)
    app.register_blueprint(regression_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(air_bp) 
    app.register_blueprint(sales_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(logistic_bp)
    app.register_blueprint(sgdClassifier_bp)
    
    
    return app