import os
from flask import Flask
from dotenv import load_dotenv # pylint: disable=import-error

from .extensions import db
from .routes import main
from .config import DevelopmentConfig, ProductionConfig

# App Factory
def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        db.init_app(app)
        app.register_blueprint(main)

    return app

### RUN FROM CLI ###
# From folder: flask_pkg
# Run: flask --app project run --debug

### For Windows ###
# python -m flask --app project run --debug