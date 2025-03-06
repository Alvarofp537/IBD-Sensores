# Guía de Inicio Rápido - IBD-Sensores

Este documento proporciona una guía rápida para desplegar el proyecto de control de sensores de un edificio inteligente.

## Requisitos Previos

-   **Docker:** Asegúrate de tener Docker instalado en tu sistema. Puedes descargarlo desde [https://www.docker.com/get-started](https://www.docker.com/get-started).
-   **Docker Compose:** Docker Compose debe estar instalado junto con Docker.
-   **Git:** Necesitarás Git para clonar el repositorio.

## Pasos para Iniciar

1.  **Clonar el Repositorio:**
    Abre tu terminal y ejecuta el siguiente comando para clonar el repositorio:

    ```bash
    git clone https://github.com/Alvarofp537/IBD-Sensores.git
    cd IBD-Sensores
    ```

2.  **Crear la red para la infraestructura:**
    Ejecuta el siguiente comando para crear la red externa necesaria:

    ```bash
    docker network create building-network
    ```

3.  **Levantar la API:**
    Navega al directorio API (donde se encuentra el archivo `docker-compose.yml`) y ejecuta el siguiente comando:

    ```bash
    docker compose up -d
    ```

> [!IMPORTANT]  
> Hasta que la API no esté operativa (aproximadamente 21 segundos) no se va a recibir información de los sensores

4.  **Levantar los Sensores:**

    Navega al directorio Sensores (donde se encuentra el archivo `docker-compose.yml`) y ejecuta el siguiente comando:

    ```bash
    docker compose up -d
    ```

    Estos comando iniciará todos los contenedores en segundo plano.

## Obtener información del ¿servicio?

Para obtener la información de cada métrica hay que hacer un GET a `http://localhost:8080/métrica`:
    - Temperatura y humedad: http://localhost:8080/temperatura
    - Ocupación y movimiento: http://localhost:8080/ocupacion
    - Consumo de energía: http://localhost:8080/consumo
    - Seguridad: http://localhost:8080/seguridad

Devuelve un json con todos los datos que se tienen hasta la fecha de esa métrica.
    