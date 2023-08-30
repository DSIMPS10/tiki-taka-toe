import pytest

from flask_pkg.project import create_app, db # pylint: disable=import-error
from flask_pkg.project.config import get_env_db_url # pylint: disable=import-error
from flask_pkg.project.config import TestingConfig # pylint: disable=import-error

@pytest.yield_fixture()
def app():

    def _app(config_class):
        app = create_app(config_class)
        app.test_request_context().push()
        client = app.test_client()

        if config_class is TestingConfig:
        # always starting with an empty DB
            db.drop_all()
            from flask_pkg.project.models import Football_teams, Players # pylint: disable=import-error
            db.create_all()

        return app, client
    
    yield _app
    
    db.session.remove()
    if str(db.engine.url) == TestingConfig.SQLALCHEMY_DATABASE_URI:
        db.drop_all()

# @pytest.fixture()
# def client(app):
#     return app.test_client()