# SkyMarket

This project is a marketplace with advertisements. It allows users to view other people's items, post their own items, and leave comments.

### Used

---

- Python 3.10
- Django 3.2.6
- Django REST Framework 3.13.0
- PostgreSQL 12.4
- React
- Docker
- Docker-compose

### Installation

---

### Linux

1. Clone Repository

    ```bash
    git clone https://github.com/Danilu2537/SkyMarket.git
    ```
2. Install Docker and Docker-compose

    ```bash
    sudo apt install docker docker-compose
    ```
3. Create file .env and fill it according to the contents of .env.example


### Usage

---

1. Go to the project folder

    ```bash
    cd SkyMarket
    ```
With frontend

2. Launch docker-compose

    ```bash
    sudo docker-compose up -d
    ```

3. Go to the address in the browser http://localhost

Only api

2. Launch docker-compose api container

    ```bash
    sudo docker-compose up -d api
    ```

### Create a Superuser

---

1. Go to the api container

    ```bash
    sudo docker exec -it skymarket_api_1 bash
    ```

2. Create a Superuser

    ```bash
    python manage.py createsuperuser
    ```

### Documentation

---

API documentation after runnning is available at: \
    http://localhost:8000/swagger/schema \
    http://localhost:8000/swagger/
