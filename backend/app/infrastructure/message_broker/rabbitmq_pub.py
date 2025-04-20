import pika
from app.core.config import RABBITMQ_URL

class RabbitMQPublisher:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(RABBITMQ_URL)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='turnos')
        
    def publicar(self, mensaje: str):
        self.channel.basic_publish(
            exchange='',
            routing_key='turnos',
            body=mensaje
        )