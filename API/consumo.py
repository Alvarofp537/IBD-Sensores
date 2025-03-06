import pika, os, time
import json

with open('/data/consumo.csv', 'w') as f:
    # Create csv with header
    f.write('id,timestamp,power_consumption,voltage,current,power_factor\n')

time.sleep(20)  # Wait for RabbitMQ container to initialize

rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'),os.getenv('RABBITMQ_PASSWORD'))

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host,credentials=rabbitmq_credentials))
channel = connection.channel(channel_number=3)

channel.queue_declare(queue='consumo')

def callback(ch, method, properties, body):
    data = json.loads(body.decode('utf-8'))
    try:
        linea = f"{data['id']},{data['timestamp']},{data['power_consumption']},{data['voltage']},{data['current']}, {data['power_factor']}"
        with open('/data/consumo.csv', 'a') as f:
            f.write(linea + '\n')
    except:
        print('El json no tiene los parámetros correctos: timestamp,power_consumption,voltage,current,power_factor')

channel.basic_consume(queue='consumo', on_message_callback=callback, auto_ack=True)

channel.start_consuming()