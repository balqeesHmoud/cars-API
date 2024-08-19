# Cars API

**Author**: Your Name  
**Date**: [19-8-2024]

## Description
This project is a Django-based API for managing car listings. The API includes custom permissions to ensure that only the owner of a car can edit or delete it. The project is set up with Docker and Docker Compose, and it uses PostgreSQL as the database.

## Features
- Users can list, create, update, and delete car listings.
- Custom permission `IsOwnerOrReadOnly` ensures that only the owner can edit or delete their listings.
- Dockerized setup with PostgreSQL as the database.

## Installation
1. Clone the repository.
2. Build the Docker containers with `docker-compose build`.
3. Start the containers with `docker-compose up`.
4. Run migrations with `docker-compose run web python manage.py migrate`.
5. Access the API at `http://localhost:8000`.
