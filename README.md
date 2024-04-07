# Hotel Management System API

## Description
Hotel Management System API is designed to support a [React.js frontend project](git@github.com:mahmoud-badri/Hotel-Booking.git) for managing hotel operations. It is built using Django Rest Framework and provides endpoints for various functionalities required in a hotel management system.


# Features

## User Roles
1. Admin: Controls the entire system through the admin panel. Can manage rooms, guests, bookings, and staff.
2. Staff-Hotel: Can manage bookings, check-in/check-out guests, add hotel, update or manage it and view the other hotels.
3. Guest: Can view available Hotel, make bookings.

## Admin
- Control all aspects of the system through the admin panel.

## Staff-hotel
- Add, update, delete Hotel.
- Manage bookings (check-in, check-out).
- View Hotel status (occupied, available).
- View booking details.

## Guest
- View available hotels.
- Make bookings.
- View their own bookings.
- Pay online.

## Related Features
- Confirmation email for register.
- Confirmation email for booking confirmation.
- Email notification for booking updates.

## Technologies
- Django
- Django Rest Framework
- PostgreSQL
- Jazzmin (for admin panel)
- Paymob API (for payment processing)

## How to Use
### Installation
1. Clone the repository
- git clone git@github.com:mahmoud-badri/Django-Rest-Framework.git
- cd hotel-management-api
2. Install the required dependencies.
- pip install -r requirements.txt
3. Apply migrations and create a superuser:
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
4. Run the server:
- python manage.py runserver

## Contributors
- [mahmoud-badri](https://github.com/mahmoud-badri)
- [AhmedMEladawy](https://github.com/AhmedMEladawy)
- [AyaElgedawy](https://github.com/AyaElgedawy)
- [mostafahefzyahmed](https://github.com/mostafahefzyahmed)
- [fadwa7a](https://github.com/fadwa7a)
- [ahmedshehata777](https://github.com/ahmedshehata777)

## Note
This project is the final project of the ITI Full Stack Web Development Using Python Track.

Thank you for reading.
