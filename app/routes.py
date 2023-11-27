from flask import Flask, request, jsonify
import jwt
from flask.views import MethodView
from flask_api import status 
from .models import Usuario
from sqlalchemy.orm.exc import NoResultFound

def verificar_usuario(documento, clave):
    try:
        usuario = Usuario.query.filter_by(documento=documento, clave=clave).one()
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
            token = jwt.encode(token_payload, app.config['SECRET_KEY'], algorithm="HS256")

            respuesta_post = {"token": token}
            status_code = status.HTTP_200_OK
        else:
            respuesta_post = {}
            status_code = status.HTTP_401_UNAUTHORIZED

        return jsonify(respuesta_post), status_code
    
class HealthCheckView(MethodView):
    def get(self):
        return jsonify(status='ok')