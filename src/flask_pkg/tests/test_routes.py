import pytest
import json

from src.flask_pkg.tests.conftest import app 
from src.flask_pkg.project import db 

from src.flask_pkg.project.models import Football_teams, Players
from src.flask_pkg.project.config import DevelopmentConfig, TestingConfig

def test_add_multiple_teams(app):
    test_app = app(DevelopmentConfig)
    app = test_app[0]
    client = test_app[1]
    test_array = []
    test_number = 3
    for i in range(test_number):
        test_team ={'team_name': f'Test_team_{i}',
                    'league': 'Test_league',
                    'country': 'England'
                    }
        test_array.append(test_team)
                
    activity_json = json.dumps(test_array)
    
    response = client.post("/api/post_teams", json=activity_json)

    assert response.status_code == 200
    assert Football_teams.query.count() == test_number
    assert Football_teams.query.first().activity_name == "Test_team_0"