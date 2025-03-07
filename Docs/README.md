# Guía de Inicio Rápido - IBD-Sensores

Este documento proporciona una guía rápida para desplegar el proyecto de control de sensores de un edificio inteligente.

## Requisitos Previos

-   **Docker:** Asegúrate de tener Docker y Docker Compose instalado en tu sistema. Puedes descargarlo desde [https://www.docker.com/get-started](https://www.docker.com/get-started).
-   **Git:** Necesitarás Git para clonar el repositorio. (Sino puedes descargarlo como zip y extraerlo manualmente)

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
    cd API/
    docker compose up -d
    ```

> [!IMPORTANT]  
> Hasta que la API no esté operativa (aproximadamente 21 segundos) no se va a recibir información de los sensores

4.  **Levantar los Sensores:**

    Navega al directorio Sensores (donde se encuentra el archivo `docker-compose.yml`) y ejecuta el siguiente comando:

    ```bash
    cd ..
    cd Sensores/
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

También proveemos el `lector.ipynb` y `lector.py`, con la función python que permite descargar los datos y meterlos en un DataFrame de pandas
    

## Problema que resuelve:


## Cómo funciona el servicio:

Existen diversos sensores de distintos tipos (seguridad, temperatura y humedad, consumo y ocupación) que recopilan información a una determinada frecuencia, cada uno de estos sensores se hospeda en un contenedor docker y envían su información recopilada a la API en formato JSON. Para que la información llegue a su destino es necesario que todos los contenedores (la API junto con los sensores) se localicen en la misma red, por eso se tiene que crear una red externa a la que se conecten los contenedores antes de levartarlos, y una vez se encuentren en la misma red, la API abrirá un puerto de escucha de protocolos http para recibir las peticiones POST de los sensores que almacenará en tablas csv (una para cada tipo de sensor) en un volumen para garantizar la consistencia de los datos.
Para evitar que se saturen las escrituras, se ha implementado la API sobre RABBITMQ para gestionar canales y colas que conectan la API con las tablas de datos de cada tipo de sensor y evitar que, al recibir demasiados mensajes, acabe descartando algunos y perdiendo información al no poder escribirlos en las tablas de cada sensor. Para ello, hemos implementado 4 canales (uno para cada tipo de sensor) que se encargan de encolar los mensajes de escritura a los microservicios implementados para interacturar con las tablas. Para la lectura de dichas tablas, hemos implementado un microservicio que se encarga de las peticiones GET, solicitando las lecturas a cada microservicio que interactua con las tablas.
 
