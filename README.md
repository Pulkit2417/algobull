# AlgoBulls Backend Developer (Web) - To-Do List App

This project is a Django-based To-Do List application developed as part of the AlgoBulls Backend Developer coding assignment.

## Project Requirements

1. **Design a simple To-Do List App using Django**
2. **Write Unit & Integration tests with 100% coverage**
3. **Use GitHub Actions for basic CI/CD operations**

## Technologies Used

- **Backend Stack**:
  - Python 3.11+
  - Django 4.2.7+
  - Django Rest Framework 3.14.0+

## Installation

1. Clone this repository.
2. Create a virtual environment and activate it.
3. Install dependencies using `pip install -r requirements.txt`.

## Django App Details

- **Models**: Implemented models to store task information including timestamp, title, description, due date, tags, and status.
- **Admin Interface**: Enabled Django admin interface with proper validations and fieldsets for each model.
- **REST APIs**: Utilized Django Rest Framework to create CRUD APIs for tasks with support for Basic Authentication.

## Testing

- **Unit & Integration Tests**: Achieved 100% code coverage by writing extensive tests for models, views, and API endpoints.

## Coverage Report

- 

## Continuous Integration/Continuous Deployment (CI/CD)

- **GitHub Actions**: Configured GitHub Actions for automated testing (unit & integration) and linting using Flake8 and Black.

## How to Run

1. Run the Django server using `python manage.py runserver`.
2. Access the Django admin interface at `http://localhost:8000/admin`.
3. For now it is running at `https://to-do-listapp-7aee02cc25cb.herokuapp.com/`.
4. Admin `https://to-do-listapp-7aee02cc25cb.herokuapp.com/admin`.
5. To-do items `https://to-do-listapp-7aee02cc25cb.herokuapp.com/api/todoitems/`.
6. Tags `https://to-do-listapp-7aee02cc25cb.herokuapp.com/api/tags`.

## Contact Information

For any queries or feedback, please contact:

- **Email**: pulkit2417@gmail.com
