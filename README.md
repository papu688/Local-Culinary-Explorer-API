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
   
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run migrations to set up the database:
   ```bash
   python manage.py migrate

5. Create a superuser for accessing the admin panel:
   ```bash
   python manage.py createsuperuser

6. Run the development server:
   ```bash
   python manage.py runserver
   
The server will be running at http://127.0.0.1:8000/.

## Usage

### Authentication

Authenticate users via token-based authentication.

1. Obtain a token by logging in with your credentials.
2. Include the token in the `Authorization` header for all subsequent requests:

    ```
    Authorization: Token <your_token>
    ```

### Example Request

To get a list of all dishes:

   ```bash
   curl -H "Authorization: Token <your_token>" http://127.0.0.1:8000/dishes

## API Endpoints

### Users
- **POST /users/**: Register a new user.
- **GET /users/**: List all users.
- **GET /users/{id}/**: Retrieve a specific user.

### Chefs
- **POST /chefs/**: Add a new chef.
- **GET /chefs/**: List all chefs.
- **GET /chefs/{id}/**: Retrieve a specific chef.

### Dishes
- **POST /dishes/**: Add a new dish.
- **GET /dishes/**: List all dishes.
- **GET /dishes/{id}/**: Retrieve a specific dish.
- **PUT /dishes/{id}/**: Update a dish.
- **DELETE /dishes/{id}/**: Delete a dish.

### Ingredients
- **POST /ingredients/**: Add a new ingredient.
- **GET /ingredients/**: List all ingredients.
- **GET /ingredients/{id}/**: Retrieve a specific ingredient.

### Ratings
- **POST /ratings/**: Add a new rating.
- **GET /ratings/**: List all ratings.
- **GET /ratings/{id}/**: Retrieve a specific rating.








