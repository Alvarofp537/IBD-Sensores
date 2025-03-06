import json
import random
import time
import requests

def generate_status_data():
    """Genera datos simulados de estado y alertas."""
    alerts = [
        "no alert", "motion detected", "unauthorized person", "abandoned object"
    ]
    alert_levels = [
        "low", "medium", "high"
    ]

    alert = random.choices(alerts, weights=[0.3, 0.2, 0.2, 0.3])[0]
    level=random.choices(alert_levels, weights=[0.3, 0.4, 0.3])[0]
    data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": random.choice(["active", "inactive"]),  # Estado del sistema
        "alerts": alert,  # Alerta generada
        "alert_level": level  # Nivel de alerta asociado
    }
    return data

API_URL = "http://localhost:8080/seguridad"  # Endpoint de la API de destino

if __name__ == "__main__":
    while True:
        status_data = generate_status_data()

        try:
            response = requests.post(API_URL, json=status_data) #se puede añadir un timeout
            response.raise_for_status()  # Lanza un error si el código de respuesta es un error
            print(json.dumps(status_data)) # Devuelve el JSON en la salida estándar
        except requests.exceptions.RequestException as e:
            print(f" Error al enviar los datos: {e}")

        time.sleep(120)  # Espera 2 minutos antes de la siguiente medición

