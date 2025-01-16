# Práctica Docker: Gestión de Datos con Flask y MySQL

## Descripción de la Aplicación

La aplicación consiste en un portal para introducir datos personales en una base de datos. Utiliza **Flask** como framework para el backend, y **MySQL** como base de datos, todo desplegado mediante **Docker**.

---

## Estructura de la Aplicación

### 1. Dockerfile
- Basado en la imagen `python:3.8-slim`.
- Copia el archivo `requirements.txt` e instala las dependencias:
  - **Flask**: Framework para aplicaciones web.
  - **Flask-SQLAlchemy**: ORM para manejar la base de datos.
  - **python-dotenv**: Para gestionar variables de entorno desde un archivo `.env`.
  - **pymysql**: Driver para conectarse a MySQL.
  - **python-json-logger**: Para generar logs en formato JSON.
- Define un `CMD` para ejecutar `app.py`.

### 2. Docker Compose
- **Servicios**:
  - **app**:
    - Construido desde el Dockerfile en el mismo directorio.
    - Depende del servicio `db`.
    - Mapeamos los puertos y utiliza las variables de entorno definidas en el archivo `.env`.
  - **db**:
    - Basado en la imagen `mysql:5.7`.
    - Configurado con variables de entorno para credenciales y base de datos.
    - Habilita un registro general con el comando `--general-log=1`.
    - Se monta un volumen en el directorio /var/lib/mysql el nombre del volumen es db_data

### 3. app.py
- Tiene la programación para gestionar el CRUD además de la función para ver los logs en formato json. 
- Configura logs en formato JSON, que pueden visualizarse en tiempo real.

---

## Intruciones para verificar su funcionamiento. 

Introducir en el navegador la siguiente dirección *localhost:5000*. Si todo funciona nos saldrá un ¡Hola mundo!. Para verificar y tal como hemos hecho en la aplicación podemos escribir el siguiente comando Docker-Compose logs y nos saldrá los registro de la aplicación. En caso de ser correcto tendría que salir algo como esto:

 ***{"message": "172.25.0.1 - - [16/Jan/2025 10:01:50] \"GET / HTTP/1.1\" 200 -"}***

Para ver los logs en formato json además de la función escrita en App.py necesitamos instalar jq en el sistema. Esto lanzará logs cuando hagamos algunas de los CRUD





