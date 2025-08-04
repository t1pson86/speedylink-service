# SpeedyLink Service

A high-performance URL shortening service built with Python and FastAPI. The service provides a RESTful API for creating short links, managing them, and tracking click statistics.

## Key Features

- Convert long URLs into short, convenient links
- Custom short URLs (optional)
- JWT authentication
- Link click statistics
- Integration-ready API
- API documentation via Swagger UI

## How URL Shortening Works

### Shortening Algorithm

1. User sends original URL to `/links` endpoint
2. Service validates the URL
3. If user is authenticated and provides a custom code, its availability is checked
4. A database record is created linking the short code to the original URL
5. User receives a short link in format `https://<your-domain>/<short-code>`

### Implementation Details

- Auto-generated codes are always 9 characters long
- Original URLs are checked for availability during creation

## Installation and Setup

### Prerequisites

- Python 3.9+
- PostgreSQL 12+

### Environment Configuration

1. Clone the repository:

```bash
git clone https://github.com/t1pson86/speedylink-service.git
cd speedylink-service
```
2. Create .env file in project root

3. Configure .env file:

```bash
# -- DATABASE SETTINGS -- 
DB_USER='your_username'
DB_PASSWORD='your_password'
DB_HOST='database_host'
DB_PORT='database_port'
DB_NAME='database_name'

# -- JWT SETTINGS --
JWT_ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
SCR_KEY='your_secure_secret_key'
TOKEN_TYPE='Bearer'
```
4. Install dependencies:

```bash
pip install -r requirements.txt
```
5. Run the application:
```bash
python main.py
The service will be available at: http://localhost:8000
```

## API Documentation
Available after launching the service:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## License
This project is licensed under the MIT License. See LICENSE file for details.