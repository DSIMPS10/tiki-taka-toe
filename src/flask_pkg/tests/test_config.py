import pytest
import os

from flask_pkg.tests.conftest import app # pylint: disable=import-error
from flask_pkg.project.config import get_env_db_url,TestingConfig,DevelopmentConfig,ProductionConfig # pylint: disable=import-error


# @pytest.mark.skipif(
#     "TRAVIS" in os.environ and os.environ["TRAVIS"] == "True",
#     reason="Skipping this test on Travis CI.",
# )

def test_development_config(app):
    
    dev_app = app(DevelopmentConfig)
    app = dev_app[0]
    # client = test_app[1]
    DB_URL = get_env_db_url("development")
    assert app.config["DEBUG"]
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == DB_URL


def test_testing_config(app):
    test_app = app(TestingConfig)
    app = test_app[0]

    DB_URL = get_env_db_url("testing")
    assert app.config["DEBUG"]
    assert app.config["TESTING"]
    # assert not app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == DB_URL


def test_production_config(app):
    prod_app = app(ProductionConfig)
    app = prod_app[0]
    DB_URL = get_env_db_url("production")
    assert not app.config["DEBUG"]
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == DB_URL