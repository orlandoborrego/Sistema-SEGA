# Sistema de Gestión de Archivos

Este proyecto es una aplicación web para la gestión de archivos, desarrollada con Flask y PostgreSQL.

## Requisitos
 Docker
 Docker Compose
 SQL Server accesible

## Configuración
1. Copia el archivo `.env.example` a `.env` y completa los valores necesarios.
2. Construye y levanta los servicios:
   ```bash
   docker-compose up --build -d
   ```
3. Accede a la aplicación en: [http://172.23.6.130:8006/](http://172.23.6.130:8006/)

## Estructura del Proyecto
- `app/`: Código fuente de la aplicación Flask
- `config.py`: Configuración de la app
- `run.py`: Punto de entrada
- `requirements.txt`: Dependencias de Python
- `Dockerfile`: Imagen de la app
- `docker-compose.yml`: Orquestación de servicios
- `.env.example`: Variables de entorno de ejemplo

## Migraciones de Base de Datos
Para crear o aplicar migraciones:
```bash
docker-compose exec web flask db init
# o
# docker-compose exec web flask db migrate
# docker-compose exec web flask db upgrade
```

## Licencia
MIT
