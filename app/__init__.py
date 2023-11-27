from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from app.routes import AutenticacionAPI, HealthCheckView
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Rutas
app.add_url_rule('/autenticacion/', view_func=AutenticacionAPI.as_view('autenticacion'))
app.add_url_rule('/health-check/', view_func=HealthCheckView.as_view('health_check'))

