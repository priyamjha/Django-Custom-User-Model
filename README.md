# Custom User Model

## Introduction

This project demonstrates the implementation of a custom user model in Django. By default, Django provides a user model that includes fields like username, email, and password. However, in many cases, you might want to customize the user model to include additional fields or change the authentication method. This project aims to show how you can create and use a custom user model with phone number authentication.

## Why Use a Custom User Model?

Using a custom user model allows you to:

- Customize the fields and methods available on the user model.
- Use a different field for authentication (e.g., phone number instead of username).
- Add additional fields like user bio and profile image.
- Tailor the user model to fit the specific needs of your application.

## Technologies Used

- Python
- Django 5.0.3
- SQLite (default database)

## Features Implemented

- Custom user model with phone number authentication.
- Fields: phone number, email, user bio, profile image.
- Custom user manager for creating users and superusers.
- Custom user authentication backend.

## How It Was Developed

1. **Project Setup**: A new Django project was created using `django-admin startproject`.
2. **App Creation**: An app named `testapp` was created to house the custom user model.
3. **Custom User Model**: A new user model `CustomUser` was defined by extending Django's `AbstractUser`.
4. **User Manager**: A custom user manager `UserManager` was created to handle user creation.
5. **Settings Update**: The `AUTH_USER_MODEL` setting was updated to use the new custom user model.
6. **Migrations**: Database migrations were created and applied to reflect the changes.

## What It Does

This project replaces Django's default user model with a custom user model that uses the phone number for authentication. It includes additional fields like user bio and profile image and provides custom methods for creating regular users and superusers.

## Project Hierarchy

```
CustomUserModel/
│
├── CustomUserModel/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── testapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── manager.py
│   ├── migrations/
│   │   └── __init__.py
│
└── manage.py
```

## Usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/django-custom-user-model.git
    cd django-custom-user-model
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

7. **Access the application**:
    Open a web browser and go to `http://127.0.0.1:8000/admin` to log in with the superuser credentials.

By following these steps, you can start using the custom user model in your Django application. The project demonstrates how to extend Django's built-in user model to fit your specific requirements.
