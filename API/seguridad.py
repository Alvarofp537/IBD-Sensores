import pika, os, time
import json

with open('/data/seguridad.csv', 'w') as f:
    # Create csv with header
    f.write('timestamp,status,alerts,alert_level\n')

time.sleep(20)  # Wait for RabbitMQ container to initialize

rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'),os.getenv('RABBITMQ_PASSWORD'))

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host,credentials=rabbitmq_credentials))
channel = connection.channel(channel_number=4)

channel.queue_declare(queue='seguridad')

def callback(ch, method, properties, body):
    data = json.loads(body.decode('utf-8'))
    try:
        linea = f"{data['id']},{data['timestamp']},{data['status']},{data['alerts']},{data['alert_level']}"
        with open('/data/seguridad.csv', 'a') as f:
            f.write(linea + '\n')
    except:
        print('El json no tiene los parámetros correctos: timestamp,status,alerts,alert_level')
    
channel.basic_consume(queue='seguridad', on_message_callback=callback, auto_ack=True)

channel.start_consuming()