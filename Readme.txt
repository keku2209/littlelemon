LITTLE LEMON - DJANGO BACKEND PROJECT

GitHub Repository:
https://github.com/keku2209/littlelemon

API ENDPOINTS
Prefix: /restaurant/

Menu API:
GET       /restaurant/menu
POST      /restaurant/menu
GET       /restaurant/menu/<id>
PUT       /restaurant/menu/<id>
PATCH     /restaurant/menu/<id>
DELETE    /restaurant/menu/<id>

Booking API:
GET       /restaurant/bookings
POST      /restaurant/bookings
GET       /restaurant/bookings/<id>
PUT       /restaurant/bookings/<id>
PATCH     /restaurant/bookings/<id>
DELETE    /restaurant/bookings/<id>

Router Booking API:
GET       /restaurant/booking/table/
POST      /restaurant/booking/table/

Authentication:
POST      /restaurant/api-token-auth

Website Pages:
Home:          /restaurant/
About:         /restaurant/about
Menu List:     /restaurant/menu-list
Booking:       /restaurant/booking
Login:         /restaurant/login
Registration:  /restaurant/register

Authentication:
Use the authentication token returned by the token endpoint in the request header:
Authorization: Token YOUR_TOKEN

Testing:
Run the Django test suite using:
python manage.py test

Database:
The project is configured to use MySQL. Configure DB_NAME, DB_HOST,
DB_PORT, DB_USER, DB_PASSWORD and DJANGO_SECRET_KEY for your environment.
