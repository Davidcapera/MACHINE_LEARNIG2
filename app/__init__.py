from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.controllers.controllersUseCases.weatherController import weather_bp
    from app.controllers.controllerMachineSupervised.regressionController import regression_bp
    from app.controllers.indexController import index_bp
    app.register_blueprint(weather_bp)
    app.register_blueprint(regression_bp)
    app.register_blueprint(index_bp)

    return app