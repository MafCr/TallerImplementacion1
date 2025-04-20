from flask import Blueprint, jsonify, request
from app.application.services import TurnoService
from app.infrastructure.repository.sqlite_repo import SQLiteTurnoRepository
from app.infrastructure.message_broker.rabbitmq_pub import RabbitMQPublisher

turnos_bp = Blueprint('turnos', __name__)
repo = SQLiteTurnoRepository()
broker = RabbitMQPublisher()
service = TurnoService(repo, broker)

@turnos_bp.route('/turnos', methods=['POST'])
def crear_turno():
    data = request.json
    turno = Turno(
        id=data['id'],
        estado="pendiente",
        datos=data
    )
    service.crear_turno(turno)
    return jsonify({"message": "Turno creado"}), 201