Álvaro Felipe Perez y Miguel Gómez Prieto
# Guía de Inicio Rápido

Este documento proporciona una guía rápida para desplegar el proyecto de control de sensores de un edificio inteligente.

## Índice
1. [Requisitos Previos](#requisitos-previos)
2. [Pasos para Iniciar](#pasos-para-iniciar)
    1. [Clonar el Repositorio](#clonar-el-repositorio)
    2. [Crear la red para la infraestructura](#crear-la-red-para-la-infraestructura)
    3. [Levantar la API](#levantar-la-api)
    4. [Levantar los Sensores](#levantar-los-sensores)
3. [Obtener información del servicio](#obtener-informacion-del-servicio)
4. [Funcionamiento del servicio](#funcionamiento-del-servicio)

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
> Por lo tanto puede ser recomendable esperar a que los logs de la API digan que ya está operativa

4.  **Levantar los Sensores:**

    Navega al directorio Sensores (donde se encuentra el archivo `docker-compose.yml`) y ejecuta el siguiente comando:

    ```bash
    cd ..
    cd Sensores/
    docker compose up -d
    ```

    Estos comando iniciará todos los contenedores en segundo plano.

## Obtener información del servicio

Para obtener la información de cada métrica hay que hacer un GET a `http://localhost:8080/métrica`:
- Temperatura y humedad: http://localhost:8080/temperatura
- Ocupación y movimiento: http://localhost:8080/ocupacion
- Consumo de energía: http://localhost:8080/consumo
- Seguridad: http://localhost:8080/seguridad

Devuelve un json con todos los datos que se tienen hasta la fecha de esa métrica.

También proveemos el `lector.ipynb` y `lector.py`, con la función python que permite descargar los datos y meterlos en un DataFrame de pandas


## Funcionamiento del servicio:

Existen diversos sensores de distintos tipos (seguridad, temperatura y humedad, consumo y ocupación) que recopilan información a una determinada frecuencia, cada uno de estos sensores se hospeda en un contenedor docker y envían su información recopilada a la API en formato JSON. 

Para que la información llegue a su destino es necesario que todos los contenedores (la API junto con los sensores) se localicen en la misma red, por eso se tiene que crear una red externa a la que se conecten los contenedores antes de levartarlos, y una vez se encuentren en la misma red, la API abre un puerto de escucha de protocolos http para recibir las peticiones POST de los sensores que se almacenará en documentos csv (una para cada tipo de sensor) en un volumen para garantizar la consistencia de los datos.

***
Se ha implementado una arquitectura de servicios usando colas con RABBITMQ que conectan la API con los servicios que guardan los datos de cada tipo de sensor y evitar que, al recibir demasiados mensajes, acabe descartando algunos y perdiendo información al no poder escribirlos en las tablas de cada sensor. 

Hemos implementado 4 canales (uno para cada tipo de sensor) y una cola en cada canal que se encargan de encolar los mensajes de escritura a los microservicios implementados para interacturar con las tablas. 

Para lograr una mayor consistencia de la infraestructura, hemos implementado un sistema de gestión de errores que, cuando se cierra el servicio de colas por motivos inesperados, automáticamente reinicia el serivcio y vuelve a estar funcional.

***
Por último. la lectura de tablas lo realiza un microservicio que se encarga de transformar los csv en un json y lo devuelve como mensaje.
También proveemos una función python para leer el json de manera sencilla.

> [!NOTE]  
> Los sensores de ocupación dan un error al enviar el mensaje desde el sensor (al enviarlo desde RABBITMQ se añade sin dar error), pero misteriosamente, pero a dar error, el mensaje llega al servicio que guarda ocupción. No hemos conseguido averiguar por qué sucede este error ni como solucionarlo.
