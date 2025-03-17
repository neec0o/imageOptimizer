# Image Optimization API

This API allows for the optimization of images and uses FastAPI and Pillow for implementation. The API supports authentication and can be run in a Docker container. An independent frontend will communicate with the API.

## Technologies

- **FastAPI**: Fast web framework for API development
- **Pillow**: Python Imaging Library for image processing
- **SQLite**: Simple database for authentication
- **Docker**: Containerization of the application

## Features

- Image optimization (compression, resizing)
- User registration and authentication
- Simple API endpoints for image interaction

## Installation

### Prerequisites

- Python 3.7+
- Docker

### Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/neec0o/imageOptimizer.git
   cd imageOptimizer

  - Install requirements: 
   pip install -r requirements.txt

   - Start the Server: 
   uvicorn main:app --reload
   ```
## Docker Init

   ```bash
      docker network create web
      docker run -d --name traefik --network web -p 80:80 -p 443:443 \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v $PWD/traefik.toml:/traefik.toml \
      traefik:v2.9
   ```

   ```bash
      docker-compose up -d --build
   ```