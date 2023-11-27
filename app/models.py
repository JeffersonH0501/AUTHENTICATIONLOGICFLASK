from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

medico_paciente = db.Table(
    'medico_paciente',
    db.Column('usuario_documento', db.String(15), db.ForeignKey('usuario.documento')),
    db.Column('medico_documento', db.String(15), db.ForeignKey('usuario.documento'))
)

class HistoriaClinica(db.Model):
    id_hc = db.Column(db.Integer, primary_key=True)
    diagnosticos = db.Column(db.String(500))
    tratamientos = db.Column(db.String(500))
    notas = db.Column(db.String(500))
    usuario = db.relationship('Usuario', back_populates='historia_clinica')

medico_paciente = db.Table(
    'medico_paciente',
    db.Column('usuario_documento', db.String(15), db.ForeignKey('usuario.documento')),
    db.Column('medico_documento', db.String(15), db.ForeignKey('usuario.documento'))
)

class Usuario(db.Model):
    documento = db.Column(db.String(15), primary_key=True)
    clave = db.Column(db.String(30), default='a')
    tipo = db.Column(db.String(30), default='a')
    nombre = db.Column(db.String(30), default='a')
    edad = db.Column(db.String(30), default='a')
    telefono = db.Column(db.String(30), default='a')
    sexo = db.Column(db.String(30), default='a')
    foto = db.Column(db.String(255), default='a')
    historia_clinica_id = db.Column(db.Integer, db.ForeignKey('historia_clinica.id_hc'))
    historia_clinica = db.relationship('HistoriaClinica', back_populates='usuario', uselist=False)
    medico = db.relationship('Usuario', secondary='medico_paciente', primaryjoin='Usuario.documento==medico_paciente.c.medico_documento', secondaryjoin='Usuario.documento==medico_paciente.c.paciente_documento', back_populates='pacientes')

class Adenda(db.Model):
    id_adenda = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(40))
    tipo = db.Column(db.String(50))
    descripcion = db.Column(db.String(500))
    historia_clinica_id = db.Column(db.Integer, db.ForeignKey('historia_clinica.id_hc'))
    historia_clinica = db.relationship('HistoriaClinica', back_populates='adendas')