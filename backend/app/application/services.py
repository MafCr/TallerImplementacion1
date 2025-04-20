from app.domain.interfaces import TurnoRepository, MessageBroker

class TurnoService:
    def __init__(self, repo: TurnoRepository, broker: MessageBroker):
        self.repo = repo
        self.broker = broker
        
    def crear_turno(self, turno: Turno):
        # Lógica de negocio
        self.repo.guardar(turno)
        self.broker.publicar(f"Nuevo turno: {turno.id}")