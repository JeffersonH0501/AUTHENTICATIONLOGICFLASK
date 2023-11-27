from flask import request, jsonify, current_app
from flask.views import MethodView
from sqlalchemy.orm.exc import NoResultFound
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