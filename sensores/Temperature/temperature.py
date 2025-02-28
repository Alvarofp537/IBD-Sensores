import json
import random
import time

def get_air_quality_index():
    """Simula el índice de calidad del aire basado en valores aleatorios."""
    levels = ["low", "medium", "high"]
    return random.choices(levels, weights=[0.6, 0.3, 0.1])[0]

def generate_sensor_data():
    """Genera datos simulados de sensores ambientales."""
    data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(15.0, 35.0), 2),  # Temperatura en °C
        "humidity": round(random.uniform(30.0, 80.0), 2),  # Humedad en %
        "air_quality": get_air_quality_index()  # Índice de calidad del aire 
    }
    return data


if __name__ == "__main__":
    while True:
        sensor_data = generate_sensor_data()
        print(json.dumps(sensor_data))  # Devuelve el JSON en la salida estándar
        time.sleep(30)  # Espera 30 segundos antes de la siguiente medición