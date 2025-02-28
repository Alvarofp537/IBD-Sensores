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
