from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HistoriaClinica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diagnosticos = db.Column(db.String(500))
    tratamientos = db.Column(db.String(500))
    notas = db.Column(db.String(500))
    adendas = db.relationship('Adenda', backref='historia_clinica', lazy=True)

class Adenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(40))
    tipo = db.Column(db.String(50))
    descripcion = db.Column(db.String(500))
    historia_clinica_id = db.Column(db.Integer, db.ForeignKey('historia_clinica.id'), nullable=False)

class Usuario(db.Model):
    documento = db.Column(db.String(15), primary_key=True)
    clave = db.Column(db.String(30), default='123')
    tipo = db.Column(db.String(30), default='default')
    foto = db.Column(db.String(255), default='default')
    nombre = db.Column(db.String(30), default='default')
    edad = db.Column(db.String(30), default='default')
    telefono = db.Column(db.String(30), default='default')
    sexo = db.Column(db.String(30), default='default')
    historia_clinica_id = db.Column(db.Integer, db.ForeignKey('historia_clinica.id'), unique=True, nullable=True)
    medico_id = db.Column(db.String(15), db.ForeignKey('usuario.documento'), unique=True, nullable=True)
    historia_clinica = db.relationship('HistoriaClinica', backref='usuario', lazy=True, uselist=False)
    medico = db.relationship('Usuario', backref='paciente', remote_side=[documento], uselist=False)