import json
import random
import time

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

if __name__ == "__main__":
    while True:
        status_data = generate_status_data()
        print(json.dumps(status_data))  # Devuelve el JSON en la salida estándar
        time.sleep(120)  # Espera 2 minutos antes de la siguiente medición
