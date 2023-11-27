from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios_usuario'
    documento = db.Column(db.String(15))
    clave = db.Column(db.String(30), default='123')
    tipo = db.Column(db.String(30), default='default')
    foto = db.Column(db.String(255), default='default')
    nombre = db.Column(db.String(30), default='default')
    edad = db.Column(db.String(30), default='default')
    telefono = db.Column(db.String(30), default='default')
    sexo = db.Column(db.String(30), default='default')