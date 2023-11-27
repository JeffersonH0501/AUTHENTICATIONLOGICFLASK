from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
admin = Admin()

def create_app():
    app = Flask(__name__)

    from config import Config

    app.config.from_object(Config)
    db.init_app(app)
    admin.init_app(app)

    from .models import Usuario

    admin.add_view(ModelView(Usuario, db.session))

    from app.routes import AutenticacionAPI, HealthCheckView

    app.add_url_rule('/autenticacion/', view_func=AutenticacionAPI.as_view('autenticacion'))
    app.add_url_rule('/health-check/', view_func=HealthCheckView.as_view('health_check'))

    return app