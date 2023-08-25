import os
from flask import Flask
from dotenv import load_dotenv
from .extensions import db
from .routes import main

from .config import DevelopmentConfig, ProductionConfig


### Load environment variables ###
load_dotenv()
url = os.getenv("POSTGRES_URL")
host = os.getenv("HOST")
database = os.getenv("DATABASE")
pg_user = os.getenv("PG_USER")
password = os.getenv("PASSWORD")

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