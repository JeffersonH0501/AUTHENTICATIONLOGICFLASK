from flask import request, jsonify, current_app
from flask.views import MethodView
from sqlalchemy.orm.exc import NoResultFound
from .models import Usuario
import jwt
import hashlib
from cryptography.fernet import Fernet

cipher_suite = Fernet(current_app.config['SIMETRIC_KEY'].encode())

def cifrar_dato(dato):
    return cipher_suite.encrypt(dato.encode())

def hash_dato(dato):
    hash_object = hashlib.sha256(dato.encode())
    return hash_object.hexdigest()

def verificar_usuario(documento, clave):
    try:
        documento_cifrado = cifrar_dato(documento)
        hash_clave = hash_dato(clave)
        usuario = Usuario.query.filter_by(documento=documento_cifrado, clave=hash_clave).one()
    except NoResultFound:
        usuario = None

    return usuario

class AutenticacionAPI(MethodView):
    def post(self):
        data = request.get_json()

        documento = data.get("documento")
        clave = data.get("clave")

        usuario = verificar_usuario(documento, clave)

        if usuario is not None: 

            token_payload = {"documento": usuario.documento, "tipo": usuario.tipo}
            token = jwt.encode(token_payload, current_app.config['SECRET_KEY'], algorithm="HS256")

            respuesta_post = {"token": token}
            status_code = 200
        else:
            respuesta_post = {}
            status_code = 200

        return jsonify(respuesta_post), status_code
    
class HealthCheckView(MethodView):
    def get(self):
        return jsonify(status='ok')