import json
import random
import time    
import requests
import os 

# Obtener el índice del sensor a partir del hostname del contenedor
SENSOR_ID = os.getenv("HOSTNAME")

def get_air_quality_index():
    """Simula el índice de calidad del aire basado en valores aleatorios."""
    levels = ["low", "medium", "high"]
    return random.choices(levels, weights=[0.6, 0.3, 0.1])[0]

def generate_sensor_data():
    """Genera datos simulados de sensores ambientales."""
    data = {
        "id": SENSOR_ID,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(15.0, 35.0), 2),  # Temperatura en °C
        "humidity": round(random.uniform(30.0, 80.0), 2),  # Humedad en %
        "air_quality": get_air_quality_index()  # Índice de calidad del aire 
    }
    return data
    
API_URL = "http://api-gateway:8080/temperatura"  # Endpoint de la API de destino

if __name__ == "__main__":
    while True:
        sensor_data = generate_sensor_data()
        try:
            response = requests.post(API_URL, json=sensor_data) #se puede añadir un timeout
            response.raise_for_status()  # Lanza un error si el código de respuesta es un error
            print(f" Datos enviados con éxito: {json.dumps(sensor_data)}")
        except requests.exceptions.RequestException as e:
            print(f" Error al enviar los datos: {e}")
        
        time.sleep(30)  # Espera 30 segundos antes de la siguiente medición