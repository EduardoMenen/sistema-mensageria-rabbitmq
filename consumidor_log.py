import pika
import json
from config import RABBIT_CONFIG

params = pika.URLParameters(RABBIT_CONFIG)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='log_queue')
channel.queue_bind(exchange='user_events', queue='log_queue', routing_key='user.login')
channel.queue_bind(exchange='user_events', queue='log_queue', routing_key='user.upload')
channel.queue_bind(exchange='user_events', queue='log_queue', routing_key='user.logout')

def callback(ch, method, properties, body):
    mensagem = json.loads(body)
    print(f"[LOG] {mensagem['user']} executou o evento: {mensagem['event']}")

channel.basic_consume(
    queue='log_queue',
    on_message_callback=callback,
    auto_ack=True
)

print("Consumidor da log_queue aguardando mensagens...")
channel.start_consuming()
