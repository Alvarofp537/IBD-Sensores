from flask import Flask, jsonify
import csv, time

app = Flask(__name__)

# Convertir CSV a JSON
def csv_to_json(csv_string):
    csv_reader = csv.DictReader(csv_string.splitlines())
    json_data = [row for row in csv_reader]
    return json_data        

@app.route('/temperatura', methods=['GET'])
def get_temperatura():
    # Call lector to access the data
    with open('/data/temperatura.csv', 'r') as f:
        response = f.read()
    contenido = response
    json_data = csv_to_json(contenido)
    print('Leyendo temperatura')
    return jsonify(json_data)

@app.route('/ocupacion', methods=['GET'])
def get_ocupacion():
    # Call lector to access the data
    with open('/data/ocupacion.csv', 'r') as f:
        response = f.read()
    contenido = response
    json_data = csv_to_json(contenido)
    print('Leyendo ocupacion')
    return jsonify(json_data)

@app.route('/consumo', methods=['GET'])
def get_consumo():
    # Call lector to access the data
    with open('/data/consumo.csv', 'r') as f:
        response = f.read()
    contenido = response
    json_data = csv_to_json(contenido)
    print('Leyendo consumo')
    return jsonify(json_data)

@app.route('/seguridad', methods=['GET'])
def get_seguridad():
    # Call lector to access the data
    with open('/data/seguridad.csv', 'r') as f:
        response = f.read()
    contenido = response
    json_data = csv_to_json(contenido)
    print('Leyendo seguridad')
    return jsonify(json_data)

if __name__ == '__main__':
    time.sleep(20)  # Wait for RabbitMQ container to initialize
    app.run(host='0.0.0.0', port=5000)