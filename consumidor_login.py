import pika
import json
from config import RABBIT_CONFIG

params = pika.URLParameters(RABBIT_CONFIG)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='login_queue')
channel.queue_bind(exchange='user_events', queue='login_queue', routing_key='user.login')

def callback(ch, method, properties, body):
    mensagem = json.loads(body)
    print(f"[LOGIN] {mensagem['user']} acabou de fazer login!")

channel.basic_consume(
    queue='login_queue',
    on_message_callback=callback,
    auto_ack=True
)

print("Consumidor da login_queue aguardando mensagens...")
channel.start_consuming()
