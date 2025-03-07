from flask import Flask, jsonify, request
import requests
import pika, os, time, json

app = Flask(__name__)


def connect_rabbitmq():
    """Establece la conexión con RabbitMQ y maneja reintentos."""
    max_retries = 5
    retry_delay = 5  # segundos

    for attempt in range(max_retries):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=os.getenv('RABBITMQ_HOST'),
                credentials=pika.PlainCredentials(
                    os.getenv('RABBITMQ_USERNAME'),
                    os.getenv('RABBITMQ_PASSWORD')
                ),
                heartbeat=600,  # Evita desconexión por inactividad
                blocked_connection_timeout=300  # Espera si la conexión está bloqueada
            ))
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Intento {attempt + 1} de {max_retries}: No se pudo conectar a RabbitMQ - {e}")
            time.sleep(retry_delay)

    raise Exception("No se pudo conectar a RabbitMQ después de varios intentos.")


def publish_message(channel, queue, message):
    """Publica un mensaje en la cola y maneja la reconexión si es necesario."""
    try:
        channel.basic_publish(exchange='', routing_key=queue, body=message)
    except (pika.exceptions.AMQPConnectionError, pika.exceptions.ChannelWrongStateError):
        print("Conexión a RabbitMQ perdida. Reintentando...")
        global CONNECTION, temperatura_channel, ocupacion_channel, consumo_channel, seguridad_channel

        CONNECTION = connect_rabbitmq()
        temperatura_channel = CONNECTION.channel(channel_number=1)
        temperatura_channel.queue_declare(queue='temperatura')
        ocupacion_channel = CONNECTION.channel(channel_number=2)
        ocupacion_channel.queue_declare(queue='ocupacion')
        consumo_channel = CONNECTION.channel(channel_number=3)
        consumo_channel.queue_declare(queue='consumo')
        seguridad_channel = CONNECTION.channel(channel_number=4)
        seguridad_channel.queue_declare(queue='seguridad')

        # Reintenta enviar el mensaje
        channel.basic_publish(exchange='', routing_key=queue, body=message)



### Temperatura ###
@app.route('/temperatura', methods=['GET'])
def get_temperatura():
    # Call lector to access the data
    try:
        response = requests.get('http://lector-service:5000/temperatura')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/temperatura', methods=['POST'])
def post_temperatura():
    try:
        message = json.dumps(request.json)
        temperatura_channel.basic_publish(exchange='',
                          routing_key='temperatura',
                          body=message)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Temperatura añadida correctamente'})

######

### Ocupacion ###
@app.route('/ocupacion', methods=['GET'])
def get_ocupacion():
    # Call lector to access the data
    try:
        response = requests.get('http://lector-service:5000/ocupacion')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/ocupacion', methods=['POST'])
def post_ocupacion():
    try:
        message = json.dumps(request.json)
        publish_message(ocupacion_channel, 'ocupacion', message)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

######

### Consumo ###
@app.route('/consumo', methods=['GET'])
def get_consumo():
    # Call lector to access the data
    try:
        response = requests.get('http://lector-service:5000/consumo')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/consumo', methods=['POST'])
def post_consumo():
    try:
        message = json.dumps(request.json)
        publish_message(ocupacion_channel, 'ocupacion', message)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Consumo añadida correctamente'})

######

### Seguridad ###
@app.route('/seguridad', methods=['GET'])
def get_seguridad():
    # Call lector to access the data
    try:
        response = requests.get('http://lector-service:5000/seguridad')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/seguridad', methods=['POST'])
def post_seguridad():
    try:
        message = json.dumps(request.json)
        seguridad_channel.basic_publish(exchange='',
                          routing_key='seguridad',
                          body=message)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Seguridad añadida correctamente'})

######

if __name__ == '__main__':
    time.sleep(20)  # Espera para que RabbitMQ esté listo
    CONNECTION = connect_rabbitmq()

    temperatura_channel = CONNECTION.channel(channel_number=1)
    temperatura_channel.queue_declare(queue='temperatura')

    ocupacion_channel = CONNECTION.channel(channel_number=2)
    ocupacion_channel.queue_declare(queue='ocupacion')

    consumo_channel = CONNECTION.channel(channel_number=3)
    consumo_channel.queue_declare(queue='consumo')

    seguridad_channel = CONNECTION.channel(channel_number=4)
    seguridad_channel.queue_declare(queue='seguridad')

    app.run(host='0.0.0.0', port=8080)
