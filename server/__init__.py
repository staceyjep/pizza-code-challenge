from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions without app first
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import and register blueprints
    from server.controllers import pizza_controller, restaurant_controller, restaurant_pizza_controller
    app.register_blueprint(pizza_controller.bp)
    app.register_blueprint(restaurant_controller.bp)
    app.register_blueprint(restaurant_pizza_controller.bp)
    
    return app