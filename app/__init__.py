from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.controllers.weatherController import weather_bp
    from app.controllers.regressionController import regression_bp
    from app.controllers.indexController import index_bp
    from app.controllers.customerController import customer_bp
    from app.controllers.airController import air_bp 
    from app.controllers.salesController import sales_bp

    app.register_blueprint(weather_bp)
    app.register_blueprint(regression_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(air_bp) 
    app.register_blueprint(sales_bp)
    app.register_blueprint(customer_bp)
    return app