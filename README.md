# Little Lemon Web Application

A Django-based restaurant web application developed as part of the Meta Back-End Developer Professional Certificate. The application includes menu management, table bookings, user authentication, and REST APIs.

## Technologies Used

- Python
- Django
- Django REST Framework
- Django REST Framework Token Authentication
- Djoser
- MySQL
- HTML, CSS, and JavaScript

## Features

- Restaurant home and about pages
- Menu listing and individual menu item pages
- Menu API for retrieving and managing menu items
- Table booking API
- User registration and login pages
- Token-based authentication
- Permissions for authenticated users and managers
- Unit tests for menu and booking functionality

## Project Structure

```text
littlelemon/
    settings.py
    urls.py
    wsgi.py
    asgi.py

restaurant/
    models.py
    serializers.py
    views.py
    urls.py
    migrations/
    tests/
    static/

templates/
    pages/
    partials/

manage.py
Pipfile
Pipfile.lock
README.md
```

## Prerequisites

Install the following before running the application:

- Python 3
- MySQL Server
- Pipenv, if using the provided Pipfile

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/keku2209/littlelemon.git
cd littlelemon
```

### 2. Install dependencies

If Pipenv is installed:

```bash
pipenv install
pipenv shell
```

Alternatively, activate your Python virtual environment and install the dependencies listed in `Pipfile`.

### 3. Configure MySQL

Create a MySQL database for the project. For example:

```sql
CREATE DATABASE littlelemon;
```

Configure the database connection in `littlelemon/settings.py` using environment variables:

- `DB_NAME` — database name
- `DB_HOST` — database host
- `DB_PORT` — database port
- `DB_USER` — MySQL username
- `DB_PASSWORD` — MySQL password

Set `DJANGO_SECRET_KEY` to a secure secret key for your environment. Do not commit real passwords or secret keys to the repository.

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an administrator

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser. The Django admin interface is available at `/admin/`.

## Website Routes

The following routes are defined in the restaurant application:

| Route | Purpose |
|---|---|
| `/` | Home page |
| `/about` | About page |
| `/menu-list` | Menu listing page |
| `/menu-item/<id>` | Individual menu item page |
| `/booking` | Booking page |
| `/login` | Login page |
| `/register` | Registration page |

The exact URL prefix depends on the project's root URL configuration.

## REST API Endpoints

The restaurant application defines the following API routes:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/menu` | Retrieve menu items |
| POST | `/menu` | Create a menu item |
| GET | `/menu/<id>` | Retrieve a menu item |
| PUT/PATCH | `/menu/<id>` | Update a menu item |
| DELETE | `/menu/<id>` | Delete a menu item |
| GET | `/bookings` | Retrieve bookings, optionally filtered by date |
| POST | `/bookings` | Create a booking |
| GET | `/bookings/<id>` | Retrieve a booking |
| PUT/PATCH | `/bookings/<id>` | Update a booking |
| DELETE | `/bookings/<id>` | Delete a booking |
| GET/POST | `/booking/table/` | Booking router endpoint |
| POST | `/api-token-auth` | Obtain an authentication token |

The API routes above assume the root URL configuration includes `restaurant.urls` at `/`. If a prefix is configured, include that prefix in the request URL.

Authenticated endpoints require a valid token in the request header:

```text
Authorization: Token YOUR_TOKEN
```

Menu creation and modification are restricted by the configured permissions. Booking endpoints require authentication.

## Running Tests

Run the project's Django tests with:

```bash
python manage.py test
```

## Repository

GitHub: https://github.com/keku2209/littlelemon

This project was created for educational purposes as part of the Meta Back-End Developer Professional Certificate.
