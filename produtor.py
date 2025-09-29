import pika
import json
from datetime import datetime, timezone
from config import RABBIT_CONFIG

params = pika.URLParameters(RABBIT_CONFIG)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange='user_events', exchange_type='direct')

usuarios = ['João']
eventos = ['user.login', 'user.upload', 'user.logout']

for user in usuarios:
    for event in eventos:
        mensagem = {
            "user": user,
            "event": event,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        channel.basic_publish(
            exchange='user_events',
            routing_key=event,
            body=json.dumps(mensagem)
        )
        print(f"Produtor enviou: {mensagem}")
        
connection.close()
