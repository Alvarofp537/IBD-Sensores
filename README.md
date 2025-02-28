# IBD-Sensores
Primera práctica de IBD

## plNTEAMOAD
la escalibidad de los sensores debeíra poder ser orizontal. 
cada senso0r en un docjer container distinto.
UNA API PARA CADA SENSOR. 
Hayq  generar sda5tos aleatorios.

## Pasos

- [ ] 1. Definir API y modelo.
- [ ] 2. Generar datos aleatorios.
- [ ] 3. Crear sensores.
- [ ] 4. Crear códigos python para la API
- [ ] 5. Preparar dockerfiles. (Uno por cada servicio)
- [ ] 6. Crear docker compose
- [ ] 7. Comprobar funcionamiento

---

### 1. Definir API y modelo
API: 
    - Un microservicio para cada tipo de datos
        - Con un csv donde guarda los datos
URL/tipo_dato con 2 opciones, GET y POST. Hería falta DELETE?? No hay PUT


### Sensores
Hemos implementado las imágenes (mediante un dockerfile) de los 4 sensores y hemos creado un docker-compose para levantar los contenedores.

SALIDAS DE CADA CONTENEDOR:
  - Temperature: {"timestamp": "2025-02-28 12:20:47", "temperature": 31.95, "humidity": 75.91, "air_quality": "low"}
  - Occupancy : {"timestamp": "2025-02-28 12:21:22", "occupancy": 11, "movement": false, "location": "Zone-2", "dwell_time": 94}
  - Power: {"timestamp": "2025-02-28 12:21:45", "power_consumption": 8.59, "voltage": 234.48, "current": 4.46, "power_factor": 0.71}
  - Security: {"timestamp": "2025-02-28 12:22:00", "status": "active", "alerts": "no alert", "alert_level": "medium"}

