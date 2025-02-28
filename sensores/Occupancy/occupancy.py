import json
import random
import time
import requests

def generate_occupancy_data():
    """Genera datos simulados de ocupación y movimiento en una zona."""
    data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "occupancy": random.randint(0, 50),  # Número de personas en la zona
        "movement": random.choice([True, False]),  # Si hay movimiento o no
        "location": f"Zone-{random.randint(1, 5)}",  # ID de la zona
        "dwell_time": random.randint(1, 120)  # Tiempo de permanencia en minutos
    }
    return data


API_URL = "http://localhost:5001/data"  # Endpoint de la API de destino

if __name__ == "__main__":
    while True:
        occupancy_data = generate_occupancy_data()

        try:
            response = requests.post(API_URL, json=occupancy_data) #se puede añadir un timeout
            response.raise_for_status()  # Lanza un error si el código de respuesta es un error
            print(json.dumps(occupancy_data)) # Devuelve el JSON en la salida estándar
        except requests.exceptions.RequestException as e:
            print(f" Error al enviar los datos: {e}")

        time.sleep(60)  # Espera 1 minuto antes de la siguiente medición

