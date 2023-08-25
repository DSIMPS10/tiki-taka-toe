# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cjkzylyi:VpI-J8Z0iO9MfUmsrw00wVos8ELYnZtL@trumpet.db.elephantsql.com/cjkzylyi'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# def create_app():
#     app = Flask(__name__)
#     db.init_app(app)
#     return app

# db = SQLAlchemy(app)

# class Football_teams(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     team_name = db.Column(db.String(100), unique=True)
#     league = db.Column(db.String(100))
#     country = db.Column(db.String(100))

# class Players(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(100))
#     last_name = db.Column(db.String(100))
#     team_id = db.Column(db.Integer)

# db.create_all()