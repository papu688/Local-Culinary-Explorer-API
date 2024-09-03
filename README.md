# Local Culinary Explorer API

This project is a REST API for a local culinary guide, allowing users to discover, share, and rate dishes. The API supports user registration, dish management, chef profiles, ingredient management, and dish ratings.

## Project Overview

The Local Culinary Explorer API is designed to help users explore local cuisine. Users can create profiles, add dishes with ingredients, rate dishes, and follow chefs. This API is built using Django Rest Framework and uses SQLite for database management.

## Features

- **User Authentication**: Token-based authentication.
- **CRUD Operations**: Full CRUD functionality for dishes, chefs, and ingredients.
- **Dish Ratings**: Rate dishes on a 5-point scale.
- **Chef Profiles**: Manage detailed chef profiles.
- **Filtering**: Filter dishes based on relevant fields like name, chef, and ingredients.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/papu688/Local-Culinary-Explorer-API.git
   cd local-culinary-explorer-API
   
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

   pip install -r requirements.txt

   python manage.py migrate

   Create a virtual environment and activate it:

bash
Code kopieren
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

bash
Code kopieren
pip install -r requirements.txt
Run migrations to set up the database:

bash
Code kopieren
python manage.py migrate
Create a superuser for accessing the admin panel:

bash
Code kopieren
python manage.py createsuperuser
Run the development server:

bash
Code kopieren
python manage.py runserver
The server will be running at http://127.0.0.1:8000/.

Usage
Authentication
Authenticate users via token-based authentication.

Obtain a token by logging in with your credentials.

Include the token in the Authorization header for all subsequent requests:

makefile
Code kopieren
Authorization: Token <your_token>
Example Request
To get a list of all dishes:

bash
Code kopieren
curl -H "Authorization: Token <your_token>" http://127.0.0.1:8000/dishes/
API Endpoints
Users
POST /users/: Register a new user.
GET /users/: List all users.
GET /users/{id}/: Retrieve a specific user.
Chefs
POST /chefs/: Add a new chef.
GET /chefs/: List all chefs.
GET /chefs/{id}/: Retrieve a specific chef.
Dishes
POST /dishes/: Add a new dish.
GET /dishes/: List all dishes.
GET /dishes/{id}/: Retrieve a specific dish.
PUT /dishes/{id}/: Update a dish.
DELETE /dishes/{id}/: Delete a dish.
Ingredients
POST /ingredients/: Add a new ingredient.
GET /ingredients/: List all ingredients.
GET /ingredients/{id}/: Retrieve a specific ingredient.
Ratings
POST /ratings/: Add a new rating.
GET /ratings/: List all ratings.
GET /ratings/{id}/: Retrieve a specific rating.
Models



