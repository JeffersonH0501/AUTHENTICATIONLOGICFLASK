from flask import request, jsonify
from flask.views import MethodView
from werkzeug import exceptions as http_exceptions
from sqlalchemy.orm.exc import NoResultFound
from app import app
from .models import Usuario
import jwt

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
            status_code = http_exceptions.HTTPStatus.OK
        else:
            respuesta_post = {}
            status_code = http_exceptions.HTTPStatus.OK

        return jsonify(respuesta_post), status_code
    
class HealthCheckView(MethodView):
    def get(self):
        return jsonify(status='ok')