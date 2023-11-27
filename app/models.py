from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HistoriaClinica(db.Model):
    id_hc = db.Column(db.Integer, primary_key=True)
    diagnosticos = db.Column(db.String(500))
    tratamientos = db.Column(db.String(500))
    notas = db.Column(db.String(500))
    usuario_id = db.Column(db.String(15), db.ForeignKey('usuario.documento'), nullable=True)

class Usuario(db.Model):
    documento = db.Column(db.String(15), primary_key=True)
    clave = db.Column(db.String(30), default='a')
    tipo = db.Column(db.String(30), default='a')
    nombre = db.Column(db.String(30), default='a')
    edad = db.Column(db.String(30), default='a')
    telefono = db.Column(db.String(30), default='a')
    sexo = db.Column(db.String(30), default='a')
    foto = db.Column(db.String(255), default='a')
    historia_clinica = db.relationship('HistoriaClinica', backref='usuario', uselist=False, cascade='all, delete-orphan')

class Adenda(db.Model):
    id_adenda = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(40))
    tipo = db.Column(db.String(50))
    descripcion = db.Column(db.String(500))
    historia_clinica_id = db.Column(db.Integer, db.ForeignKey('historia_clinica.id_hc'), nullable=False)

#db.init_app(app)
