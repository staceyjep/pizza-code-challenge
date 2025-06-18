from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    Migrate(app, db)

    from .controllers.restaurant_controller import restaurant_bp
    app.register_blueprint(restaurant_bp)

    return app
