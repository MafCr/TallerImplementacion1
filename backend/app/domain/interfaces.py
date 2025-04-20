from abc import ABC, abstractmethod

class TurnoRepository(ABC):
    @abstractmethod
    def guardar(self, turno: Turno): ...
    
class MessageBroker(ABC):
    @abstractmethod
    def publicar(self, mensaje: str): ...