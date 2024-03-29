# app_fastapi2024
This repository contains the source code for creating an API using FastAPI in Python. The API is designed to interact with a PostgreSQL database managed through pgAdmin.

## Technologies Used:
- **FastAPI**: FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **pgAdmin**: pgAdmin is a popular open-source administration and development platform for PostgreSQL.
- **Postman**: Postman is a collaboration platform for API development. It's used here for testing the functionality of the API.

## Features:
- **Database Connectivity**: The API connects to a PostgreSQL database managed by pgAdmin using SQLAlchemy.
- **CRUD Operations**: With SQLAlchemy, the API can perform Create, Read, Update, and Delete (CRUD) operations on the database.
- **Testing**: Postman is utilized to test the API's functionality, including path operations for creating, deleting, and retrieving data.
  
## Usage:
1. Ensure you have Python 3.7+ installed on your system.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt

