import requests
from sqlalchemy import desc
import json

from flask import request, jsonify, render_template, redirect, url_for, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

from .extensions import db
# from .models import Athletes, Activities, Activity_maps, Activities_test

main = Blueprint("main", __name__)
