import json
import random
import time

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

if __name__ == "__main__":
    while True:
        occupancy_data = generate_occupancy_data()
        print(json.dumps(occupancy_data))  # Devuelve el JSON en la salida estándar
        time.sleep(6)  # Espera 1 minuto antes de la siguiente medición
