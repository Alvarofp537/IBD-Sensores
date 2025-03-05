import pika, os, time
import json

with open('/data/ocupacion.csv', 'a') as f:
    # Create csv with header
    f.write('timestamp,occupancy,movement,location,dwell_time\n')

time.sleep(10)  # Wait for RabbitMQ container to initialize

rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'),os.getenv('RABBITMQ_PASSWORD'))

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host,credentials=rabbitmq_credentials))
channel = connection.channel(channel_number=2)

channel.queue_declare(queue='ocupacion')

def callback(ch, method, properties, body):
    data = json.load(body)
    linea = f"{data['timestamp']},{data['occupancy']},{data['movement']},{data['location']}, {data['dwell_time']}"
    with open('/data/ocupacion.csv', 'a') as f:
        f.write(linea + '\n')

channel.basic_consume(queue='ocupacion', on_message_callback=callback, auto_ack=True)

channel.start_consuming()