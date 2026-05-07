# Backend User API

A RESTful API built with Python and Flask for user management. This project demonstrates backend development fundamentals including CRUD operations, modular architecture, database integration, and error handling.

## Features

- Full CRUD operations (Create, Read, Update, Delete)
- Modular architecture using Flask Blueprints
- SQLite database with SQLAlchemy ORM
- Input validation and error handling
- Clean and scalable project structure

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Git and GitHub

## Project Structure

backend-user-api/

├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── database.py
│
├── run.py
├── requirements.txt
└── README.md

## API Endpoints

Get all users  
GET /users  

Create a new user  
POST /users  

Request Body:
{
  "name": "John Doe",
  "email": "john@example.com"
}

Update a user  
PUT /users/<id>  

Delete a user  
DELETE /users/<id>  

## How to Run the Project

1. Clone the repository:

git clone https://github.com/camilocanasteros/backend-user-api.git

2. Install dependencies:

pip install -r requirements.txt

3. Run the application:

python run.py

4. Open in your browser or API client:

http://127.0.0.1:5000

## Future Improvements

- User authentication (JWT)
- Password hashing
- Deployment (Docker or cloud platforms)
- API documentation (Swagger)

## Author

Juan Camilo Canasteros  
https://github.com/camilocanasteros