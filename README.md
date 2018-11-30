# Un Webapp en Contenedores.

## Secciones

1. Docker
    1. Introducción a Docker: que es y como funciona.
        - **Compilar imagen:** `docker build -t class/nginx .`
        - **Montar un volúmen:** `docker run --rm --name my_site -p 8080:80 -v $(pwd)/imgs:/srv/www/site/imgs class/nginx`
    2. Introducción a `docker-compose`.
    3. Ejemplos de como usar Docker y `docker-compose`.
2. Configuración de una applicación Django.
    1. Configuración local: desarrollo, logs, pruebas y debug.
    2. Configuración en producción: Servidor HTTP (Nginx), Servidor WSGI (uwsgi/gunicorn), Aplicación (Django)
    3. Por que diferentes configuraciones?
    4. Por que estas configuraciones?
3. La imagen completa.
    1. Pros y contras de correr estos servicios con y sin contenedores.
    2. Moviendo una aplicación Django a contenedores (contenerizando).
    3. Configuración local: desarrollo, logs, tests, debug.
    4. Configuración en producción: Servidor HTTP, Servidor WSGI, Applicación (Django).
    5. Tips para ir a QA/producción.
4. Recomendaciones.
    1. Manejo de Docker local.
    2. Manejo de contenedores local y en servidores.


kernel de linux

crea una capa de insolacion.
containers are isolated, but share OS and, 
docker corre en una pequeña MV de linux en cualquier otro OS (no recomendado)

Un contenedor se crea a base de imagenes, de una imagen se pueden crear distintos contenedores
Se puede compartir distintas cosas entre contenedores, por ejemplo, un volumen, data, etc

Se utiliza siempre vim Dockerfile

FROM
COPY

-------------------------------
unit_tests Django

ipdb command
se pueden poner breakpoints manualmente o en la bash
