from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
jwt = JWTManager(app)

from app.routes import AutenticacionAPI, HealthCheckView

# Rutas
app.add_url_rule('/autenticacion/', view_func=AutenticacionAPI.as_view('autenticacion'))
app.add_url_rule('/health-check/', view_func=HealthCheckView.as_view('health_check'))

