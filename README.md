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
   cd image-optimization-api

  - Install requirements: 
   pip install -r requirements.txt

   - Start the Server: 
   uvicorn main:app --reload

